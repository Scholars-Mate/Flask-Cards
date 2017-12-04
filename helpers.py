from flask import session
from flask import Flask
from werkzeug.security import check_password_hash
from dbconnection import getConnection

def logIn(username: str, password: str) -> bool:
    """Attempt to log a user in

    Uses the given plaintext username and password and tries to log the user in.
    If it succeeds, it adds the userid to the session with the key 'userid' and
    returns True. Otherwise, it only returns False
    """
    # Get a connection to the database and a cursor to use
    conn = getConnection()
    cursor = conn.cursor(prepared=True)

    # SQL Query
    statement = 'SELECT * FROM Users WHERE username = %s'
    cursor.execute(statement, (username,))

    # result is an array of arrays with each subarray representing a row
    # In this case, we only expect to have one, since username is unique
    result = cursor.fetchall()
    if len(result) != 1:
        return(False)
    result = result[0]

    # Check the password
    if not check_password_hash(result[3].decode(), password):
        return(False)

    # Set session values and return
    session['userid'] = result[0]
    return(True)

def getSets(userid:int):
    """Take the userid, display all sets in their account

    Returns the sets as a list of dictionaries with the following keys:
    'id'
    'name'
    'category'
    """
    # Get a connection to the database and a cursor to use
    conn = getConnection()
    cursor = conn.cursor(prepared=True)

    # SQL Query
    statement = 'SELECT * FROM Sets WHERE Sets.userid = %s;'
    cursor.execute(statement, (userid,))

    # result is an array of arrays with each subarray representing a row
    # In this case, we may get 1 or more or 0 results
    result = cursor.fetchall()
    return result
    #not quite sure if we need to fix it or not

def getCards(setid:int):
    """Get all the cards in the given set

    Returns the cards as a list of dictionaries with the following keys:
    'id'
    'front'
    'back'
    'indicator'
    """
    # Get a connection to the database and a cursor to use
    conn = getConnection()
    cursor = conn.cursor(prepared=True)
    
    #SQL Query
    statement = 'SELECT * FROM Cards WHERE Cards.setid = %s;'
    cursor.execute(statement, (setid,))

    # result is an array of arrays with each subarray representing a row
    # In this case, we may get 1 or more or 0 results
    result = cursor.fetchall()
    return result
    #not quite sure if we need to fix it or not

def addCard(cardFront:str, cardBack:str, setid:int) -> bool:
    """Add a new card to the given set

    Uses the given information, and the userid in the session, and adds a card
    to the given set
    If the card was successfully added, return true, else return false
    """
    # Get a connection to the database and a cursor to use
    conn = getConnection()
    cursor = conn.cursor(prepared=True)
    
    # SQL Query
    statement = 'INSERT INTO Cards(front, back, setid) VALUES(%s, %s, %s);'
    data = (cardFront, cardBack, setid)
    cursor.execute(statement, data)
    
    # Check if the data is inserted to the Cards table
    statement = 'SELECT * FROM Cards WHERE front = %s AND back = %s AND setid = %s;'
    data = (cardFront, cardBack, setid)
    cursor.execute(statement, data)
    result = cursor.fetchall()
    if len(result) != 1:
        return (False)
    else:
        return (True)
    
def editCard(cardid:int, cardFront:str, cardBack:str) -> bool:
    """Modify a card

    If successfully edited, return true, else return false
    """
    # Get a connection to the database and a cursor to use
    conn = getConnection()
    cursor = conn.cursor(prepared=True)
    
    # SQL Query
    statement = 'UPDATE Cards SET front = %s, back = %s WHERE Cards.id = %s;'
    data = (cardFront, cardBack, cardid)
    cursor.execute(statement, data)
    
    # Check if the data is inserted to the Cards table
    statement = 'SELECT * FROM Cards WHERE Cards.id = %s;'
    cursor.execute(statement, (cardid,))
    result = cursor.fetchall()
    return result
#    if result[2] != cardFront or result[3] != cardBack:
#        return (False)
#    else:
#        return (True)
    
    #not sure if it's correct, need to test with database

def deleteCard(cardid:id) -> bool:
    """Delete a card

    If successfully deleted, return true, else return false
    """
    # Get a connection to the database and a cursor to use
    conn = getConnection()
    cursor = conn.cursor(prepared=True)
    
    # SQL Query
    statement = 'DELETE FROM Cards WHERE Cards.id = %s;'
    cursor.execute(statement, (cardid,))
    
    # Check if the data is still in the Cards table
    statement = 'SELECT * FROM Cards WHERE Cards.id= %s;'
    cursor.execute(statement, (cardid,))
    result = cursor.fetchall()
    if len(result) != 0:
        return (False)
    else:
        return (True)
    #the statement isn't working on mysql for some reason
    
def indicateCard(cardid:int, indicator:bool = False) -> bool:
    """Set the indicator to True or False

    If successfully changed it's value, return true, else return false
    """
    # Get a connection to the database and a cursor to use
    conn = getConnection()
    cursor = conn.cursor(prepared=True)
    
    # SQL Query
    statement = 'UPDATE Cards SET indicator = %(indicator)s WHERE Cards.id = %s;'
    data = (indicator, cardid)
    cursor.execute(statement, data)
    
    # Check if the data is inserted to the Cards table
    statement = 'SELECT * FROM Cards WHERE Cards.id = %s;'
    cursor.execute(statement, (cardid,))
    result = cursor.fetchall()
    if result[4] != indicator:
        return (False)
    else:
        return (True)
    
    #not sure if it's correct, need to test with database

def addCategory(categoryName:str) -> bool:
    """Add a new category

    Create a new category with the given name, and the userid from the session
    If successfully added, return true, else return false
    """
    # Get a connection to the database and a cursor to use
    conn = getConnection()
    cursor = conn.cursor(prepared=True)
    
    # SQL Query
    statement = 'INSERT INTO Category(userid, name) VALUES(%d, %s)'
    data = (userid, categoryName)
    cursor.execute(statement, data)
    
    # Check if the data is inserted to the Cards table
    statement = 'SELECT * FROM Category WHERE Category.name = %s;'
    cursor.execute(statement, (categoryName,))
    result = cursor.fetchall()
    if len(result) < 1:
        return (False)
    else:
        return (True)

def addSet(setName:str, categoryid:int) -> bool:
    """Add a new set

    Create an empty set with the given name and categoryid, as well as the
    userid from the session
    If successful, return true, else return false
    """
    # Get a connection to the database and a cursor to use
    conn = getConnection()
    cursor = conn.cursor(prepared=True)
    
    # SQL Query
    statement = 'INSERT INTO Set(name, categoryid, userid ) VALUES(%s, %s, %s);'
    data = (setName, categoryid, userid)
    cursor.execute(statement, data)
    
    # Check if the data is inserted to the Cards table
    statement = 'SELECT * FROM Sets WHERE Sets.name = %s;'
    cursor.execute(statement, (setName,))
    result = cursor.fetchall()
    if len(result) < 1:
        return (False)
    else:
        return (True)

def addCategory(categoryName:str) -> bool:
    """Add a new category

    Create an empty category with the given name as well as the
    userid from the session
    If successful, return true, else return false
    """
    # Get a connection to the database and a cursor to use
    conn = getConnection()
    cursor = conn.cursor(prepared=True)
    
    # SQL Query
    statement = 'INSERT INTO Category(name,userid ) VALUES( %s, %s);'
    data = (categoryName, userid)
    cursor.execute(statement, data)
    
    # Check if the data is inserted to the Cards table
    statement = 'SELECT * FROM Category WHERE Category.name = %s;'
    cursor.execute(statement, (categoryName,))
    result = cursor.fetchall()
    if len(result) < 1:
        return (False)
    else:
        return (True)

def modifySet(setid:int, newName:str) -> bool:
    """Change a set's name

    If successful, return true, else return false
    """
    # Get a connection to the database and a cursor to use
    conn = getConnection()
    cursor = conn.cursor(prepared=True)
    
    # SQL Query
    statement = 'UPDATE Sets name = %s WHERE Sets.id = %s;'
    data = (newName, setid)
    cursor.execute(statement, data)
    
    # Check if the data is inserted to the Cards table
    statement = 'SELECT * FROM Sets WHERE Sets.id = %s;'
    cursor.execute(statement, (setid,))
    result = cursor.fetchone()
    if result[1] != newName:
        return (False)
    else:
        return (True)

def modifyCategory(categoryid:int, newName:str) -> bool:
    """Change a category's name

    If successful, return true, else return false
    """
    # Get a connection to the database and a cursor to use
    conn = getConnection()
    cursor = conn.cursor(prepared=True)
    
    # SQL Query
    statement = 'UPDATE Category name = %s WHERE Category.id = %s;'
    data = (newName, categoryid)
    cursor.execute(statement, data)
    
    # Check if the data is inserted to the Cards table
    statement = 'SELECT * FROM Category WHERE Category.id = %s;'
    cursor.execute(statement, (categoryid,))
    result = cursor.fetchone()
    if result[1] != newName:
        return (False)
    else:
        return (True)

def deleteSets(setid:int) -> bool:
    """Delete a set and all cards belonging to it

    If successful, return true, else return false
    """
    # Get a connection to the database and a cursor to use
    conn = getConnection()
    cursor = conn.cursor(prepared=True)
    
    # SQL Query
    statement = 'DELETE FROM Sets WHERE id = %d;'
    cursor.execute(statement, (setid,))
    
    # Check if the data is still in the Cards table
    statement = 'SELECT * FROM Sets WHERE Sets.id= %s;'
    cursor.execute(statement, (cardid,))
    result = cursor.fetchall()
    if len(result) != 0:
        return (False)
    else:
        return (True)
    
def signOut() -> bool:
    """Sign out the user

    If the user was successfully signed out, return true, else return false
    """
    # Set session values and return

    session.pop('logged_in')
    
    if session['userid']:
        return(False)
    else:
        return (True)
