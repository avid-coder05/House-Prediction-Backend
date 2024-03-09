credentials=[]

def add_cred(data):
    credentials.append([data['username'], data['password']])
    print(credentials)
    return True

def check_cred(data):
    print(credentials)
    for i in credentials:
        if(i[0]==data['username'] and i[1]==data['password']):
            return True

    return False