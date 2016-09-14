"""
Oracle access for  mail listlists.
http://www.oracle.com/technetwork/articles/dsl/prez-transactions-lobs-089563.html
"""

import cx_Oracle
from secrets import banHOST,banUSER,banPASS,banPORT,banSID


class ora_sbcc_lists(object):
	
	
	def __enter__(self):
		dsn_tns = cx_Oracle.makedsn(banHOST, banPORT, banSID)
		self.__db = cx_Oracle.connect(banUSER, banPASS, dsn_tns)
		self.__cursor = self.__db.cursor()
		return self
		
	def __exit__(self,type,value,traceback):
		self.__db.close()
		
	def rows_to_set(self,cursor):
		s = set()
		for row in cursor:
			l.add(row[0])
		return l
	
	def get_ban_list(self,sql):
		
		select_sql = sql
		
		#~ self.__db.begin()
		self.__cursor.execute(sql)
		#~ D = dict(self.__cursor.fetchall())
		#~ return D
		#return self.__cursor.fetchall()
		return self.rows_to_set(self.__cursor)
		
		
