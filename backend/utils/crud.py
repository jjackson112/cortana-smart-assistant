# helper methods - when code prints data
# should not know about flask (no db.session.commit(), persistence or SQLAlchemy sessions)

# For each allowed field, if the client sent it, update that attribute on the database object - no hardcoding
# no if "mode" in data: contact.mode = data["mode"] - less error prone + more concise
    # for field in ["mode", "name", "phone", "job"]:
        # if field in data:
            # setattr(contact, field, data[field])

# CRUD specific to avoid duplicated code
def apply_updates(model, data, allowed_fields):
    for field in allowed_fields:
        if field in data:
            setattr(model, field, data[field])
