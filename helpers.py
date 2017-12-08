from flask import session
from werkzeug.security import check_password_hash, generate_password_hash
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

def addUser(username:str, password:str, fullname:str):
    # Hash the password
    hashedpw = generate_password_hash(password)

    # Get a connection to the database and a cursor to use
    conn = getConnection()
    cursor = conn.cursor(prepared=True)

    # SQL Query
    statement = 'INSERT INTO Users (fullname, username, password) VALUE (%s,%s,%s)'
    try:
        cursor.execute(statement, (fullname, username, hashedpw))
        conn.commit()
    except:
        return(False)

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
    statement = ('SELECT s.id, s.name, c.name '
                 'FROM Sets s INNER JOIN Category c ON s.categoryid = c.id '
                 'WHERE s.userid = %s'
                )
    cursor.execute(statement, (userid,))

    # result is an array of arrays with each subarray representing a row
    # In this case, we may get 1 or more or 0 results
    rows = cursor.fetchall()

    # Pack the results into dictionaries
    result = []
    for row in rows:
        d = {'id': row[0], 'name': row[1].decode(), 'category': row[2].decode()}
        result.append(d)

    return result

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

    # SQL Query
    statement = ('SELECT id, front, back, indicator '
                 'FROM Cards '
                 'WHERE Cards.setid = %s'
                )
    cursor.execute(statement, (setid,))

    # result is an array of arrays with each subarray representing a row
    # In this case, we may get 1 or more or 0 results
    rows = cursor.fetchall()

    # Pack the results into dictionaries
    result = []
    for row in rows:
        d = {'id': row[0], 'front': row[1].decode(), 'back': row[2].decode(), 'indicator': row[3]}
        result.append(d)

    return result

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
    statement = 'INSERT INTO Cards (setid, front, back) VALUES (%s, %s, %s)'
    cursor.execute(statement, (setid, cardFront, cardBack))
    conn.commit()

    return(True)
    
def editCard(cardid:int, cardFront:str, cardBack:str) -> bool:
    """Modify a card

    If successfully edited, return true, else return false
    """
    # Get a connection to the database and a cursor to use
    conn = getConnection()
    cursor = conn.cursor(prepared=True)
    
    # SQL Query
    statement = 'UPDATE Cards SET front = %s, back = %s WHERE Cards.id = %s'
    cursor.execute(statement, (cardFront, cardBack, cardid))
    conn.commit()

    return(True)

def deleteCard(cardid:id) -> bool:
    """Delete a card

    If successfully deleted, return true, else return false
    """
    # Get a connection to the database and a cursor to use
    conn = getConnection()
    cursor = conn.cursor(prepared=True)
    
    # SQL Query
    statement = 'DELETE FROM Cards WHERE id = %s'
    cursor.execute(statement, (cardid,))
    
    return(True)

def indicateCard(cardid:int, indicator:bool = False) -> bool:
    """Set the indicator to True or False

    If successfully changed it's value, return true, else return false
    """
    # Get a connection to the database and a cursor to use
    conn = getConnection()
    cursor = conn.cursor(prepared=True)
    
    # SQL Query
    statement = 'UPDATE Cards SET indicator = %(indicator)s WHERE Cards.id = %d;'
    data = (indicator, cardid)
    cursor.execute(statement, data)
    
    # Check if the data is inserted to the Cards table
    statement = 'SELECT * FROM Cards WHERE Cards.id = %d;'
    cursor.execute(statement, (cardid,))
    result = cursor.fetchall()
    if result[4] != indicator):
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
    statement = 'INSERT INTO Category(userid, name) VALUES(%s, %s)'
    data = (session.get('userid'), categoryName)
    cursor.execute(statement, data)
    conn.commit()
    
def addSet(setName:str, category:str) -> bool:
    """Add a new set

    Create an empty set with the given name and category, as well as the
    userid from the session
    If successful, return true, else return false
    """
    # Get a connection to the database and a cursor to use
    conn = getConnection()
    cursor = conn.cursor(prepared=True)
    
    # Find if there is a category with the same name
    s = 'SELECT id FROM Category WHERE userid = %s AND name = %s'
    cursor.execute(s, (session.get('userid'), category))
    results = cursor.fetchall()
    if len(results) < 1:
        addCategory(category)
        cursor.execute(s, (session.get('userid'), category))
        results = cursor.fetchall()
    categoryid = results[0][0]

    s = 'INSERT INTO Sets (name, categoryid, userid) VALUES (%s,%s,%s)'
    cursor.execute(s, (setName, categoryid, session.get('userid')))
    conn.commit()

def editSet(setid:int, newName:str, category:str) -> bool:
    """Change a set's name or category

    If successful, return true, else return false
    """
    # Get a connection to the database and a cursor to use
    conn = getConnection()
    cursor = conn.cursor(prepared=True)

    # Get the categoryid or create one
    s = 'SELECT id FROM Category WHERE userid = %s AND name = %s'
    cursor.execute(s, (session.get('userid'), category))
    results = cursor.fetchall()
    if len(results) < 1:
        addCategory(category)
        cursor.execute(s, (session.get('userid'), category))
        results = cursor.fetchall()
    categoryid = results[0][0]

    # SQL Query
    s = 'UPDATE Sets SET name = %s, categoryid = %s WHERE id = %s;'
    cursor.execute(s, (newName, categoryid, setid))

    return(True)

def modifyCategory(categoryid:int, newName:str) -> bool:
    """Change a category's name

    If successful, return true, else return false
    """
    # Get a connection to the database and a cursor to use
    conn = getConnection()
    cursor = conn.cursor(prepared=True)
    
    # SQL Query
    statement = 'UPDATE Category name = %s WHERE Category.id = %d;'
    data = (newName, categoryid)
    cursor.execute(statement, data)
    
    # Check if the data is inserted to the Cards table
    statement = 'SELECT * FROM Category WHERE Category.id = %d;'
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
    
    # Delete cards in set
    statement = 'DELETE FROM Cards WHERE setid = %s'
    cursor.execute(statement, (setid,))
    
    # Delete set
    statement = 'DELETE FROM Sets WHERE id = %s'
    cursor.execute(statement, (setid,))

    conn.commit()

    return(True)
    
def signOut() -> bool:
    """Sign out the user

    If the user was successfully signed out, return true, else return false
    """
    # Clear userid session variable
    if session.get('userid') is not None:
        session.pop('userid')
        return(True)
    return(False)
