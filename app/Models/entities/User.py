from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, username, password, fullname="") -> None:
        self.id = id
        self.username = username
        self.password = password
        self.fullname = fullname
    
    @classmethod
    def verifContra(self, password, user_password):
        return password == user_password

#from werkzeug.security import check_password_hash

    #@classmethod
    #def check_password(self, hashed_password, password):
        #return check_password_hash(hashed_password,password)