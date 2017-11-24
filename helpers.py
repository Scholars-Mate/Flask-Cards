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
