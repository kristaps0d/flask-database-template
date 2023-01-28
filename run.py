import sys
from src import app

args = sys.argv
if (len(args) > 1):
    # check for functional arguments
    _arg = args[1]
    
    if _arg == 'dev':
        # run development server
        app.run(port=8080, debug=True)
        _arg = None

    if _arg == 'start':
        # run production server
        app.run(port=80, debug=False)
        _arg = None

    if _arg is None:
        quit()

_filename = str(__file__).split('\\')[-1]
raise SystemExit(f'info: {_filename} (argument)\n\tstart\trun production server\n\tdev\trun development server')