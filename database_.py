import sqlite3


def convert_to_binary(filename):
    with open(filename, 'rb') as fl:
        blob_data = fl.read()
    return blob_data

def connect():

    db = sqlite3.connect('database_.sqlite3')
    cursor = db.cursor()

    return db, cursor

def create_table():
    db, cursor = connect()

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS persons
                   (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   firstname TEXT NOT NULL,
                   lastname TEXT NOT NULL,
                   gender TEXT CHECK(gender IN ('زن', 'مرد')) NOT NULL,
                   birthdate TEXT NOT NULL,
                   photo BLOB)
        ''')
    db.commit()
    db.close()

def show_members():

    db, cursor = connect()

    cursor.execute('''
            SELECT * FROM persons
        ''')
    members_ = cursor.fetchall()

    db.close()
    return members_

def add_member(fname, lname, gender, birthdate, photo):

    db, cursor = connect()

    rb_photo_data = convert_to_binary(photo)

    cursor.execute('''
            INSERT INTO persons (firstname, lastname, gender, birthdate, photo)
            VALUES (?, ?, ?, ?, ?)
        ''', (fname, lname, gender, birthdate, rb_photo_data))
    
    db.commit()
    db.close()

def delete_user_db(user_id):
    db, cursor = connect()
    cursor.execute('''
        DELETE FROM persons WHERE id=?
    ''', (user_id,))

    db.commit()
    db.close()

def update_user_db(fname, lname, gender, birthdate, photo, user_id):
    db, cursor = connect()

    rb_photo_data = convert_to_binary(photo)

    cursor.execute('''
            UPDATE persons SET firstname=?, lastname=?, gender=?, birthdate=?, photo=?
            WHERE id=?
        ''', (fname, lname, gender, birthdate, rb_photo_data, user_id))
    
    db.commit()
    db.close()