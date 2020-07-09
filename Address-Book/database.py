import sqlite3


def create_table():
    '''function to create a table'''
    conn = sqlite3.connect('addressbook.db')
    c = conn.cursor()
    c.execute("""
                CREATE TABLE addressbook
                (
                    first_name text NOT NULL,
                    last_name text NOT NULL,
                    phone text CHECK(length(phone) >= 10),
                    email text
                )

            """)
    # Commit our command and close the connection
    conn.commit()
    conn.close()


def show_table():
    '''function to show the contents of the table'''
    conn = sqlite3.connect('addressbook.db')
    c = conn.cursor()

    c.execute("SELECT rowid,* FROM addressbook")
    items = c.fetchall()
    for item in items:
        print(item)


def drop_table():
    '''function to delete the table'''
    conn = sqlite3.connect('addressbook.db')
    c = conn.cursor()
    c.execute('DROP TABLE addressbook')

    # after dropping the table, it will create a fresh table with the required columns.
    create_table()

    # Commit our command and close the connection
    conn.commit()
    conn.close()


def insert_record(one_record):
    '''function to insert only one record into the table'''

    conn = sqlite3.connect('addressbook.db')
    c = conn.cursor()

    c.execute("INSERT INTO addressbook VALUES(?,?,?,?)", one_record)

    # Commit our command and close the connection
    conn.commit()
    conn.close()


def delete_record(id):
    '''function to delete a record from the table'''
    conn = sqlite3.connect('addressbook.db')
    c = conn.cursor()

    c.execute("DELETE FROM addressbook WHERE rowid = (?)", id)

    # Commit our command and close the connection
    conn.commit()
    conn.close()


def search_table(keyword):
    '''function to search a record from the table'''
    conn = sqlite3.connect('addressbook.db')
    c = conn.cursor()

    c.execute("SELECT * FROM addressbook WHERE first_name = :first",
              {'first': keyword})
    items = c.fetchall()
    for item in items:
        print(item)
