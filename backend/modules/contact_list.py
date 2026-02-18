import json
from datetime import datetime
from pathlib import Path
import re

# normalize data after json load - take what ever comes out of JSON and force it into a predictable structure my code can rely on
# for example - missing keys, inconsistent casing, extra whitespace, old data formats

class ContactList:

  def __init__(self, file_path="data/contacts.json"):
    self.file_path = Path(file_path)
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
        "updated_at": contact.get("updated_at")
      })

    return normalized
  
  # no junk characters, length enforced and consistent storage
  def normalize_phone_number(self, phone_number):
    digits = re.sub(r"\D", "", phone_number)

    # Allow US numbers only for now
    if len(digits) == 10:
        return f"{digits[:3]}-{digits[3:6]}-{digits[6:]}"
    
    if len(digits) == 11 and digits.startswith("1"):
        digits = digits[1:]
        return f"{digits[:3]}-{digits[3:6]}-{digits[6:]}"
    
    raise ValueError("Invalid phone number format.")
    
  def save_contacts(self):
    with open(self.file_path, "w") as file:
      json.dump(self.contacts, file, indent=4)

# add contacts - method of class (data-focused function)
# User → prompt method → data method → save
  def add_contacts(self, name, phone_number, job):
    if any (c["name"].lower() == name.lower() for c in self.contacts):
      raise ValueError("This contact already exists.")
    
    normalized_phone_number = self.normalize_phone_number(phone_number)

    if any (c["phone_number"] == normalized_phone_number for c in self.contacts):
      raise ValueError("This phone number already exists.")
  
    self.contacts.append({
      "name": name.strip(),
      "phone_number": normalized_phone_number,
      "job": job.strip(),
      "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    self.save_contacts()

  def add_contacts(self, name, phone_number, job):
    if not name or not phone_number or not job:
      return "All fields are required."
    
    if any(c["name"].lower() == name.lower() for c in self.contacts):
      return "This contact already exists."
    
    try:
      normalized_phone_number = self.normalize_phone_number(phone_number)
    except ValueError as e:
      return str(e)

    if any(c["phone_number"].lower() == normalized_phone_number.lower() for c in self.contacts):
      return "This phone number already exists."
    
    self.add_contacts.append({
      "name": name.strip(),
      "phone_number": phone_number.strip(),
      "job": job.strip(),
      "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    
    self.save_contacts()
    return "Contact added successfully."

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
      return "Search query cannot be empty."  
    found = False

    for contact in self.contacts:
      if query in contact["name"].lower() or query in contact["job"].lower():
        found = True
        return f"{contact['name']} | {contact['phone_number']} | {contact['job']}"

    if not found:
      return "No matching contacts found."

# update contacts - find by name, verify existence in self.contacts, edit value only, timestamp
  def update_contacts(self):
    update_query = input("Enter the name of the contact you want to update. ").strip().lower()
    contact = self.find_contact(update_query)
    if not contact:
      return "Contact not found."

    selected_value = input(f"Update (n)ame, (p)hone number, or (j)ob? ").strip().lower()

    if selected_value == "n":
      updated_value = input(f"What's the new name? ").strip()
      if not updated_value:
        return "It cannot be empty"

      if any(c["name"].lower() == updated_value.lower() for c in self.contacts):
        return "This name already exists."

      contact["name"] = updated_value

    elif selected_value == "p":
      updated_value = input(f"What's the new phone number? ").strip()
      if not updated_value:
        return "It cannot be empty"

      if any(c["phone_number"] == updated_value for c in self.contacts):
        return "This phone number already exists."

      contact["phone_number"] = updated_value

    elif selected_value == "j":
      updated_value = input(f"What's the new job title? ").strip()
      if not updated_value:
        return "It cannot be empty"

      contact["job"] = updated_value

    else:
      return "Invalid choice"

    # timestamp
    contact["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    self.save_contacts()
    return "Contact updated successfully."

# delete contacts -verify existence, is the new value valid, overwrite value and save
  def delete_contacts(self, name, confirm=False):
    contact = self.find_contact(name)
    if not contact:
      return "This contact cannot be found."

    if not confirm:
      return f"Are you sure you want to delete '{contact['name']}'? (y/n): ".lower()

    self.contacts.remove(contact)
    self.save_contacts()
    return f"{contact['name']} has been deleted successfully."