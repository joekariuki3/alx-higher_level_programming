--- Script to creat table 'force_name' if not exist
--- desc id INT, name VARCHAR(256) NOT NULL
DROP TABLE IF EXISTS force_name;
CREATE TABLE IF NOT EXISTS force_name (
	id INT, name VARCHAR(256) NOT NULL);
