**skeleton of functions**


**when the program starts**

bool checkLogin():        
check the login session, see if we can find user's information
if yes, return true, else return no


**take user's input, check if we have the user data in out database**

bool login(username:str, password:str):
call a hash function to generate the hashed password, and compare it and the username with the Users table, 
if they matched return true, else return false



**register a new user, update the Users table**

bool registerANewUser(username:str, password:str, fullName:str)
call hash function to get hashedPassword
take the username, hashedPassword, fullName and insert them to Users table
if successfully inserted, return true, else return false



**if successfully logged in, display the card sets of the user**

bool displayMySets(userid:int) 
take the userid, display all sets in his account
if successfully read the sets, return true, else return false



**if the user clicked on 1 set, display it**

bool displayOneSet(userid:int, setid:int)
get all cards with a specific userid in a set



**add a card**

bool addCard(cardFront = '':str, cardBack = '':str, setid:int)
take the information on a card's front side and/or back side, insert it to Cards table and assign a set to it
if successfully added it, return true, else return false



**edit a card**

bool editCard(cardid:int, cardFront:str, cardBack:str, setid:int)
edit a card's information
if successfully edited it, return true, else return false



**delete a card**

deleteCard(cardid:str)
delete a card from Cards table
if successfully deleted it, return true, else return false



**set the card indicator to 0 or 1**

indicateCard(cardid:int, answer:int = 0)
take a cardid and a number which needs to be 0 or 1
set the card's indicator to the number
if successfully changed it's value, return true, else return false



**settings**

resetCards()
delete evething in the Cards table
resetSets()
delete everthing in the Sets table
SignOut()
sign out the user
