CREATE TABLE restaurants(
            business_id VARCHAR(25) PRIMARY KEY,
            name VARCHAR(50),
            address VARCHAR(30),
            city VARCHAR(30),
            state CHAR(2),
            postal_code VARCHAR(10),
            latitude FLOAT,
            longitude FLOAT,
            stars FLOAT,
            review_count INT,
            is_open INT
);

CREATE TABLE reviews(
            review_id VARCHAR(25) PRIMARY KEY,
            business_id VARCHAR(25),
            user_id VARCHAR(25),
            stars INT,
            review_date CHAR(10),
            review TEXT,
            useful_votes INT,
            funny_votes INT,
            cool_votes INT,
            FOREIGN KEY (business_id) REFERENCES restaurants(business_id)
);



