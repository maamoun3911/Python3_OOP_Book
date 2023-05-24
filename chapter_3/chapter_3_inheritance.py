# 1 #
# class ContactList(list):
#     def search(self, name):
#         matching_names = []
#         for contact in self:
#             if name in contact.name:
#                 matching_names.append(f"{contact.name}, {contact.email}")
#         return matching_names

# class Contact:
    
#     all_contacts = ContactList()
    
#     def __init__(self, name, email) -> None:
#         self.name, self.email = name, email
#         self.all_contacts.append(self)

# c1 = Contact("John A", "johna@example.com")
# c2 = Contact("John B", "johnb@example.com")
# c3 = Contact("Jenna C", "jenna@example.com")
# print(Contact.all_contacts.search("John"))

# 2 #
# class LongNameDict(dict):
#     def longest_key(self):
#         longest = ""
#         for key in self:
#             if len(key) > len(longest):
#                 longest = key
#         return longest

# longkeys = LongNameDict()
# longkeys['hello'] = 1
# longkeys['longest yet'] = 5
# longkeys['hello2'] = 'world'
# print(longkeys.longest_key())

# 3 #
# class ContactList(list):
#     def search(self, name):
#         matching_names = []
#         for contact in self:
#             if name in contact.name:
#                 try:
#                     matching_names.append(f"{contact.name}, {contact.email}, {contact.phone}")
#                 except AttributeError:
#                     matching_names.append(f"{contact.name}, {contact.email}")
#         return matching_names

# class Contact:
    
#     all_contacts = ContactList()
    
#     def __init__(self, name, email) -> None:
#         self.name, self.email = name, email
#         self.all_contacts.append(self)


# class Friend(Contact):
    
#     def __init__(self, name, email, phone) -> None:
#         super().__init__(name, email)
#         self.phone = phone
    
#     def __str__(self) -> str:
#         return f"{self.name}, {self.phone}, {self.email}"

# c1 = Contact("John A", "johna@example.com")
# c2 = Contact("John B", "johnb@example.com")
# c3 = Contact("Jenna C", "jenna@example.com")
# c4 = Friend("John Friend", "freind@example.com", 932715313)
# print(Friend.all_contacts.search("John"))

# 4 #
# class ContactList(list):
#     def search(self, name):
#         matching_names = []
#         for contact in self:
#             if name in contact.name:
#                 try:
#                     matching_names.append(f"{contact.name}, {contact.email}, {contact.phone}")
#                 except AttributeError:
#                     matching_names.append(f"{contact.name}, {contact.email}")
#         return matching_names

# class Contact:
    
#     all_contacts = ContactList()
    
#     def __init__(self, name, email) -> None:
#         self.name, self.email = name, email
#         self.all_contacts.append(self)

# class Friend(Contact):
    
#     def __init__(self, name, email, phone) -> None:
#         super().__init__(name, email)
#         self.phone = phone
    
#     def __str__(self) -> str:
#         return f"{self.name}, {self.phone}, {self.email}"

# class MailSender:
#     def send_email(self, message):
#         print(f"Sending mail to {self.email}")
# #         # Add email logic here


# class EmailableContact(Contact, MailSender):
#     pass

# e = EmailableContact("John Smith", "jsmith@example.net")
# print(Contact.all_contacts)
# e.send_email("Hello, test e-mail here")

# 5 #
class Contact:
    all_contacts = []
    
    def __init__(self, name='', email='', **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.email = email
        self.all_contacts.append(self)
        
class AddressHolder:
    def __init__(self, street='', city='', state='', code='', **kwargs):
        super().__init__(**kwargs)
        self.street = street
        self.city = city
        self.state = state
        self.code = code
        
class Friend(Contact, AddressHolder):
    
    def __init__(self, phone='', **kwargs):
        super().__init__(**kwargs)
        self.phone = phone
        
    def __init__(self, phone='', **kwargs):
        kwargs['phone'] = phone
        super().__init__(**kwargs)
        self.phone = phone
        
    def __init__(self, phone='', **kwargs):
        super().__init__(phone=phone, **kwargs)
        self.phone = phone
        