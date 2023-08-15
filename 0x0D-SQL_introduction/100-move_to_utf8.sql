-- script to convert hbtn_0c_0 to UTF8
-- Change to the target database
USE hbtn_0c_0;

-- Convert the table collation
ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the field collation
ALTER TABLE first_table
MODIFY COLUMN name VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
