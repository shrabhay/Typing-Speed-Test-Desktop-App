import json
import os

DATA_FILE = 'user_scores.json'


def load_user_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {}


def save_user_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file)
