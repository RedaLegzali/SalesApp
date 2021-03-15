# SalesApp

* Description
* Technologies
* Setup

## Description 

SalesApp is a small furnitures e-commerce leveraging relational and non relational databases.

## Technologies

* Furnitures API
  * Python Flask + Mariadb / MySQL
* Sales API
  * Node JS + Mongodb
* Web Application
  * Vue JS

## Setup 

First you have to install the following in your system : 

* Python 3.x
* Node JS 
* Mongodb
* Mariadb or MySQL

Once you have you can clone this repository and start your setup.
Open a terminal in this project directory and follow along
You will need to use multiple terminal windows.

### Mariadb Setup 
  You will have to setup your root user in Mariadb : ```mysql_secure_installation``` <br>
```cd mariadb/``` <br>
```mysql -u root -p < schema.sql``` <br>
```mysql -u root -p furnitures < data.sql``` <br>

### Flask Setup
  ```pip install pipenv``` <br>
  ```cd furnitures/``` <br>
  ```pipenv install``` <br>
  ```pipenv run python run.py``` <br>
  
### Node JS Setup
  ```cd sales/``` <br>
  ```npm install``` <br>
  ```npm start``` <br>
  
### Webapp Setup
  ```cd webapp/``` <br>
  ```npm install``` <br>
  ```npm run serve``` <br>
  ```

