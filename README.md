
# Flask database app

Flask database app template, with visit and user logging.
Added possibility to reject(ban) ip's from access.



### Installation

Developmental deployment

```bash
  cp .env.dev .env
  pip3 install -r requirements.txt

  python3 run (start | dev)
```

Example gunicorn deployment
```bash
  cp .env.dev .env
  pip3 install -r requirements.txt
  
  python3 -m gunicorn --workers=3 --bind="0.0.0.0:port" src:app
```
