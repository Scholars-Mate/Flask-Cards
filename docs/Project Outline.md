# Project Outline

Decided on by our first meeting, but subject to change

# Functionality

What should our app do?

* Use Flashcards
  * Create flashcards
  * Modify flashcards
  * Delete flashcards

* Log in

* Stretch goals
  * Chat
  * Refresh without reload
  * Making it pretty
  * Notifications/reminders(combined with calendar)
  * Share flashcard sets
  * Upvote/Downvote

# UI

What pages should we have? What kind of functionality should be on each of them?

* Log in page

* Home page
  * Flashcard categories
    * Flashcard sets
    * Sort options
  * Create flashcards
  * Settings
  * Logout

* Flashcard view(for using flashcards)
  * Flip to front/back
  * Flashcard reviews
  * Next/previous buttons
  * Modify
  * Homepage button
  * Indicator(know/don't know)

* Flashcard edit/modify
  * Add/modify flashcard
    * Textbox
      * Front/back
  * Delete card/set

# Tables

What tables in our database do we need?

* Users
  * UID
    * int
    * primary key, not null, auto increment, unique
  * Password
    * varchar(255)
  * Username
    * varchar(15)
  * Full Name
    * varchar(255)

* Flashcard sets
  * set ID
    * int
    * primary key, not null, auto increment, unique
  * Name
    * varchar(255)
  * Category
    * varchar(255)
  * Owner ID
    * int foreign key(uID)
  * timestamp

* Cards
  * card ID
    * int
    * primary key, not null, auto increment, unique
  * front
    * varchar(1023)
  * back
    * varchar(1023)
  * indicator
    * boolean
  * timestamp

* Set to Card Table
  * set ID
  * card ID
