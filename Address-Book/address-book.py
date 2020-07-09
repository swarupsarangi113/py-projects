import database

functiondict = {

    1: database.show_table,
    2: database.insert_record,
    3: database.drop_table,
    4: database.delete_record,
    5: database.search_table
}

# function asking for user inputs


def user_input():

    print("""

        Hello There, Welcome to Your Address Book
        What do you want to do ?
        
        1. Show All Contacts and Details
        2. Create a New Contact
        3. Delete All the Contacts
        4. Delete a Contact
        5. Search by First Name
        """)

    n = int(input("Enter the option below \n"))
    # if user wants to create a new contact, we need to require inputs like firstname, lastname from the user
    if n == 2:
        onerecord = []
        fname = input('Enter First name\n').lower()
        lname = input('Enter Last name\n').lower()
        ph = input('Enter Phone Number\n').lower()
        email = input('Enter Email Address\n').lower()
        onerecord.extend([fname, lname, ph, email])
        functiondict[n](onerecord)

    # if user wants to delete a record from the table, we need the rowid in string format from the user
    elif n == 4:
        id = input('Enter the Row Number you want to DELETE !\n')
        functiondict[n](id)
    elif n == 5:
        search = input('Enter the first name to search\n').lower()
        functiondict[5](search)

    else:
        functiondict[n]()
    print()
    print('Command successfully executed....')

    m = input('Do you want to perform more actions? y/n \n')
    if m in ('y', 'YES', 'Y', 'yes'):
        user_input()
    else:
        quit()


user_input()
