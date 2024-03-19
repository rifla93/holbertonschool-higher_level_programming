-- This script lists all genres and the number of shows linked to each genre
SELECT g.name AS genre, COUNT(s.id) AS number_of_shows
FROM genres AS g
JOIN tv_show_genres AS tsg ON g.id = tsg.genre_id
JOIN tv_shows AS s ON tsg.show_id = s.id
GROUP BY g.name
HAVING COUNT(s.id) > 0
ORDER BY COUNT(s.id) DESC;
