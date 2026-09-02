DROP DATABASE IF EXISTS flask_todo;

CREATE DATABASE flask_todo;

USE flask_todo;

CREATE TABLE user (
    user_id INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    PRIMARY KEY (user_id)
);

CREATE TABLE task (
    task_id INT NOT NULL AUTO_INCREMENT,
    task_title VARCHAR(100) NOT NULL,
    task_description MEDIUMTEXT NOT NULL,
    user_id INT NOT NULL,
    status ENUM('on_going', 'complete', 'discarded') NOT NULL DEFAULT 'on_going',

    PRIMARY KEY (task_id),

    CONSTRAINT fk_task_user
        FOREIGN KEY (user_id)
        REFERENCES user(user_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);