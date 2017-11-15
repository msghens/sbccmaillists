#!/bin/sh -x
rm -rf google-env
#virtualenv2 --system-site-packages google-env
virtualenv google-env
. /home/ghens/google-env/bin/activate
pip install --upgrade google-api-python-client
pip install --upgrade cx_Oracle
