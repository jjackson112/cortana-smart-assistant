import json

# normalize data after json load

class ContactList:

  def __init__(self, file_path="contacts.json"):
    self.file_path = file_path
    self.contacts = self.load_contacts()

  def load_contacts(self):
    try:
      with open(self.file_path, "r") as file:
        return json.load(file)
    except json.JSONDecodeError:
      print("File corrupted. Starting fresh.")
      return []
    
  def save_contacts(self):
    with open(self.file_path, "w") as file:
      json.dump(self.contacts, file, indent=4)

# add contacts - method of class (data-focused function)
  def add_contacts(self, name, phone_number, job):
    if any (c["name"] == name for c in self.contacts):
      raise ValueError("This contact already exists.")
  
    self.contacts.append({
      "name": name,
      "phone_number": phone_number,
      "job": job
    })
    self.save_contacts()

# search contacts 

# update contacts
def update_contacts(self, name):
  for contact in self.contacts:
    input("Which contact would you like to update?")
  
  search_contact_list = input("Would you like to see the contact list? (y/n) ")
    if search_contact_list != "y":
    return

  

# delete contacts
