-- Listar los registros descending score and descending names
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
