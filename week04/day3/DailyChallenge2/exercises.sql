-- create table product_orders(
-- 	order_id serial primary key,
-- 	order_sum int default 0,
-- 	order_date date
-- );

-- create table items(
-- 	item_id serial primary key,
-- 	item_title varchar(30) not null,
-- 	item_price smallint default 0,
-- 	order_fk_id int references product_orders(order_id)
-- );

-- insert into product_orders (order_date) values
-- (now()), (now());

-- insert into items (item_title, item_price, order_fk_id) values
-- ('Laptop', 3000, (select order_id from product_orders where order_id=1)),
-- ('Smartphone', 1500, (select order_id from product_orders where order_id=2)),
-- ('Watch', 300, (select order_id from product_orders where order_id=2)),
-- ('Headphones', 500, (select order_id from product_orders where order_id=1));

-- create function calculate_sum_on_update(the_order_id int)
-- returns void as $$
-- begin
-- 	update product_orders set order_sum = (select sum(item_price) from items where order_fk_id=the_order_id)
-- 	where order_id=the_order_id;
-- end;
-- $$ language plpgsql;

-- select calculate_sum_on_update(order_id), order_sum from product_orders;

-- select * from product_orders
-- join items
-- on order_id=order_fk_id;

-- Bonus

-- create table users (
-- 	user_id serial primary key,
-- 	user_name varchar(30)
-- );

-- alter table product_orders 
-- add column user_fk_id int references users(user_id)

-- insert into users (user_name) values ('Cthulhu');
-- update product_orders set user_fk_id = (select user_id from users where user_id=1)

-- Total price of all orders:
-- create function calculate_total(the_user_id int)
-- returns int as $$
-- begin
-- 	return (select sum(order_sum) from product_orders where user_fk_id=the_user_id);
-- end;
-- $$ language plpgsql;

-- select calculate_total(1);