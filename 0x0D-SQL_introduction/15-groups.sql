-- script that list the number of records with same score in table
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score
