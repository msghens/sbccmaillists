#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from google_group_lib import googLib
import log
logger = log.setup_custom_logger('root')
#
#  Mail List Shell. Use this file to create new lists.
#

# Name of mail list. This should  mirror Group email address in settings



listname = 'nc-faculty@sbcc.edu'

logger.info(listname + ' Starting List processing')

# next is the sql. This should be a query that returns email address
# This should call a view in schema sbcc_listsrv
sql = """
select EMAIL_ADDRESS from GV_MASTER_LIST_GG where LIST_FACULTY_NC='Y' or LIST_MANAGER = 'Y'
union
select 'cmalsheimerb@pipeline.sbcc.edu' from dual
union
select 'chgrant@pipeline.sbcc.edu' from dual
"""

#Inistate processing
_list = googLib(listname,sql)
logger.info(listname + ' List processing complete')
