-- Importar lo mismo que en los anteriores adentro de la base de datos
-- FILTRAR SOLO LOS QUE TENGAN VALOR NULL 
-- Juntar titulo con id del genero.
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id;
