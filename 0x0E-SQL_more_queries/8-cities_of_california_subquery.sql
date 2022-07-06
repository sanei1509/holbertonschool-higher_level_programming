-- Listar todas las ciudades de California que se puedan encontrar en 'htbtn_0d_usa'
-- Realizar una subconsulta, traer las tablas que tienen 2 cosas iguales
SELECT id, name FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California');
