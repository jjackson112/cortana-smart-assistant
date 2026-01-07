import json

# normalize data after json load

class ContactList:

  def __init__(self, file_path="contacts.path"):
    self.file_path = file_path()
    self.contacts = self.load_contacts()

  def load_contacts(self):
    try:
      with open(self.file_path, "r") as file:
        return json.load(file)
    except:
      return []
   