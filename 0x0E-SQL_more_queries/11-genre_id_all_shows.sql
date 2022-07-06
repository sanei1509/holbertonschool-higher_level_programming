-- Importar desde el link hacia la base de datos
-- Mostrar 
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_shows_genres.show_id
ORDER BY tv_show.title, tv_show_genres.genre_id;
