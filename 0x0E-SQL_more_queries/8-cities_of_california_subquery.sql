-- Listar todas las ciudades de California que se puedan encontrar en 'htbtn_0d_usa'
SELECT name, id FROM cities 
WHERE state_id = 
(
	SELECT id
	FROM states 
	WHERE name = 'California'
) GROUP BY id ORDER BY id;

