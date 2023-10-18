-- To list all cities in the 'hbtn_0d_usa' database, along with their respective states
-- sorted in ascending order by cities.id
USE hbtn_0d_usa;

SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id;
