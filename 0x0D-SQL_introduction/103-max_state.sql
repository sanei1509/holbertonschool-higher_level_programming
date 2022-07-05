-- Importación del mismo archivo temperatures.sql:
-- Mostrar la máxima temperature de cada State
-- Ordenados por "State Name"
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state ASC 
