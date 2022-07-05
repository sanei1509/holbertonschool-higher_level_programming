-- Importar una table en una base de datos, file "temeperatures.sql"
SELECT city, AVG(value) as avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;

