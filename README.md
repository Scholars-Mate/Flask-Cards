
## List of Group Members

* Christopher Wong
* Qiwen Guo
* Haiyan Hu
* Roger Kiew
* Melissa Hollingshed
* Chase Scott

## Link to our program:
http://test.cwong.org/login


## Database Schema

| Users    |              |
| -----    | ---          |
| id       | integer      |
| username | varchar(15)  |
| fullname | varchar(255) |
| password | char(94)     |

| Sets       |              |
| ----       | ---          |
| id         | integer      |
| name       | varchar(255) |
| categoryid | integer      |

| Cards      |               |
| -----      | ---           |
| id         | integer       |
| setid      | integer       |
| front      | varchar(1023) |

| Category |              |
| -------- | ---          |
| id       | integer      |
| userid   | integer      |
| name     | varchar(255) |


## Explanation of CRUD

Create: 
	When the user click “Add Sets!” on the left the homepage, a window will pop up to ask the user type title and category for the new set. After clicked “Add” button, the program will insert data into Sets table based on the input.
``` 
	s = 'SELECT id FROM Category WHERE userid = %s AND name = %s'
```
	In each sets, the user can click the “Add Card” button, a window will pop up to ask the user type the title of the card and the description of the card(referred as card front and card back). AFter clicked “add” button, the program will insert data into Cards table based on the input.
SQL statement used:
```
	statement = 'INSERT INTO Cards (setid, front, back) VALUES (%s, %s, %s)'

```
Read: 
When the user signed in, the program will read the data from the Sets table based on the user’s account.
```
	statement = 'SELECT * FROM Users WHERE username = %s'

```
After the user clicked ”Go to Set” button, the program will read the data from the Sets table based on the selected set.
```
	 statement = ('SELECT s.id, s.name, c.name '
                 'FROM Sets s INNER JOIN Category c ON s.categoryid = c.id '
                 'WHERE s.userid = %s ')

```
Update: 
In each set, when the user click edit, a window will pop up and the user needs to type a new title name and a new category. The program will update the names in the database based on the input.
```
	s = 'UPDATE Sets SET name = %s, categoryid = %s WHERE id = %s;'
```
Delete: 
Same as Update but if the user click delete instead, the program will delete the current set from the database.
```
    # Delete cards in set
    statement = 'DELETE FROM Cards WHERE setid = %s'
    
    # Delete set
    statement = 'DELETE FROM Sets WHERE id = %s'
```
