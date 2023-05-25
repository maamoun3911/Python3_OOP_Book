import hashlib


class User:
    def __init__(self, username, password) -> None:
        self.username, self.logged_in = username, False
        self.password = self._encrypt_password(password)
    
    def _encrypt_password(self, password):
        hash_string = self.username+password
        hash_string = hash_string.encode("utf8")
        return hashlib.sha256(hash_string).hexdigest()
    
    def check_password(self, password):
        encrypt = self._encrypt_password(password)
        return self.password == encrypt

class AuthException(Exception):
    def __init__(self, username: str) -> None:
        super().__init__(username)
        self.username = username

class UsernameAlreadyExists(AuthException):
    pass
class ShortPassword(AuthException):
    pass
class InvalidUsername(AuthException):
    pass
class InvalidPassword(AuthException):
    pass
class AlreadyLogin(AuthException):
    pass
class UsernameIsNotExist(AuthException):
    pass
class NotLoggedIn(AuthException):
    pass


class Authentication:
    def __init__(self) -> None:
        self.users: dict[str, User] = {}
    
    def register(self, username, password):
        if username in self.users:
            raise UsernameAlreadyExists(username)
        
        if len(password) < 6:
            raise ShortPassword(username)
        
        self.users[username] = User(username, password)
        self.login(username, password)
    
    def login(self, username, password):
        try:
            user: User = self.users[username]
        except KeyError:
            raise InvalidUsername(username)
        
        else:
            if not user.check_password(password):
                raise InvalidPassword(username)
        
        if user.logged_in:
            raise AlreadyLogin(username)
        user.logged_in = True
    
    def logout(self, username):
        if not self.check_login(username):
            raise NotLoggedIn(username)
        self.users[username].logged_in = False
        
    
    def check_login(self, username):
        if username not in self.users:
            raise UsernameIsNotExist(username)
        return self.users[username].logged_in

authenticator = Authentication()
authenticator.register("admin", "adminpanel")

# UsernameAlreadyExists: admin
# authenticator.register("admin", "adminpanel")

# ShortPassword: Ahmad
# authenticator.register("Ahmad", "admin")

authenticator.logout("admin")
# NotLoggedIn: admin
# authenticator.logout("admin")

# InvalidUsername: adm
# authneticator.login("admi", "adminpanel")

# InvalidPassword: adm
# authneticator.login("admin", "admin")

authenticator.login("admin", "adminpanel")

# AlreadyLogin: admin
# authenticator.login("admin", "adminpanel")


# UsernameIsNotExist: admi
# print(authenticator.check_login("admi"))

print(authenticator.check_login("admin"))

class PermissionError(Exception):
    pass
class NotPermittedUser(Exception):
    pass
class UserAlreadyPermitted(AuthException):
    pass


class Authorizor:
    def __init__(self, authenticator: Authentication) -> None:
        self.permission, self.authenticator = {}, authenticator
        
    def add_permission(self, perm_name):
        try:
            perm_set = self.permission[perm_name]
        except KeyError:
            self.permission[perm_name] = set()
            
        else:
            raise PermissionError(f"{perm_name} is already exist")
    
    def check_permission(self, perm_name):
        try:
            perm_set = self.permission[perm_name]
        except KeyError:
            raise PermissionError(f"{perm_name} isn't exist")
    
    def permit_user(self, perm_name, username):
        try:
            perm_set = self.permission[perm_name]
        except KeyError:
            raise PermissionError(f"{perm_name} isn't exist")
        
        if username in perm_set:
            raise UserAlreadyPermitted(username)
        
        perm_set.add(username)
    
    def check_user_permision(self, perm_name, username):
        if not username in self.permission[perm_name]:
            raise NotPermittedUser(f"{username} hasn't this permission: {perm_name}")
        return True

authorizor = Authorizor(authenticator)
authorizor.add_permission("News Feed")

# PermissionError: News Feed is already exist
# authorizor.add_permission("News Feed")

# PermissionError: News Feeds isn't exist
# authorizor.check_permission("News Feeds")

authorizor.add_permission("News Feeds")

authorizor.permit_user("News Feed", "admin")

# NotPermittedUser: admin hasn't this permission: News Feeds
# authorizor.check_user_permision("News Feeds", "admin")