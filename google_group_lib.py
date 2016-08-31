#
# Module to keep google group info in one place
#
import httplib2
import os

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools




def getGoogGroup(service,ggroup):
        groupKey = ggroup + '@pipeline.sbcc.edu'
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
def getGoogGroup(service,ggroup):
        groupKey = ggroup + '@pipeline.sbcc.edu'
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
def getGoogGroup(service,ggroup):
        groupKey = ggroup + '@pipeline.sbcc.edu'
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
                                results = service.delete(groupKey=groupEmail, memberKey = group_member + '@pipeline.sbcc.edu')
.execute()
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
