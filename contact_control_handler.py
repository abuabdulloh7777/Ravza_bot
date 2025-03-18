# contact_control_handler.py

import json
from config import ADMIN_ID

FILE = "premium_contacts.json"

def load_contact_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_contact_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def has_contact_right(user_id):
    data = load_contact_data()
    return data.get(str(user_id), 0) > 0

def use_contact_right(user_id):
    data = load_contact_data()
    if str(user_id) in data and data[str(user_id)] > 0:
        data[str(user_id)] -= 1
        save_contact_data(data)
        return True
    return False

def add_contact_rights(user_id, count):
    data = load_contact_data()
    data[str(user_id)] = data.get(str(user_id), 0) + count
    save_contact_data(data)
