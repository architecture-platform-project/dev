DROP DATABASE IF EXISTS arch;

CREATE DATABASE arch;
USE arch;

CREATE TABLE test_table (
    id INTEGER AUTO_INCREMENT,
    message VARCHAR(100),
    PRIMARY KEY (id)
);

INSERT INTO test_table (message) VALUES ('Hello World')