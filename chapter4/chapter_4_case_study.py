import hashlib

# just a user defination class 
# it defines username, encryptpassword and user remain out (not logged in)

class User:
    def __init__(self, username, password) -> None:
        self.username, self.logged_in = username, False
        self.password = self._encrypt_password(password)
    
    def _encrypt_password(self, password):
        hash_string = self.username+password
        hash_string = hash_string.encode("utf8")
        return hashlib.sha256(hash_string).hexdigest()
    
    def check_password(self, password):
        encrypt_password = self._encrypt_password(password)
        return encrypt_password == self.password


class AuthException(Exception):
    def __init__(self, username, user=None) -> None:
        super().__init__(username, user)
        self.username, self.user = username, user


class UsernameAlreadyExists(AuthException):
    pass


class PasswordTooShort(AuthException):
    pass

class InvalidUsername(AuthException):
    pass


class InvalidPassword(AuthException):
    pass


# by defination this class makes a dict of User objects
# methods: 1] add_user: add user to authenticator sys(dict) where username is key and User objects is value
#          2] login: checks if user in authenticator sys and swap logged_in User object attr to True if is exist
#          3] is_logged_in: check if User object attr logged_in == True

class Authenticator:
    def __init__(self) -> None:
        self.users: dict[str, User] = {}
    
    def add_user(self, username, password):
        if username in self.users:
            raise UsernameAlreadyExists(username)
        
        if len(password) < 6:
            raise PasswordTooShort
        
        self.users[username] = User(username, password)
    
    def login(self, username, password):
        try:
            user: User = self.users[username]
        except KeyError:
            raise InvalidUsername(f"{username} is not exist")
        
        if not user.check_password(password):
            raise InvalidPassword
        
        user.logged_in = True
        return True
    
    def is_logged_in(self, username):
        if username in self.users:
            return self.users[username].logged_in


authenticator = Authenticator()

class PermissionError(Exception):
    pass

class NotLoggedInError(AuthException):
    pass

class NotPermittedError(AuthException):
    pass


# by defination this class has two attrs one is Authneticator object and second is permission sys (dict) 
# methods: 1] add_permission: add pemission to authorizor sys(dict) where
#               permisiion name is key and username is value in a set()
#          2] permit_user: checks if User object in authorizor authenticator sys object and check
#               if permission is added to authorizor permission sys(dict) object
#          3] check_permission: check if the permission in permission sys(dict) and
#               if User object is logged-in and 
#                   given username in permission sys(dict) of checked permission set values

class Authorizor:
    def __init__(self, authenticator: Authenticator) -> None:
        self.authenticator, self.permission = authenticator, {}
    
    def add_permission(self, perm_name):
        try:
            perm_set = self.permission[perm_name]
        except KeyError:
            self.permission[perm_name] = set()
        else:
            raise PermissionError(f"{perm_name} alread exists")
    
    def permit_user(self, perm_name, username):
        try:
            perm_set = self.permission[perm_name]
        except KeyError:
            raise PermissionError(f"{perm_name} is not exist")
        else:
            if not username in self.authenticator.users:
                raise InvalidUsername(username)
            perm_set.add(username)
    
    def check_permission(self, perm_name, username):
        if not self.authenticator.is_logged_in(username):
            raise NotLoggedInError
        
        try:
            perm_set = self.permission[perm_name]
        except KeyError:
            raise PermissionError(f"{perm_name} isn't exists")
        
        else:
            if not username in self.permission[perm_name]:
                raise NotPermittedError(username)
            return True
        

authorizor = Authorizor(authenticator)

authenticator.add_user("joe", "joepassword")
authorizor.add_permission("paint")
print(authenticator.login("joe", "joepassword"))
authorizor.permit_user("paint", "joe")
print(authorizor.check_permission("paint", "joe"))
