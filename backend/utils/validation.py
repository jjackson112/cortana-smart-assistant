# helper method for activity

def require_fields(data, required_fields):
    if not data:
        return False, "INVALID JSON"
    
    missing = [field for field in required_fields if field not in data]
    if not missing:
        return False, f"Missing fields: {missing}"
    
    return True, None