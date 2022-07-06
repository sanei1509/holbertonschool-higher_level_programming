-- Listar todas las ciudades que contienen 'hbtn_0d_usa'
-- Pudiendo usar JOIN
SELECT cities.id, cities.name ,states.name FROM cities JOIN states WHERE states.id = cities.state_id
ORDER BY cities.id ASC
