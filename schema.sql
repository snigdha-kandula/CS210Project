CREATE TABLE business(
            business_id CHAR(22) PRIMARY KEY,
            name VARCHAR(50),
            address VARCHAR(30),
            city VARCHAR(30),
            state CHAR(2),
            postal_code VARCHAR(5),
            latitude FLOAT,
            longitude FLOAT,
            stars FLOAT,
            review_count INT,
            is_open INT,
);

CREATE TABLE reviews(
            review_id CHAR(22),
            user_id CHAR(22),
            stars INT,
            date CHAR(10),
            review TEXT,
            useful_votes INT,
            funny_votes INT,
            cool_votes INT
);

