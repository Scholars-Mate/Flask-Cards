#skeleton of functions
#Assume all Tables are global

#take user's input, check if we have the user data in out database
login(userName, password)
	#call a function to compare the password's hash value, if matched, return true, else return false
	if(compare_hash(userName, password))
		return home_page

	else	return login_page

#take the id and password, compare them with the data in our database
compare_hash(userName, password)
	#simple version: if(hashedPassword = Users.password) return true
	if((hashedPassword = generateHash(password)) == SELECT password FROM Users WHERE Users.username == userName)
		return true
	else
		return false

#register a new user, update the Users table
registerANewUser(userName, password, fullName)
	hashedPassword = generateHash(password)
	INSERT INTO Users(username, fullname, hashedPassword)
	VALUES(userName,  fullName, hashedPassword)

#if successfully logged in, display the card sets of the user
displayMySets(userid) 
	SELECT * FROM Sets
	WHERE Sets.id == userid

#display the cards in a set in the user's account
displayCardsInASet(userid, setsid)
	SELECT * FROM Cards
	WHERE Cards.setid == Sets.id && Sets.userid == userid

#add a card 
addACard(cardFront, cardBack)
	Cards.setid = setid
	Cards.front = cardFront
	Cards.back = cardBack
	Cards.indicator = false
	INSERT INTO Cards(createdate) VALUES(TO_DATE('2017/11/20, 'YYYY/MM/DD'))
	
#add a card to a set
addToSet()

