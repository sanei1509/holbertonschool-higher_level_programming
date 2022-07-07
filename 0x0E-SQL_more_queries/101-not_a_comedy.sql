-- misma database cargada de las anteriores tareas
-- task 18 advanced:
-- listar las peliculas que no tengan comedia como genero
SELECT DISTINCT tv_shows.title AS title
FROM tv_shows
WHERE tv_shows.title NOT IN(
	SELECT title FROM tv_shows
		JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
		JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
		WHERE tv_genres.name = "Comedy")
ORDER BY title ASC;
