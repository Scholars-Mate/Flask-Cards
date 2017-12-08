# Database Schema

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
