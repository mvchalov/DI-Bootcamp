create table items (
	id serial primary key,
	item_name varchar(200),
	item_price float
);
create table customers (
	id serial primary key,
	first_name varchar(30),
	last_name varchar(50)
);
insert into items (item_name, item_price)
values ('Small Desk', 100),
('Large desk', 300),
('Fan', 80)
insert into customers (first_name, last_name)
values ('Greg', 'Jones'),
('Sandra','Jones'),
('Scott','Scott'),
('Trevor','Green'),
('Melanie','Johnson');

select * from items;
select * from items where item_price > 80;
select * from items where item_price <= 300;
select * from customers where last_name='Smith';
select * from customers where last_name='Jones';
select * from customers where first_name!='Scott';