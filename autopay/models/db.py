

class User():

    def __init__(self, id, username, role):
        self.id = id
        self.username = username
        self.role = role
 
    def is_authenticated(self):
        return True

    def is_active(self):
        return True
 
    def is_anonymous(self):
        return False
 
    def get_id(self):
        return unicode(self.id)
 
    def __repr__(self):
        return '<User %r>' % (self.username)
