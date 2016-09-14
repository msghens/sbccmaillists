"""
Oracle access for  mail listlists.
http://www.oracle.com/technetwork/articles/dsl/prez-transactions-lobs-089563.html
"""

import cx_Oracle
from secrets import banHOST,banUSER,banPASS,banPORT,banSID

import logging

logger = logging.getLogger('root')

class ora_sbcc_lists(object):
	
	
	def __enter__(self):
		dsn_tns = cx_Oracle.makedsn(banHOST, banPORT, banSID)
		try:
			self.__db = cx_Oracle.connect(banUSER, banPASS, dsn_tns)
			self.__cursor = self.__db.cursor()
		except cx_Oracle.DatabaseError as e:
			error, = e.args
			if error.code == 1017:
				logger.error('Please check your credentials.')
			else:
				logger.error('Database connection error: %s'.format(e))
			raise
			
		return self
		
	def __exit__(self,type,value,traceback):
		try:
			self.__cursor.close()
			self.__db.close()
		except cx_Oracle.DatabaseError:
			logger.error("Database close error")
			pass
		
	def rows_to_set(self,cursor):
		s = set()
		for row in cursor:
			s.add(row[0])
		return s
	
	def get_ban_list(self,sql):
		
		select_sql = sql
		
		#~ self.__db.begin()
		self.__cursor.execute(sql)
		#~ D = dict(self.__cursor.fetchall())
		#~ return D
		#return self.__cursor.fetchall()
		return self.rows_to_set(self.__cursor)
		
		
