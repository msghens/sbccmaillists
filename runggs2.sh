#!/bin/sh
export ORACLE_SID='PROD'
. /usr/local/bin/oraenv_local

. /home/ghens/google-env/bin/activate
cd /home/ghens/sbccmaillists
./list-all-campus.py
./list-classified.py
./list-managers.py
./list-all-faculty.py
./list-ft-faculty.py
./list-adjuncts-faculty.py
./list-nc-faculty.py
./list-students-ah.py
./list-students-nc.py
./list-students.py
./list-retirees.py
