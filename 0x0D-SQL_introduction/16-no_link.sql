-- sccript that list all records in second_table that has name order by scpre
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC
