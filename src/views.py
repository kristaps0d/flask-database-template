# python libs
from flask import request, render_template, Response

# app modules
from src import app

from src.modules.database.connection import DbConnection
from src.modules.database.cursor import DbCursor

from src.modules.routes import PageNotFound, PageForbidden

# database tables
from src.modules.database.schemas.addresses import Addresses
from src.modules.database.schemas.visits import Visits
from src.modules.database.schemas.bans import Bans

# stop indexing
@app.route('/robots.txt')
def no_index():
    _res = Response(response="User-Agent: *\nDisallow: /\n", status=200, mimetype="text/plain")
    _res.headers["Content-Type"] = "text/plain; charset=utf-8"
    return _res

# routing implementation
@app.errorhandler(404)
def page_not_found(e):

    # Path variables
    _full_path = request.full_path.split('?')
    _method, _address = request.method, request.access_route[-1]
    (_url, _args), _status = _full_path, 'ALLOWED'

    with DbConnection('DB_URI') as con:
        with DbCursor(con) as cur:
            # Incoming request logging to database
            AddressesTable = Addresses(cur)
            _res = AddressesTable.SelectAddress(_address)

            if len(_res) < 1:
                AddressesTable.Insert(_address)
                _res = AddressesTable.SelectAddress(_address)

            VisitsTable = Visits(cur)
            (_key, _) = _res[0]

            BansTable = Bans(cur)
            if len(BansTable.SelectId(_key)) > 0:
                # Reject banned ips
                _status = 'REJECTED'

            _url = f'{_url}{"?" if len(_args) > 0 else ""}{_args}'
            VisitsTable.Insert(_key, _url, _method, _status)

    if (_status == 'REJECTED'):
        # Reject
        return PageForbidden()

    if (_method != 'GET'):
        # Reject
        return PageNotFound()

    if (_url != '/'):
        # Reject
        return PageNotFound()

    return render_template('index.html')