import json

# normalize data after json load - take what ever comes out of JSON and force it into a predictable structure my code can rely on
# for ex - missing keys, inconsistent casing, extra whitespace, old data formats

class ContactList:

  def __init__(self, file_path="contacts.json"):
    self.file_path = file_path
    self.contacts = self.load_contacts()

  def load_contacts(self):
    try:
      with open(self.file_path, "r") as file:
        return json.load(file)
    # prod-safe behavior - if files dont't exist
    except (FileNotFoundError, json.JSONDecodeError):
      print("File corrupted. Starting fresh.")
      return []
    
  def normalize_contacts(self, raw_contacts):
    normalized = [] # clean, safe version of data

    for contact in raw_contacts:
      if not isinstance(contact, dict): # if it's not a dict then skip it
        continue

      name = str(contact.get("name", "")).strip()
      phone_number = str(contact.get("phone_number","")).strip()
      job = str(contact.get("job", "")).strip()

      if not name:
        continue
      if not phone_number:
        continue
      if not job:
        continue

      normalized.append({
        "name": name,
        "phone_number": phone_number,
        "job": job
      })

      return normalized
    
  def save_contacts(self):
    with open(self.file_path, "w") as file:
      json.dump(self.contacts, file, indent=4)

# add contacts - method of class (data-focused function)
  def add_contacts(self, name, phone_number, job):
    if any (c["name"] == name for c in self.contacts):
      raise ValueError("This contact already exists.")
  
    self.contacts.append({
      "name": name.strip(),
      "phone_number": phone_number.strip(),
      "job": job.strip()
    })
    self.save_contacts()

# search contacts 

# update contacts
def update_contacts(self):
  query = input("Would you like to search the contact list? ")

  if not query:
    print("Search query cannot be empty.")
    return
  
  found = False
  if not found:
    print("Query not found")


  

# delete contacts
