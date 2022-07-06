-- Importar desde el link hacia la base de datos
-- Mostrar todos los datos de la tabla izquierda aunque no tenga valor la segunda
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_shows_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
