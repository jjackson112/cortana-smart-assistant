import json

# normalize data after json load

class ContactList:

  def __init__(self, file_path="contacts.path"):
    self.file_path = file_path()
    self.contacts = self.load_contacts()


   