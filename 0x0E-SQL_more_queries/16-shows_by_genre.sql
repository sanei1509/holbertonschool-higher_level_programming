-- Listar todas los titulos con su respectivo genero
-- table 1 -> title   table 2 -> name
SELECT tv_shows.title AS title, tv_genres.name AS name FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id ORDER BY title, name;
