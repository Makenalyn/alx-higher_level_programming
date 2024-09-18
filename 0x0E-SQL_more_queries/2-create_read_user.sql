-- create a database and user 
-- user should have only SELECT privilege
CREATE DATABASE `hbtn_0d_2`;
CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT TO 'user_0d_2'@'localhost';
