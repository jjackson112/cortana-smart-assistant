import json
from datetime import datetime

# normalize data after json load - take what ever comes out of JSON and force it into a predictable structure my code can rely on
# for example - missing keys, inconsistent casing, extra whitespace, old data formats

class ContactList:

  def __init__(self, file_path="data/contacts.json"):
    self.file_path = (file_path)
    self.contacts = self.normalize_contacts(self.load_contacts())

  def load_contacts(self):
    if not self.file_path.exists():
      return []
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

      if not name or not phone_number or not job:
        continue

      normalized.append({
        "name": name,
        "phone_number": phone_number,
        "job": job,
        "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
      })

    return normalized
    
  def save_contacts(self):
    with open(self.file_path, "w") as file:
      json.dump(self.contacts, file, indent=4)

# add contacts - method of class (data-focused function)
# User → prompt method → data method → save
  def add_contacts(self, name, phone_number, job):
    if any (c["name"].lower() == name.lower() for c in self.contacts):
      raise ValueError("This contact already exists.")
  
    self.contacts.append({
      "name": name.strip(),
      "phone_number": phone_number.strip(),
      "job": job.strip()
    })

    self.save_contacts()

  def add_contacts_prompt(self):
    name = input("Enter name: ").strip()
    phone_number = input("Enter phone number: ").strip()
    job = input("Enter job title: ").strip()

    if not name or not phone_number or not job:
      print("All fields are required.")
      return

    try:
      self.add_contacts(name, phone_number, job)
      print("Contact added successfully.")
    except ValueError as e:
      print(e)

# find contacts as a utility method - search for a single contact by job or name
  def find_contact(self, query):
    query = query.strip().lower()
    for contact in self.contacts:
        if query in contact["name"].lower() or query in contact["job"].lower():
            return contact
    return None

# search contacts - find by name or job
  def search_contacts(self):
    query = input(f"Enter a keyword to search the contact list. " ).strip().lower()
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

# update contacts - find by name, verify existence in self.contacts, edit value only, timestamp
  def update_contacts(self):
    update_query = input("Enter the name of the contact you want to update. ").strip().lower()
    contact = self.find_contact(update_query)
    if not contact:
      return 

    selected_value = input(f"Update (n)ame, (p)hone number, or (j)ob? ").strip().lower()

    if selected_value == "n":
      updated_value = input(f"What's the new name? ").strip()
      if not updated_value:
        print("It cannot be empty")
        return

      if any(c["name"].lower() == updated_value.lower() for c in self.contacts):
        print("This name already exists.")
        return

      contact["name"] = updated_value

    elif selected_value == "p":
      updated_value = input(f"What's the new phone number? ").strip()
      if not updated_value:
        print("It cannot be empty")
        return

      if any(c["phone_number"] == updated_value for c in self.contacts):
        print("This phone number already exists.")
        return

      contact["phone_number"] = updated_value

    elif selected_value == "j":
      updated_value = input(f"What's the new job title? ").strip()
      if not updated_value:
        print("It cannot be empty")
        return

      contact["job"] = updated_value

    else:
      print("Invalid choice")
      return

    # timestamp
    contact["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    self.save_contacts()
    print("Contact updated successfully.")

# delete contacts -verify existence, is the new value valid, overwrite value and save
  def delete_contacts(self):
    delete_name = input(f"What contact would you like to delete? ").strip().lower()
    contact = self.find_contact(delete_name)
    if not contact:
      print("This contact cannot be found.")
      return 

    delete_confirmation = input(f"Are you sure you want to delete '{contact['name']}'? (y/n): ").lower()
    if delete_confirmation != "y":
      return

    self.contacts.remove(contact)
    self.save_contacts()
    print(f"{contact['name']} has been deleted successfully.")