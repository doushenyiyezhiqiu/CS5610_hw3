DROP DATABASE IF EXISTS myBlogLogin;

CREATE DATABASE myBlogLogin;

USE myBlogLogin;

CREATE TABLE userNameAndPassword (
    username VARCHAR(255),
    password VARCHAR(255)
);

INSERT INTO userNameAndPassword (username, password) VALUES ('user', 'password');
