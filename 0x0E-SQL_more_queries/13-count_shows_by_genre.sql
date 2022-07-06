-- Misma importación que los anteriores
-- Listar generos con con el número de vistas de cada uno
-- Solo los titulos que tengan alguna vista
SELECT tv_genres.name AS genre, count(tv_show_genres.show_id) AS number_of_shows FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id 
GROUP BY genre ORDER BY number_of_shows DESC;
