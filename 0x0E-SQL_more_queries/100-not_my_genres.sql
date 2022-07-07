-- misma base de datos cargada de tareas anteriores
-- Listar todos los generos no vinculados a "Dexter"
SELECT tv_genres.name AS name
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
WHERE name NOT IN(
	SELECT FROM tv_genres
	JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
	JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
	WHERE tv_shows.title = "Dexter"
);
ORDER BY tv_genres.name ASC;