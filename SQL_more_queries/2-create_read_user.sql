-- creating database and user
CREATE DATABASE 'hbtn_0d_2' AND User 'user_0d_2'@'localhost' IF NOT EXISTS IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT TO 'user_0d_2'@'localhost' ON 'hbtn_0d_2';

