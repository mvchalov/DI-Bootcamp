-- Exercise 1: DVD Rental
-- select * from language;

-- select title, description, language.name from film
-- join language
-- on film.language_id = language.language_id;

-- create table new_film (
-- 	id serial primary key, 
-- 	name varchar(50) not null unique
-- );

-- insert into new_film(name) values
-- ('Babylon'), ('Luck'), ('Blonde')

-- create table customer_review (
-- 	review_id serial primary key,
-- 	film_id int references new_film(id) on delete cascade,
-- 	language_id int references language(language_id) on delete no action,
-- 	title text,
-- 	score smallint,
-- 	review_text text,
-- 	last_update date
-- );

-- insert into customer_review (film_id, language_id, title, review_text) values
-- (2, 1, 'The best review', 'Lorem Ipsum'),
-- (1, 1, 'The other best review', 'Ipsum Ipsum Lorem Lorem')

-- delete from new_film where id=1


-- Exercise 2 : DVD Rental
-- update film
-- set language_id = 2 where film_id=1

-- drop table customer_review

-- select rental_date, (select title from film where film_id=(select film_id from inventory where inventory_id=rental.inventory_id)) 
-- from rental where return_date > current_date

-- select rental_date, (select title from film where film_id=(select film_id from inventory where inventory_id=rental.inventory_id)), (select replacement_cost from film where film_id=(select film_id from inventory where inventory_id=rental.inventory_id)) 
-- from rental where return_date > current_date
-- order by (select replacement_cost from film where film_id=(select film_id from inventory where inventory_id=rental.inventory_id)) desc
-- limit 30

-- select title from film
-- where film_id in
-- (select film_id from film_actor where actor_id=(select actor_id from actor where first_name='Penelope' and last_name='Monroe')) 
-- and description ~~* '%sumo%wrestler%'

-- select title, length, description from film
-- where length < 60 and rating='R' and description ~~* '%documentary%'

-- select title
-- from film
-- inner join inventory
-- on inventory.film_id = film.film_id
-- inner join rental
-- on rental.inventory_id = inventory.inventory_id
-- inner join customer
-- on customer.customer_id = rental.customer_id
-- where first_name ~~* 'Matthew' and last_name ~~* 'Mahan' and 
-- '2005-07-28' <= return_date and return_date <= '2005-08-01'
-- and rental_rate > 4

select title
from film
inner join inventory
on inventory.film_id = film.film_id
inner join rental
on rental.inventory_id = inventory.inventory_id
inner join customer
on customer.customer_id = rental.customer_id
where first_name ~~* 'Matthew' and last_name ~~* 'Mahan' 
and (title ~~* '%boat%' or description ~~* '%boat%')
order by replacement_cost desc
limit 1