import pandas as pd

db = pd.read_csv("data.csv", index_col=0)


def add_cred(data):
    global db
    new_entries = []

    if data['username'] in db['username'].values:
        return False

    new_entries.append(
        {'username': data['username'], 'password': data['password']})
    new_db = pd.DataFrame(new_entries)
    db = pd.concat([db, new_db], ignore_index=True)
    db.to_csv("data.csv")
    return True


def check_cred(data):
    for index, row in db.iterrows():
        if row['username'] == data['username'] and row['password'] == data['password']:
            return True
    return False
