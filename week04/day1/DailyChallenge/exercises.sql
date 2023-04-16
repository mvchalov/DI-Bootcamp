-- Before DailyChallenge:

CREATE TABLE actors(
 actor_id SERIAL PRIMARY KEY,
 first_name VARCHAR (50) NOT NULL,
 last_name VARCHAR (100) NOT NULL,
 age DATE NOT NULL,
 number_oscars SMALLINT NOT NULL
);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('Matt','Damon','08/10/1970', 5);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('George','Clooney','06/05/1961', 2);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('Mila','Kunis','08/14/1983', 0);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('Reese','Witherspoon','03/22/1976', 1);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES ('Charlize', 'Theron', '1975-08-07', 1),
('Nicole', 'Kidman', '1967-06-20', 1),
('Meryl', 'Streep', '1949-06-22', 3);

SELECT * FROM actors;

SELECT * FROM actors WHERE actor_id < 5;

SELECT * FROM actors WHERE actor_id < 5 ORDER BY last_name DESC;

SELECT * FROM actors WHERE last_name ~~* '%e%';

SELECT * FROM actors WHERE number_oscars > 4;

UPDATE actors SET first_name='Maty' WHERE first_name='Matt' AND last_name='Damon';

UPDATE actors SET number_oscars=4 WHERE first_name='George' AND last_name='Clooney'
RETURNING actor_id, first_name, last_name, number_oscars;

DELETE FROM actors
WHERE number_oscars=0
RETURNING actor_id, first_name, last_name, number_oscars;

ALTER TABLE actors RENAME COLUMN age TO birthdate;

-- Daily Challenge : Actors:

SELECT COUNT(*) FROM actors;

ALTER TABLE actors ALTER COLUMN birthdate DROP NOT NULL;

INSERT INTO actors (first_name, last_name, birthdate, number_oscars)
VALUES('Mila','Kunis', NULL, 0);
