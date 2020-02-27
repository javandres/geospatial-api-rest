#!/bin/sh
source venv/bin/activate
exec gunicorn -b 127.0.0.1:5000 --access-logfile - --error-logfile - run:app