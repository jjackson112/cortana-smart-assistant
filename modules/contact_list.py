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

# search contacts - find by name or job
def search_contacts(self):
  query = input("Enter a keyword to search the contact list" )
  if not query:
    print("Search query cannot be empty.")
    return
  
  found = False

  for contact in self.contacts:
    if query in contact["name"].lower() or query in contact["job"].lower():
      print(f"{contact['name']} | {contact['phone_number']} | {contact['job']}")
    found = True

  if not found:
    print("No matching contacts found.")


# update contacts - find by name or job, edit value only, timestamp
def update_contacts():
  updated_value = input("What needs to be updated? ").strip().lower()

  selected_value = input("Update (n)ame, (p)hone number, or (j)ob? ").strip().lower()
  
# delete contacts
