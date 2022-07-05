-- Con la misma importación de archivo :
-- Mostrar 3 ciudades durante julio y agosto ordenadas por temperatura
-- temperatures es el nombre de nuestra tabla en temperatures.sql
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month=7 or month=8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
