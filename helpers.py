from flask import session
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
    pass

def getCards(setid:int):
    """Get all the cards in the given set

    Returns the cards as a list of dictionaries with the following keys:
    'id'
    'front'
    'back'
    'indicator'
    """
    # Get Database connection and cursor
    conn = getConnection()
    cursor = conn.cursor(prepared=True)

    # Execute the SQL
    s = 'SELECT id, front, back, indicator FROM Cards WHERE setid = %s'
    cursor.execute(s, (setid,))
    results = cursor.fetchall()

    # Pack the results into a list of dictionaries
    ret = []
    for row in results:
        ret.append({'id': row[0],
                    'front': row[1].decode(),
                    'back': row[2].decode(),
                    'indicator': row[3]})
    return(ret)

def addCard(cardFront:str, cardBack:str, setid:int) -> bool:
    """Add a new card to the given set

    Uses the given information, and the userid in the session, and adds a card
    to the given set
    If the card was successfully added, return true, else return false
    """
    pass

def editCard(cardid:int, cardFront:str, cardBack:str) -> bool:
    """Modify a card

    If successfully edited, return true, else return false
    """
    pass

def deleteCard(cardid:id) -> bool:
    """Delete a card

    If successfully deleted, return true, else return false
    """
    pass

def indicateCard(cardid:int, indicator:bool = False) -> bool:
    """Set the indicator to True or False

    If successfully changed it's value, return true, else return false
    """
    pass

def addCategory(categoryName:str) -> bool:
    """Add a new category

    Create a new category with the given name, and the userid from the session
    If successfully added, return true, else return false
    """
    pass

def addSet(setName:str, categoryid:int) -> bool:
    """Add a new set

    Create an empty set with the given name and categoryid, as well as the
    userid from the session
    If successful, return true, else return false
    """
    pass

def modifySet(setid:int, newName:str) -> bool:
    """Change a set's name

    If successful, return true, else return false
    """
    pass

def modifyCategory(categoryid:int, newName:str) -> bool:
    """Change a category's name

    If successful, return true, else return false
    """
    pass

def deleteSets(setid:int) -> bool:
    """Delete a set and all cards belonging to it

    If successful, return true, else return false
    """
    pass

def deleteCategory(categoryid: int) -> bool:
    """Delete a category and all sets belonging to it

    If successful, return true, else return false
    """
    pass

def signOut() -> bool:
    """Sign out the user

    If the user was successfully signed out, return true, else return false
    """
    pass
