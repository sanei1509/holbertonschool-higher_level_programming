-- Debemos importar desde hbtn_0d_tvshows
-- Listar todos todos los shows contenidos en 'hbtn_0d_tvshows' 
-- que tienen al menos un genero en común.
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows 
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
