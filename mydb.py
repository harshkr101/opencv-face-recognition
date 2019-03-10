import sqlite3

db = "face_db"
conn = sqlite3.connect(db)
c = conn.cursor()


def enter_data(uname, email, password):
    uname = str(uname)
    email = str(email)
    password = str(password)
    line = 'INSERT INTO LOGIN VALUES("{name}","{passwd}","{email}")'.format(name=uname, passwd=password, email=email)
    line2 = 'SELECT * FROM LOGIN WHERE Name="{name}"'.format(name=uname)
    username_already_present=conn.execute(line2)

    if uname == '' and password == '' and email == '':
        return False

    elif username_already_present is not None:
        return False

    else:
        conn.execute(line)
        conn.commit()
        return True


def check_login(username, password):
    if username == '' and password == '':
        return False
    else:
        line = 'SELECT * FROM LOGIN WHERE Name="{name}"'.format(name=username)
        c.execute(line)
        data = list(c.fetchall())
        for num in data:
            if num[0] == username:
                if num[1] == password:
                    print("Your login ")
                    return True
                else:
                    print("check your Password is wrong")
                    return False
        if data is None:
            print("check your data")
            return False


def close_connection():
    conn.close()
