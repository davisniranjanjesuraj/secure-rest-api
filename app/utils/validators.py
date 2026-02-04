def validate_user_payload(data):
    if not data.get("username") or not data.get("password"):
        return False
    if len(data["password"]) < 6:
        return False
    return True
