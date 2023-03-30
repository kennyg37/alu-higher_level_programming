-- querie that uses inner join to filter out shows that do not fill the condition
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.tv_show_id) AS number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;
