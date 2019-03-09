import sqlite3

db = "face_db"
conn = sqlite3.connect(db)
c = conn.cursor()


def enter_data(uname, email, password):
    uname = str(uname)
    email = str(email)
    password = str(password)
    line = 'INSERT INTO LOGIN VALUES("{name}","{passwd}","{email}")'.format(name=uname,passwd=password,email=email)
    conn.execute(line)
    conn.commit()
    return True


def read_db(username, password):
    if username == '' and password == '':
        print('please enter the details')
    else:
        line = ("SELECT * FROM face_db WHERE Name= " + "'" + username + "' ")
        c.execute(line)
        data = c.fetchall()
        for num in data:
            if num[0] == username:
                if num[1] == password:
                    print("Your login ")
                else:
                    print("check your Password is worng")
        if not data:
            print("check your Name worng")


#conn.close()
