# Intergenerational Conflicts


## MySQL side database

This ap requires an off model database to store data from sessions that can then
be used in other sessions or apps. Otree does not support this, so this app uses a 
seperate database. The app is depoyed on the FEELE server in a Docker container,
so we could have put a database in another container, but the FEELE server has 
a local copy of MySQL which is readily available and reduces container build 
time and size

To that end the following SQL commands only get run once, the first time the app
is deployed on the server, so I have not scripted them, they are for reference
in case the app is ever moved.

### To create the mySQL database for the side data (Use a different password!!)

```
CREATE DATABASE garmin_menopause;
CREATE USER 'garmin_mnopadmin'@'%' IDENTIFIED BY '2oaCBAR5ffa#';
GRANT ALL PRIVILEGES ON `garmin_menopause`.* TO 'garmin_mnopadmin'@'%';
FLUSH PRIVILEGES;

```
### Then as that user, create the the following tables and link with a foreign keys

Load the schema.sql file from the "common" folder
```
```

### To clear the database for a new study

```
delete from fit_to_work_player_scores
```
