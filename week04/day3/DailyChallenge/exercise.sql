-- PART 1

-- create table customer (
-- 	id serial primary key, 
-- 	first_name varchar(30), 
-- 	last_name varchar(30) NOT NULL
-- );

-- create table customer_profile (
-- 	id serial primary key,
-- 	isLoggedIn bool DEFAULT false, 
-- 	customer_id int references customer(id)
-- );

-- insert into customer (first_name, last_name) values
-- ('John', 'Doe'),
-- ('Jerome', 'Lalu'),
-- ('Lea', 'Rive');

-- insert into customer_profile (isLoggedIn, customer_id) values
-- (true, (select id from customer where first_name='John')),
-- (false, (select id from customer where first_name='Jerome'));

-- select first_name from customer
-- join customer_profile
-- on customer.id = customer_profile.customer_id
-- where customer_profile.isLoggedIn;

-- select customer.first_name, customer_profile.isLoggedIn from customer
-- left outer join customer_profile
-- on customer.id=customer_profile.customer_id;

-- select first_name, last_name from customer
-- where id = (select customer_id from customer_profile where not isLoggedIn);

-- PART 2

-- create table book (
-- 	book_id SERIAL PRIMARY KEY, 
-- 	title varchar(200) NOT NULL, 
-- 	author varchar(100) NOT NULL
-- );

-- insert into book (title, author) values
-- ('Alice In Wonderland', 'Lewis Carroll'),
-- ('Harry Potter', 'J.K Rowling'),
-- ('To kill a mockingbird', 'Harper Lee');

-- create table student (
-- 	student_id SERIAL PRIMARY KEY, 
-- 	name varchar(100) NOT NULL UNIQUE, 
-- 	age smallint check (age < 16)
-- );

-- insert into student (name, age) values
-- ('John', 12),
-- ('Lera', 11),
-- ('Patrick', 10),
-- ('Bob', 14);

-- create table library (
-- 	book_fk_id int references book(book_id) on delete cascade on update cascade,
-- 	student_fk_id int references student(student_id) on delete cascade on update cascade,
-- 	borrowed_date date
-- );

-- insert into library (borrowed_date, book_fk_id, student_fk_id) values
-- ('2022-02-15', (select book_id from book where title='Alice In Wonderland'), (select student_id from student where name='John')),
-- ('2021-03-03', (select book_id from book where title='To kill a mockingbird'), (select student_id from student where name='Bob')),
-- ('2021-05-23', (select book_id from book where title='Alice In Wonderland'), (select student_id from student where name='Lera')),
-- ('2021-08-12', (select book_id from book where title='Harry Potter'), (select student_id from student where name='Bob'))

-- select * from library
-- join book on library.book_fk_id=book.book_id
-- join student on library.student_fk_id=student.student_id

-- select student.name, book.title from library
-- join book on library.book_fk_id=book.book_id
-- join student on library.student_fk_id=student.student_id

-- select avg(student.age) from library
-- join book on library.book_fk_id=book.book_id
-- join student on library.student_fk_id=student.student_id
-- where book.title='Alice In Wonderland'

-- delete from student 
-- where name='Lera'

-- cascade works