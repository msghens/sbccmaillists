#!/usr/bin/env python2

from google_group_lib import googLib
import log
logger = log.setup_custom_logger('root')
#
#  Mail List Shell. Use this file to create new lists.
#

# Name of mail list. This should  mirror Group email address in settings



listname = 'list@sbcc.edu or list-group@pipeline.sbcc.edu'

logger.info(listname + ' Starting List processing')

# next is the sql. This should be a query that returns email address
# This should call a view in schema sbcc_listsrv
sql = "select 1 from dual"

_list = googLib(listname,sql)



#Inistate processing
_list = googLib(listname)
logger.info(listname + ' List processing complete')
