CREATE DATABASE expense_tracker;

USE expense_tracker;

CREATE TABLE expenses(
        id INT,
        amount INT,
        description VARCHAR(1000),
        category VARCHAR(50),
        extra_info VARCHAR(50)
)