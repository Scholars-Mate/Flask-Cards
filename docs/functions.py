#skeleton of functions
#Assume all Tables are global

```
from flask import Flask, session, redirect, url_for, escape, request
```

#when the program starts
```
def start():
        if 'username' in session:
		return 'Logged in as %s' %escape(session['username'])
	else
		return 'You are not logged in'
```
#take user's input, check if we have the user data in out database
```
def login(username:str, password:str):
	#call a fddunction to compare the password's hash value, if matched, return true, else return false
	if compare_hashedPassword(username, password):
		return true
	else:
		return false

```

#register a new user, update the Users table
```
def registerANewUser(userName:str, password:str, fullName:str)
	hashedPassword = generateHash(password)
	INSERT INTO Users(username, fullname, hashedPassword)
	VALUES(userName,  fullName, hashedPassword)
```

#if successfully logged in, display the card sets of the user
```
def displayMySets(userid:int) 
	SELECT * FROM Sets
	WHERE Sets.userid == userid
        statement = 'SELECT * FROM Sets WHERE userid == %s'
        cursor.execute(statement, (userid,))

```

#display the cards in a set in the user's account
```
def displayCardsInASet(userid:int, setsid:int)
	SELECT * FROM Cards
	WHERE Cards.setid == Sets.id && Sets.userid == userid
```

#add a card
```
def addCard(cardFront:str, cardBack:str)
	INSERT INTO Cards(front, back, indicator, createdate) VALUES(cardFront, cardBack, false, 
	                                                            TO_DATE('2017/11/20', 'YYYY/MM/DD'))
	#the above TO_DATE function will get the systym time
        if successfully added to table, return true
	else return false

```

#add a card to a set
```
def addToSet(userid:int, setName:str, categoryid:int)
	INSERT INTO Sets(name, userid, createdate) VALUES(setName, userid, caterotyid, 
								TO_DATE('2017/11/20, YYYY/MM/DD'))
def addToSet(userid:int, setName:str)
	INSERT INTO Sets(name, userid, createdate) VALUES(setName, userid,
								TO_DATE('2017/11/20, YYYY/MM/DD'))
	if successfully added to table, return true
	else return false
```

#edit a card
```
def editCard(cardFront:str, cardBack:str)
UPDATE Cards
	SET front = cardFront, back = cardBack

def editCard(cardFront:str)
	UPDATE Cards
	SET front = cardFront

editCard(NULL, CardBack:str)
	UPDATE Cards
	SET back = cardBack
	
	if successfully updated table, return true
	else return false
	according to the parameters, we should have different actions
```

#delete a card
```
deleteCard(cardid:str)
	DELETE FROM Cards
	WHERE id = cardid
	cardSetid = Cards.setid
	deleteCardFromSet(cardSetid:str)

	if successfully deleted the card, return true
	else return false
```

#delete a card from a set
```
deleteCardFromSet(cardSetid:int)
	DELETE FROM Sets
	WHERE Sets.id == cardSetid)
	
	if successfully deleted the card from a set, return true
	else return false
```

#indicat the user can recognize the card of not
```
indicateCard(answer:int)
	UPDATE Cards
	SET indicator = answer #must be 0,1 or NULL
	if successfully updated the indicator, return true
	else return false
```

#settings
```
resetCards()
	DROP SCHEMA IF EXISTS Cards
resetSets()
	DROP SCHEMA IF EXISTS Sets
SignOut()
	SignedIn = false
	
	if successfully reset the cards/sets or signed out, return true
	else return false
```
