SELECT avg(number_oscars) FROM actors;
SELECT DISTINCT ON (number_oscars) first_name, last_name, number_oscars FROM actors;
SELECT * FROM actors WHERE birthdate > '1970-01-01'
SELECT * FROM actors WHERE first_name='David' OR first_name='Morgan' OR first_name='Reese'

CREATE TABLE movies(
movie_id SERIAL,
movie_title VARCHAR (50) NOT NULL,
movie_story TEXT,
actor_playing_id INTEGER,
PRIMARY KEY (movie_id),
FOREIGN KEY (actor_playing_id) REFERENCES actors (actor_id)
);

INSERT INTO movies (movie_title, movie_story, actor_playing_id) VALUES
    ( 'Good Will Hunting',
    'Written by Affleck and Damon, the film follows 20-year-old South Boston janitor Will Hunting',
    (SELECT actor_id from actors WHERE first_name='Matt' AND last_name='Damon')),
    ( 'Oceans Eleven',
    'American heist film directed by Steven Soderbergh and written by Ted Griffin.',
    (SELECT actor_id from actors WHERE first_name='Matt' AND last_name='Damon'));

SELECT actors.first_name, actors.last_name, movies.movie_title
FROM actors
INNER JOIN movies
ON actors.actor_id = movies.actor_playing_id;

CREATE TABLE producers(
producer_id SERIAL,
first_name VARCHAR (20) NOT NULL,
last_name VARCHAR (20) NOT NULL,
bio TEXT,
movie_producer_id INTEGER,
PRIMARY KEY (producer_id),
FOREIGN KEY (movie_producer_id) REFERENCES movies (movie_id)
);

INSERT INTO producers (first_name, last_name, bio, movie_producer_id) VALUES
    ( 'Su', 'Armstrong',
	 'Su Armstrong is known for Casanova (2005), Good Will Hunting (1997) and Berlin Syndrome (2017). She has been married to Brian Rosen since 3 October 2003.',
    (SELECT movie_id from movies WHERE movie_title='Good Will Hunting')),
    ( 'Bruce', 'Berman',
    'Bruce Berman is Chairman and CEO of Village Roadshow Pictures. The company has a successful joint partnership with Warner Bros. Pictures to co-produce a wide range of motion pictures, with all films distributed worldwide by Warner Bros.Bruce Berman is Chairman and CEO of Village Roadshow Pictures. The company has a successful joint partnership with Warner Bros. Pictures to co-produce a wide range of motion pictures, with all films distributed worldwide by Warner Bros.',
    (SELECT movie_id from movies WHERE movie_title='Oceans Eleven'));

SELECT * FROM producers;

INSERT INTO movies (movie_title, movie_story, actor_playing_id) VALUES
	('The Departed', 'An undercover cop and a mole in the police attempt to identify each other while infiltrating an Irish gang in South Boston.',
	(SELECT actor_id from actors WHERE first_name='Matt' AND last_name='Damon'))

SELECT movies.movie_title, movies.movie_story, producers.first_name, producers.last_name
FROM movies
INNER JOIN producers
ON movies.movie_id = producers.movie_producer_id;

CREATE TABLE countries(
country_id SERIAL,
country_name VARCHAR (20) NOT NULL
);

INSERT INTO countries (country_name) VALUES
	('United States'), ('Germany'), ('France')

SELECT actors.first_name, actors.last_name, countries.country_name
FROM actors
FULL OUTER JOIN countries
ON actors.actor_id = countries.country_id;

SELECT actors.first_name, actors.last_name, countries.country_name
FROM actors
INNER JOIN countries
ON actors.actor_id = countries.country_id;

SELECT actors.first_name, actors.last_name, countries.country_name
FROM actors
LEFT JOIN countries
ON actors.actor_id = countries.country_id;

SELECT actors.first_name, actors.last_name, countries.country_name
FROM actors
RIGHT JOIN countries
ON actors.actor_id = countries.country_id;