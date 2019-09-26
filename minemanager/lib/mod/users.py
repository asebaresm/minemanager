from minemanager.lib.helpers.aux import load_whitelist, load_users, store_users

def is_whitelisted(mail):
    wl = load_whitelist()
    if mail in wl:
        return True
    return False

def active_user(id):
    users = load_users()
    return users.get(str(id))

def nick_from(id):
    users = load_users()
    return users[str(id)].split('@')[0]

def email_from(id):
    users = load_users()
    return users[str(id)]

def register_user(id,mail):
    if not is_whitelisted(mail):
        return None
    users = load_users()
    users[str(id)] = mail
    store_users(users)
    return id
