CREATE DATABASE expense_tracker;

USE expense_tracker;

CREATE TABLE expenses(
        id INT AUTO INCREMENT PRIMARY KEY,
        amount INT,
        description VARCHAR(255),
        category VARCHAR(50),
        extra_info VARCHAR(50)
)