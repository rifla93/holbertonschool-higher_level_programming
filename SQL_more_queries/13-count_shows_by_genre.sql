-- This script lists all genres from the tv_shows table 
SELECT genre AS genre, COUNT(*) AS number_of_shows
FROM tv_shows
WHERE genre IS NOT NULL
GROUP BY genre
HAVING COUNT(*) > 0
ORDER BY COUNT(*) DESC;