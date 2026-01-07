import json

class ContactList:

  def __init__(self, name, phone_number, job):
    self.name = name
    self.phone_number = phone_number
    self.job = job

  with open("contacts.json", "r") as file:
    contact_list_data = json.load(file)

    print(contact_list_data)


   