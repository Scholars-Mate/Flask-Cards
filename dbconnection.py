from mysql.connector import connect

connInfo = {'user': 'flaskcards',
            'password': '',
            'database': 'flaskcards'}

conn = connect(user=connInfo['user'],
               password=connInfo['password'],
               database=connInfo['database'])

def getConnection():
    global conn
    if not conn.is_connected():
        conn = connect(user=connInfo['user'],
                       password=connInfo['password'],
                       database=connInfo['database'])
    return(conn)
