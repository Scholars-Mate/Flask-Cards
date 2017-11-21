#skeleton of functions
#Assume all Tables are global
#global variable: (boolean)signedIn = false


#when the program starts
page start()
	if(signedIn)
		return home_page
	else
		return login_page

#take user's input, check if we have the user data in out database
page login(str:userName, str:password)
	#call a function to compare the password's hash value, if matched, return true, else return false
	if(compare_hash(userName, password))
		signedIn = true
		return home_page

	else	return login_page

#take the id and password, compare them with the data in our database
bool compare_hash(str:userName, str:password)
	#simple version: if(hashedPassword = Users.password) return true
	if((hashedPassword = generateHash(password)) == SELECT password FROM Users WHERE Users.username == userName)
		return true
	else
		return false

#register a new user, update the Users table
void registerANewUser(str:userName, str:password, str:fullName)
	hashedPassword = generateHash(password)
	INSERT INTO Users(username, fullname, hashedPassword)
	VALUES(userName,  fullName, hashedPassword)

#if successfully logged in, display the card sets of the user
void displayMySets(int:userid) 
	SELECT * FROM Sets
	WHERE Sets.id == userid

#display the cards in a set in the user's account
void displayCardsInASet(int:userid, int:setsid)
	SELECT * FROM Cards
	WHERE Cards.setid == Sets.id && Sets.userid == userid

#add a card
bool addCard(str:cardFront, str:cardBack)
	if(!Cards_table)
		CREATE TABLE 'Cards'(
			'id' INT(8) NOT NULL AUTO_INCREMENT,
			'setid' INT(8) DEFAULT '',
			'front' NOT NULL DEFAULT '',
			'back' DEFAULT '',
			'indicator' INT(1) DEFAULT NULL,
			'createdate'DATETIME DEFAULT '',
		)
	INSERT INTO Cards(front, back, indicator, createdate) VALUES(cardFront, cardBack, false, 
	TO_DATE('2017/11/20, 'YYYY/MM/DD'))
	#the above TO_DATE function will get the systym time)
	if successfully added to table, return true
	else return false

#add a card to a set
bool addToSet(int:userid, str:setName, int:categoryid)
	INSERT INTO Sets(name, userid, createdate) VALUES(setName, userid, caterotyid, 
								TO_DATE('2017/11/20, YYYY/MM/DD'))
bool addToSet(int:userid, str:setName)
	INSERT INTO Sets(name, userid, createdate) VALUES(setName, userid,
								TO_DATE('2017/11/20, YYYY/MM/DD'))
	if successfully added to table, return true
	else return false
#edit a card
bool editCard(str:cardFront, str:cardBack)
	UPDATE Cards
	SET front = cardFront, back = cardBack
bool editCard(str:cardFront)
	UPDATE Cards
	SET front = cardFront
bool editCard(NULL, str:CardBack)
	UPDATE Cards
	SET back = cardBack
	
	if successfully updated table, return true
	else return false
	according to the parameters, we should have different actions

#delete a card
bool deleteCard(int:cardid)
	DELETE FROM Cards
	WHERE id = cardid
	cardSetid = Cards.setid
	deleteCardFromSet(int:cardSetid)

	if successfully deleted the card, return true
	else return false

#delete a card from a set
bool deleteCardFromSet(int:cardSetid)
	DELETE FROM Sets
	WHERE Sets.id == cardSetid)
	
	if successfully deleted the card from a set, return true
	else return false

#indicat the user can recognize the card of not
bool indicateCard(int:answer)
	UPDATE Cards
	SET indicator = answer #must be 0,1 or NULL
	if successfully updated the indicator, return true
	else return false

#settings
bool resetCards()
	DROP SCHEMA IF EXISTS Cards
bool resetSets()
	DROP SCHEMA IF EXISTS Sets
bool SignOut()
	SignedIn = false
	
	if successfully reset the cards/sets or signed out, return true
	else return false
