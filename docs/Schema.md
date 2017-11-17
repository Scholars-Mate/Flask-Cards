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
| userid     | integer      |
| createdate | timestamp    |

| Cards      |               |
| -----      | ---           |
| id         | integer       |
| setid      | integer       |
| front      | varchar(1023) |
| back       | varchar(1023) |
| indicator  | boolean       |
| createdate | timestamp     |

| Category |              |
| -------- | ---          |
| id       | integer      |
| userid   | integer      |
| name     | varchar(255) |
