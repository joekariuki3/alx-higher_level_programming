-- script that lists all cities contained in the database hbtn_0d_usa
-- Each record should display: cities.id - cities.name - states.name
SELECT cities.id, cities.name, states.name
FROM states
INNER JOIN cities
ON state.id = cities.state_id;
