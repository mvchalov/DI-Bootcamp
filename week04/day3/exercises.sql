-- noinspection SqlDialectInspectionForFile

-- create table items (
-- id serial primary key,
-- name varchar(50) not null unique, 
-- price int not null
-- );

-- create table product_orders (
-- id serial primary key, 
-- quantity int not null, 
-- "date" timestamp not null default CURRENT_TIMESTAMP,
-- product_id int references items(id) on delete no action
-- ); 

-- insert into items (name, price)
-- values
-- ('TV', 50),
-- ('Radio', 44),
-- ('Laptop', 1000);

-- insert into product_orders(quantity, product_id)
-- values
-- (1, (select id from items where name = 'TV')),
-- (5, (select id from items where name = 'Radio')),
-- (2, (select id from items where name = 'Laptop'))

-- select name, quantity*price from product_orders
-- join items
-- on product_orders.product_id = items.id;

-- create or replace function whole_price (order_id int)
-- returns int as $cost$
-- 	declare
-- 		total_s int;
-- 	begin
-- 		total_s := (select sum(quantity*price) from product_orders
-- 		join items
-- 		on product_orders.product_id = items.id);
-- 		return total_s;
-- 	end;

-- $cost$ language plpgsql;

-- select * from whole_price(1)

