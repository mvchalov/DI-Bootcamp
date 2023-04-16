create table students (
	id serial primary key,
	last_name varchar(20),
	first_name varchar(20),
	birth_date date
);

insert into students (first_name, last_name, birth_date)
values ('Marc','Benichou','1998-11-02'),
('Yoan','Cohen','2010-12-03'),
('Lea','Benichou','1987-07-27'),
('Amelia','Dux','1996-04-07'),
('David','Grez','2003-06-14'),
('Omer','Simpson','1980-10-03');

insert into students (first_name, last_name, birth_date)
values ('Maksim', 'Chalov', '1980-11-09');

select * from students;

select first_name, last_name from students;
select * from students where first_name='Marc' and last_name='Benichou';
select * from students where first_name='Marc' or last_name='Benichou';
select * from students where lower(first_name) like '%a%';
select * from students where lower(first_name) ~~ 'a%';
select * from students where first_name ~~* '%a';
select * from students where first_name ilike '%a_';
select * from students where id=1 or id=3;
select * from students where birth_date >= '2000-01-01';
