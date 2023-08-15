-- script that display the top 3 of cities temp during July n August
-- ordered by temp DESC
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE (month = 7 or month = 8) GROUP BY city ORDER BY avg_temp DESC LIMIT 3
