DROP DATABASE IF EXISTS myBlogLogin;

CREATE DATABASE myBlogLogin;

USE myBlogLogin;

CREATE TABLE userNameAndPassword (
    username VARCHAR(255),
    password VARCHAR(255)
);

CREATE TABLE welcome_messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    message TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO userNameAndPassword (`username`, `password`) VALUES ('user', 'password');
INSERT INTO userNameAndPassword (`username`, `password`) VALUES ('abc', 'abc');
