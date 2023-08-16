-- script to create table 'unique_id' IF NOT EXISTS
-- id INT DEFAULT 1 UNIQUE
-- na,e VARCHAR(256)
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256))
