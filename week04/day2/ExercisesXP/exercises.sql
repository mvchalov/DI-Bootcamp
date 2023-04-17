SELECT * FROM customer
SELECT (first_name, last_name) AS full_name FROM customer
SELECT DISTINCT create_date FROM customer
SELECT * FROM customer
ORDER BY first_name DESC
SELECT film_id, title, description, release_year, rental_rate FROM film
ORDER BY rental_rate ASC
SELECT address, phone from address
WHERE district='Texas'
SELECT * FROM film
WHERE film_id=15 OR film_id=150
SELECT film_id, title, description, length, rental_rate FROM film
WHERE title='The Departed'
SELECT film_id, title, description, length, rental_rate FROM film
WHERE lower(title) ~~ 'th%';
SELECT * FROM film
ORDER BY replacement_cost ASC
LIMIT 10;
SELECT * FROM film
ORDER BY replacement_cost, title ASC
OFFSET 10
FETCH NEXT 10 ROWS ONLY;
SELECT * FROM payment
SELECT customer.first_name, customer.last_name, payment.amount, payment.payment_date
FROM customer INNER JOIN payment
ON payment.customer_id = customer.customer_id
ORDER BY payment.payment_id
SELECT * FROM film
LEFT JOIN inventory
ON film.film_id = inventory.film_id
WHERE inventory.film_id IS NULL;
SELECT city.city, country.country
FROM city INNER JOIN country
ON city.country_id=country.country_id
SELECT customer.customer_id, customer.first_name, customer.last_name, 
payment.amount, payment.payment_date
FROM customer INNER JOIN payment
ON customer.customer_id=payment.customer_id
ORDER BY payment.staff_id
