CREATE DATABASE IF NOT EXISTS testdb;
USE testdb;
CREATE TABLE IF NOT EXISTS Utilisateurs(courriel varchar(50), motpasse varchar(12), nom varchar(20), avatar varchar(40));
INSERT INTO Utilisateurs VALUES("alice@ulaval.ca","12345","Alice", "MonChat.jpg"),("bob@ulaval.ca","qwerty","Bob", "Grimlock.jpg"),("cedric@ulaval.ca","password","C�dric","smiley.gif"),("denise@ulaval.ca","88888888","Denise","reine.jpg");