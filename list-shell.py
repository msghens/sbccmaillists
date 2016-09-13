#!/usr/bin/env python2

from google_group_lib import googLib

#
#  Mail List Shell. Use this file to create new lists.
#

# Name of mail list. This should  mirror Group email address in settings

listname = 'list@sbcc.edu or list-group@pipeline.sbcc.edu'


# next is the sql. This should be a query that returns email address
# This should call a view in schema sbcc_listsrv
sql = "select 1 from dual"

_list = googLib(listname)



#Inistate processing
_list = googLib(listname)
