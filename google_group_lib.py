#
# Module to keep google group info in one place
#
import httplib2
import os

from apiclient import discovery,errors
import oauth2client
from oauth2client import client
from oauth2client import tools
from listmaster import listmasters
from ora_list import ora_sbcc_lists

class googLib:
	

	
	def __init__(self,ggroup,sql):
		
		#Owners need to be read in
		self.owners = listmasters
	
		self.ggroup = ggroup
		credentials = self.get_credentials()
		http = credentials.authorize(httplib2.Http())
		self.service = discovery.build('admin', 'directory_v1', http=http)
		
		#Get members from banner
		with ora_sbcc_lists() as listm:
			self.listmembers = listm.get_ban_list(sql)
		
		#remove owners
		self.listmembers = [n for n in self.listmembers not in self.owners]
			
		#get members from google
		self.ggroupmembers = self.getGoogGroup()
		

	def get_credentials(self):
		
		"""Gets valid user credentials from storage.
		
		If nothing has been stored, or if the stored credentials are invalid,
		the OAuth2 flow is completed to obtain the new credentials.
		
		Returns:
			Credentials, the obtained credential.
		
		"""
		#https://developers.google.com/admin-sdk/directory/v1/quickstart/python
		
		try:
			import argparse
			flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
		except ImportError:
			flags = None
		
		SCOPES = ['https://www.googleapis.com/auth/admin.directory.user',
			 'https://www.googleapis.com/auth/apps.groups.settings',
			 'https://www.googleapis.com/auth/admin.directory.group']
			 
			 
	

		CLIENT_SECRET_FILE = 'client_secret.json'
		APPLICATION_NAME = 'Santa Barbarbara City College Mail List'
		
		home_dir = os.path.expanduser('~')
		credential_dir = os.path.join(home_dir, '.credentials')
		if not os.path.exists(credential_dir):
			os.makedirs(credential_dir)
		credential_path = os.path.join(credential_dir,'admin-directory_v1-python-quickstart.json')
		store = oauth2client.file.Storage(credential_path)
		credentials = store.get()
		if not credentials or credentials.invalid:
			flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
			flow.user_agent = APPLICATION_NAME
			if flags:
				credentials = tools.run_flow(flow, store, flags)
			else:
				credentials = tools.run(flow, store)
		return credentials
		
		

	def getGoogGroup(self):
			groupKey = self.ggroup
			service = self.service.members()
			all_users = []
			page_token = None
			params = {'groupKey': groupKey}
			


			while True:
					try:
							if page_token:
									params['pageToken'] = page_token
							current_page = service.list(**params).execute()
							all_users.extend(current_page['members'])
							page_token = current_page.get('nextPageToken')
							if not page_token:
									break

					except errors.HttpError as error:
							print 'An error occurred: %s' % error
							break

			user = set()
			for i in all_users:
											#~ print json.dumps(i)
					#~ if (i['role'] == 'MEMBER'):
											if '@' in i['email']:
													user.add(i['email'].split('@')[0])
											else:
													user.add(i['email'])
			return user


	def insert_member_google(service,groupEmail,group_member):
			#Sends the update to google.
					emailaddress = '"' + displayname[group_member] + '"' + ' <' + group_member + '@pipeline.sbcc.edu>'
					member_body = { "email": group_member + '@pipeline.sbcc.edu'}
					#~ member_body = { "email": emailaddress }
					#~ member_body = json.dumps(member_body)
					print member_body

	def getGoogGroup(self):
			groupKey = self.ggroup
			service = self.service.members()
			all_users = []
			page_token = None
			params = {'groupKey': groupKey}
			


			while True:
					try:
							if page_token:
									params['pageToken'] = page_token
							current_page = service.list(**params).execute()
							all_users.extend(current_page['members'])
							page_token = current_page.get('nextPageToken')
							if not page_token:
									break

					except errors.HttpError as error:
							print 'An error occurred: %s' % error
							break

			user = list()
			for i in all_users:
				if i['email'] not in user and 'MEMBER' in i['role']:
					user.append(i['email'])
					print i['role']
			return user


	def insert_member_google(self,service,groupEmail,group_member):
			#Sends the update to google.
					emailaddress = '"' + displayname[group_member] + '"' + ' <' + group_member + '@pipeline.sbcc.edu>'
					member_body = { "email": group_member + '@pipeline.sbcc.edu'}
					#~ member_body = { "email": emailaddress }
					#~ member_body = json.dumps(member_body)
					print member_body
					

	def insert_member_google(service,groupEmail,group_member):
			#Sends the update to google.
					emailaddress = '"' + displayname[group_member] + '"' + ' <' + group_member + '@pipeline.sbcc.edu>'
					member_body = { "email": group_member + '@pipeline.sbcc.edu'}
					#~ member_body = { "email": emailaddress }
					#~ member_body = json.dumps(member_body)
					print member_body
					for n in range(0, 5):
							try:
									results = service.insert(groupKey=groupEmail, body = member_body).execute()
									print json.dumps(results, indent=4)
									print 'Updated: {0}'.format(groupEmail) 
									return results
							except errors.HttpError, e:
									error = simplejson.loads(e.content)
									errorcode = e.resp.status
									errorreason = json.loads(e.content)['error']['errors'][0]['reason']
									print 'Error code: %d' % errorcode
									print 'Error message: %s' % errorreason
									if errorcode == 409:
											return error
									print "Backing off"
									time.sleep((2 ** n) + random.randint(0, 1000) / 1000)
							except Exception,e:
											print str(e)
											print 'problems with group: {0}'.format(groupEmail)
											sys.exit('Could not update')
											#raise

	def delete_member_google(service,groupEmail,group_member):
			#Sends the update to google.
					#~ member_body = { "email": group_member + '@pipeline.sbcc.edu'}
					#~ print member_body
					for n in range(0, 5):
							try:
									results = service.delete(groupKey=groupEmail, 
										memberKey = group_member + '@pipeline.sbcc.edu').execute()
									#~ print json.dumps(results, indent=4)
									#~ print 'Updated: {0}'.format(groupEmail) 
									return results
							except errors.HttpError, e:
									error = simplejson.loads(e.content)
									errorcode = e.resp.status
									errorreason = json.loads(e.content)['error']['errors'][0]['reason']
									print 'Error code: %d' % errorcode
									print 'Error message: %s' % errorreason
									print "Backing off"
									time.sleep((2 ** n) + random.randint(0, 1000) / 1000)
							except Exception,e:
											print str(e)
											print 'problems with group: {0}'.format(groupEmail)
											sys.exit('Could not update')
											#raise
