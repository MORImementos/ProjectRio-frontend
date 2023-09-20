import random
import string
import requests
import time
import os

from connection import Connection

db = Connection()

class User:
    pk       = None
    rk       = None
    ak       = None
    url      = None
    verified = False
    groups   = list()
    success  = False

    def __init__(self, in_user_dict=None):
        # If user details are not specified, randomize user
        if in_user_dict == None:
            in_user_dict = dict()
        length = random.randint(3,20)
        self.username = in_user_dict['Username'] if ('Username' in in_user_dict.keys()) else ''.join(random.choices(string.ascii_letters, k=length))
        self.email = in_user_dict['Email'] if ('Email' in in_user_dict.keys()) else ''.join(random.choices(string.ascii_letters, k=length)) + "@email.com"
        self.password = in_user_dict['Password'] if ('Password' in in_user_dict.keys()) else ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation , k=20))

    def register(self):
        # Post new user
        json = {'Username': self.username, 'Email': self.email, 'Password': self.password}
        response = requests.post("http://127.0.0.1:5000/register/", json=json)
        self.success = (response.status_code == 200)

        # Get user info from db
        query = 'SELECT * FROM rio_user WHERE username = %s'
        params = (self.username,)
        result = db.query(query, params)
        
        self.pk       = result[0]['id']
        self.username = result[0]['username']
        self.email    = result[0]['email']
        self.rk       = result[0]['rio_key']
        self.url      = result[0]['active_url']
        self.password = None # Zero password, even for testing
        self.verified = False

    def verify_user(self):
        response = requests.post(f"http://127.0.0.1:5000/verify_email/{self.url}")
        # Confirm user is verified
        query = 'SELECT * FROM rio_user WHERE username = %s'
        params = (self.username,)
        result = db.query(query, params)
        self.verified = (result[0]['verified'] == True)

        self.refresh()

        return (response.status_code == 200)

    def add_to_group(self, group_name):
        json = {'username': self.username, 'group_name': group_name, 'ADMIN_KEY': os.getenv('ADMIN_KEY')}
        response = requests.post(f"http://127.0.0.1:5000/user_group/add_user", json=json)
        success = (response.status_code == 200)

        if not success:
            return success
        
        self.groups.append('group_name'.lower())
        return success

    def register_api_key(self):
        json = {'Username': self.username}
        response = requests.post(f"http://127.0.0.1:5000/api_key/register/", json=json)
        success = (response.status_code == 200)

        if not success:
            return success
        # Confirm user is verified
        query = ('SELECT * '
                 'FROM api_key ' 
                 'JOIN rio_user ON api_key.id = rio_user.api_key_id '
                 'WHERE rio_user.username = %s ')
        params = (self.username,)
        result = db.query(query, params)
        self.ak = result[0]['api_key']
        return success

    def refresh(self):
        query = ('SELECT * FROM rio_user \n'
                 'WHERE username = %s')
        params = (self.username,)
        result = db.query(query, params)

        self.username = result[0]['username']
        self.email    = result[0]['email']
        self.pk       = result[0]['id']
        self.url      = result[0]['active_url']
        self.verified = result[0]['verified']
        self.rk       = result[0]['rio_key']

        query = ('SELECT * FROM rio_user \n'
                 'JOIN api_key ON api_key.id = rio_user.api_key_id \n'
                 'WHERE username = %s')
        params = (self.username,)
        result = db.query(query, params)

        if len(result) > 0:
            self.ak = result[0]['api_key']
        else:
            self.ak = None

        # User groups
        self.groups.clear()
        query = ('SELECT * '
                 'FROM rio_user ' 
                 'JOIN user_group_user ON rio_user.id = user_group_user.user_id \n'
                 'JOIN user_group ON user_group_user.user_group_id = user_group.id \n'
                 'WHERE rio_user.username = %s ')
        params = (self.username,)
        result = db.query(query, params)
        for result_row in result:
            self.groups.append(result_row['name'])
    
    def to_dict(self):
        return {
            'RioUser PK' : self.pk,
            'Username': self.username,
            'Email': self.email,
            'RioKey': self.rk,
            'APIKey': self.ak,
            'URL': self.url,
            'Verified': self.verified,
            'Groups': self.groups
        }


class CommUser():
    def __init__(self, user, comm_user_pk, comm_id, admin, invited, active, banned, ck):
        self.pk = comm_user_pk
        self.user = user
        self.comm_id = comm_id
        self.admin = admin
        self.invited = invited
        self.active = active
        self.banned = banned
        self.ck = ck
    
    def to_dict(self):
        return {
            'CommUser PK': self.pk,
            'RioUser PK': self.user.pk,
            'CommID': self.comm_id,
            'Admin': self.admin,
            'Invited': self.invited,
            'Active': self.active,
            'Banned': self.banned,
            'CommKey': self.ck
        }

class Community:
    def __init__(self, founder_user, official, private, link, in_comm_dict=None):
        if in_comm_dict == None:
            in_comm_dict = dict()
            length = random.randint(3,20)
            in_comm_dict['community_name'] =  ''.join(random.choices(string.ascii_letters, k=length))
            in_comm_dict['desc'] =  ''.join(random.choices(string.ascii_letters, k=length))

        in_comm_dict['type'] = 'Official' if official else 'Unofficial'
        in_comm_dict['private'] = 1 if private else 0
        in_comm_dict['global_link'] = 1 if link else 0
        in_comm_dict['rio_key'] = founder_user.rk

        response = requests.post("http://127.0.0.1:5000/community/create", json=in_comm_dict)
        self.success = (response.status_code == 200)

        if not self.success:
            return None

        # Community created check, do not check comm user and tag (they function the same regardless, redundant)
        query = 'SELECT * FROM community WHERE name = %s'
        params = (in_comm_dict["community_name"],)
        result = db.query(query, params)

        self.pk = result[0]['id']
        self.name = result[0]['name']
        self.type = result[0]['comm_type']
        self.private = (result[0]['private'] == True)
        self.url = result[0]['active_url']

        # Get founder community user
        query = 'SELECT * FROM community_user WHERE community_id = %s AND user_id = %s'
        params = (str(self.pk),str(founder_user.pk))
        result = db.query(query, params)
        self.founder = CommUser(founder_user, result[0]['id'], self.pk, result[0]['admin'], result[0]['invited'], 
                                result[0]['active'], result[0]['banned'], result[0]['community_key'])
        print(self.founder.to_dict())
        self.members = dict()
        self.members[self.founder.pk] = self.founder

        # Save sponsor
        self.sponsor = founder_user

        self.tags = dict()
        self.tagsets = dict()

        #Get all users and tags that have been created automatically 
        self.refresh()

    #def join_via_url(self, user, name_err=False, url_err=False, rk_err=False):
    def join_via_url(self, user):
        if (self.url != None):
            endpoint = "http://127.0.0.1:5000/community/join/{}/{}".format(self.name, self.url)
        else:
            endpoint = "http://127.0.0.1:5000/community/join/{}".format(self.name)
        response = requests.post(endpoint, json={'rio_key': user.rk})
        success = (response.status_code == 200)

        if not success:
            return success
            
        # Get community user
        query = 'SELECT * FROM community_user WHERE community_id = %s AND user_id = %s'
        params = (str(self.pk),str(user.pk),)
        result = db.query(query, params)
        comm_user = CommUser(user, result[0]['id'], self.pk, result[0]['admin'], result[0]['invited'], 
                             result[0]['active'], result[0]['banned'], result[0]['community_key'])
        self.members[comm_user.pk] = comm_user
        return success
        
    # If invited, join. If not, request outstanding
    def join_via_request(self, user):
        response = requests.post("http://127.0.0.1:5000/community/join", json={'community_name': self.name, 'rio_key': user.rk})
        success = (response.status_code == 200)

        if not success:
            return success

        # Get community user
        query = 'SELECT * FROM community_user WHERE community_id = %s AND user_id = %s'
        params = (str(self.pk),str(user.pk),)
        result = db.query(query, params)
        comm_user = CommUser(user, result[0]['id'], self.pk, result[0]['admin'], result[0]['invited'], 
                             result[0]['active'], result[0]['banned'], result[0]['community_key'])
        self.members[comm_user.pk] = comm_user

        return success
        
    # If requested to join, accept. If not, invite
    def invite(self, admin_user, invitee_dict):
        invite_json = {'rio_key': admin_user.rk, 
                       'community_name': self.name, 
                       'invite_list': [invitee.username for invitee in invitee_dict.values()] }

        response = requests.post("http://127.0.0.1:5000/community/invite", json=invite_json)
        success = (response.status_code == 200)

        if (success):
            self.refresh()
        return success

    # If requested to join, accept. If not, invite
    def manage(self, admin_user, user_list, modification):
        manage_user_list = list()
        for user in user_list:
            temp_dict = {'username': user.username}
            if modification.lower() == 'admin':
                temp_dict['admin'] = True
            elif modification.lower() == 'ban':
                temp_dict['ban'] = True
            elif modification.lower() == 'remove':
                temp_dict['remove'] = True
            manage_user_list.append(temp_dict)
        
        response = requests.post("http://127.0.0.1:5000/community/manage", json={'community_name': self.name, 
                                                                             'rio_key': admin_user.rk, 
                                                                             'user_list': manage_user_list })
        success = (response.status_code == 200)

        if (success):
            self.refresh()
        return success
    
    def key(self, member_rk, action):
        payload = {'rio_key': member_rk, 'action': action, 'community_name': self.name}
        
        response = requests.post("http://127.0.0.1:5000/community/key", json=payload)
        success = (response.status_code == 200)

        if (success):
            self.refresh()
        return success

    def manage_sponsor(self, user, modification):
        json = {'community_name': self.name, 'action': modification, 'rio_key': user.rk}

        response = requests.post("http://127.0.0.1:5000/community/sponsor", json=json)

        success = (response.status_code == 200)

        self.refresh()

        return success

    # Pulls all comm users and updates members list
    def refresh(self):
        query = ('SELECT \n'
                 'rio_user.id AS user_id,\n'
                 'rio_user.email AS email,\n'
                 'rio_user.username AS username,\n'
                 'rio_user.rio_key AS rio_key,\n'
                 'rio_user.verified AS verified,\n'
                 'rio_user.active_url AS url,\n'
                 'community_user.id AS id,\n'
                 'community_user.admin AS admin,\n'
                 'community_user.invited AS invited,\n'
                 'community_user.active AS active,\n'
                 'community_user.banned AS banned,\n'
                 'community_user.community_key AS community_key \n'
                 'FROM community_user \n'
                 'JOIN rio_user ON community_user.user_id = rio_user.id \n'
                 'WHERE community_user.community_id = %s')
        params = (str(self.pk),)
        result = db.query(query, params)
        for result_row in result:
            user = User()
            user.username = result_row['username']
            user.email    = result_row['email']
            user.pk       = result_row['user_id']
            user.verified = result_row['verified']
            user.rk       = result_row['rio_key']
            user.url      = result_row['url']
            comm_user = CommUser(user, result_row['id'], self.pk, result_row['admin'], result_row['invited'], 
                                    result_row['active'], result_row['banned'], result_row['community_key'])
            print(comm_user.to_dict())
            self.members[comm_user.pk] = comm_user

        #Get tags
        query = ('SELECT * \n'
                 'FROM tag \n'
                 'WHERE community_id = %s')
        params = (str(self.pk),)
        result = db.query(query, params)
        for result_row in result:
            tag = Tag(self.founder, self)        
            tag.pk      = result_row['id']
            tag.refresh()

            self.tags[tag.pk] = tag

        #Get tagsets
        query = ('SELECT * \n'
                 'FROM tag_set \n'
                 'WHERE community_id = %s')
        params = (str(self.pk),)
        result = db.query(query, params)
        for result_row in result:
            tagset = TagSet(self.founder, self, self.tags.values(), "NULL")        
            tagset.pk         = result_row['id']
            tagset.refresh()

            self.tagsets[tagset.pk] = tagset

        # Get the sponsor
        query = ('SELECT * \n'
                 'FROM rio_user \n'
                 'JOIN community ON community.sponsor_id = rio_user.id \n'
                 'WHERE community.id = %s')
        params = (str(self.pk),)
        result = db.query(query, params)

        if len(result) == 0:
            self.sponsor = None
        else:
            user = User()
            user.username = result[0]['username']
            user.email    = result[0]['email']
            user.pk       = result[0]['id']
            user.verified = result[0]['verified']
            user.rk       = result[0]['rio_key']
            user.refresh()

            self.sponsor = user   

    def get_member(self, user):
        for comm_user in self.members.values():
            if comm_user.user.pk == user.pk:
                return comm_user
        return None

class Tag:
    # Tag type will always be component if a test is creating it
    def __init__(self, admin_comm_user, community, type="Component", tag_details=None):
        if tag_details == None:
            tag_details = dict()
        if 'name' not in tag_details.keys():
            length = random.randint(3,20)
            tag_details['name'] =  ''.join(random.choices(string.ascii_letters, k=length))
        if 'desc' not in tag_details.keys():
            length = random.randint(3,20)
            tag_details['desc'] =  ''.join(random.choices(string.ascii_letters, k=length))
        tag_details['community_name'] = community.name
        tag_details['type'] = type
        tag_details['rio_key'] = admin_comm_user.user.rk

        self.init_dict = tag_details

        self.community = community

    def create(self):
        # Post Tag
        response = requests.post("http://127.0.0.1:5000/tag/create", json=self.init_dict)

        self.success = (response.status_code == 200)

        if not self.success:
            return self.success

        query = 'SELECT * FROM tag WHERE name = %s'
        params = (self.init_dict['name'],)
        result = db.query(query, params)
        
        self.pk      = result[0]['id']
        self.name    = result[0]['name']
        self.comm_id = result[0]['community_id']
        self.type    = result[0]['tag_type']
        self.active  = result[0]['active']

        self.community.refresh()

        return self.success

    def refresh(self):
        query = 'SELECT * FROM tag WHERE id = %s'
        params = (str(self.pk),)
        result = db.query(query, params)

        self.pk      = result[0]['id']
        self.name    = result[0]['name']
        self.comm_id = result[0]['community_id']
        self.type    = result[0]['tag_type']
        self.active  = result[0]['active']

class TagSet:
    def __init__(self, admin_comm_user, community, tags, tag_type, tagset_details=None):
        if tagset_details == None:
            tagset_details = dict()
            length = random.randint(3,20)
            tagset_details['name'] =  ''.join(random.choices(string.ascii_letters, k=length))
            tagset_details['desc'] =  ''.join(random.choices(string.ascii_letters, k=length))
            tagset_details['start_date'] = int( time.time() )
            tagset_details['end_date'] = int( time.time() ) + random.randrange(100000, 1000000)
        tagset_details['community_name'] = community.name
        tagset_details['rio_key'] = admin_comm_user.user.rk
        tagset_details['type'] = tag_type
        tagset_details['tags'] = [tag.pk for tag in tags]

        self.community = community
        self.creator_comm_user = admin_comm_user
        self.tags = dict()
        self.init_dict = tagset_details

    def create(self):
        response = requests.post("http://127.0.0.1:5000/tag_set/create", json=self.init_dict)
        self.success = (response.status_code == 200)
        if not self.success:
            return self.success

        query = 'SELECT * FROM tag_set WHERE name = %s'
        params = (self.init_dict['name'],)
        result = db.query(query, params)
        
        self.pk         = result[0]['id']
        self.name       = result[0]['name']
        self.comm_id    = result[0]['community_id']
        self.type       = result[0]['type']
        self.start_date = result[0]['start_date']
        self.end_date   = result[0]['end_date']

        self.refresh() # NEed to refresh to get the non provided tags
        self.community.refresh()

        return self.success

    def refresh(self):
        #Get tagsets
        query = ('SELECT * \n'
                 'FROM tag_set \n'
                 'WHERE id = %s')
        params = (str(self.pk),)
        result = db.query(query, params)      
        self.pk         = result[0]['id']
        self.name       = result[0]['name']
        self.comm_id    = result[0]['community_id']
        self.type       = result[0]['type']
        self.start_date = result[0]['start_date']
        self.end_date   = result[0]['end_date']

        #Get tags
        query = ('SELECT * \n'
                 'FROM tag_set_tag \n'
                 'WHERE tagset_id = %s')
        params = (str(self.pk),)
        result = db.query(query, params)
        for result_row in result:
            tag = Tag(self.creator_comm_user, self.community)
            tag.pk      = result_row['tag_id']
            tag.refresh()

            self.tags[tag.pk] = tag

def wipe_db():
    response = requests.post("http://127.0.0.1:5000/wipe_db/", json={"ADMIN_KEY": "NUKE"})
    return response.status_code == 200

def reset_db():
    response = requests.post("http://127.0.0.1:5000/init_db/", json={"ADMIN_KEY": "NUKE"})
    return response.status_code == 200

def get_community_members(community_name, user):
    json = {'community_name': community_name, 'rio_key': user.rk}
    response = requests.get("http://127.0.0.1:5000/community/members", json=json)
    success = response.status_code == 200

    data = response.json()

    return [success, data]

def compare_comm_user_to_dict(comm_user_dict, comm_user):
    return ( comm_user_dict['user_id'] == comm_user.user.pk
         and comm_user_dict['id']      == comm_user.pk
         and comm_user_dict['admin']   == comm_user.admin
         and comm_user_dict['active']  == comm_user.active
         and comm_user_dict['invited'] == comm_user.invited
         and comm_user_dict['banned']  == comm_user.banned )

def get_community_tags(community_name, user):
    json = {'community_name': community_name, 'rio_key': user.rk}
    response = requests.get("http://127.0.0.1:5000/community/tags", json=json)
    success = response.status_code == 200

    data = response.json()

    return [success, data]

def compare_comm_tag_to_dict(tag_dict, tag):
    return ( tag_dict['id']      == tag.pk
         and tag_dict['comm_id'] == tag.comm_id
         and tag_dict['name']    == tag.name
         and tag_dict['type']    == tag.type
         and tag_dict['active']  == tag.active )

def compare_users(user_a, user_b):
    return (user_a.pk == user_b.pk
        and user_a.rk == user_b.rk
        and user_a.ak == user_b.ak
        and user_a.url == user_b.url
        and user_a.verified == user_b.verified)
