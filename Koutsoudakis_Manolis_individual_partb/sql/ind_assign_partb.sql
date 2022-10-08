create database if not exists ind_proj_partb;
use  ind_proj_partb;

create table if not exists students(
       stid int auto_increment,
       firstName varchar (45),
       lastName varchar (45),
       dateOfBirth date,
       tuitionFees float,
       primary key (stid)
);

create table if not exists courses(
       cid int auto_increment,
       title varchar (45),
       stream1 varchar (45),
       type1 varchar (45),
       start_date date,
       end_date date,
       primary key (cid)
);

create table if not exists trainers(
	   trid int auto_increment,
       firstName varchar (45),
       lastName varchar (45),
       subject1 varchar (45),
       primary key (trid)
);

create table if not exists assignments(
	   asid int auto_increment,
       title varchar (45),
       description1 varchar(45),
       subDateTime date,
       oralMark float,
       totalMark float,
       primary key (asid)
);

create table if not exists student_per_course(
       st_per_c_id int auto_increment,
       stid int not null,
       cid int not null,
       primary key (st_per_c_id),
       foreign key (stid) references students (stid),
       foreign key (cid) references courses (cid)
);

create table if not exists trainer_per_course(
       tr_per_c_id int auto_increment,
       trid int not null,
       cid int not null,
       primary key (tr_per_c_id),
       foreign key (trid) references trainers (trid),
       foreign key (cid) references courses (cid)
);

create table if not exists assignment_per_course(
       as_per_c_id int auto_increment,
       asid int not null,
       cid int not null,
       primary key (as_per_c_id),
       foreign key (asid) references assignments (asid),
       foreign key (cid) references courses (cid)
);

create table if not exists assignment_per_student_per_course(
       as_per_st_per_c_id int auto_increment,
       asid int not null,
       stid int not null,
       cid int not null,
       primary key (as_per_st_per_c_id),
       foreign key (asid) references assignments (asid),
       foreign key (stid) references students (stid),
       foreign key (cid) references courses (cid)
);
-- insert dummy data to the tables
insert into students (firstName, lastName, dateOfBirth, tuitionFees)  values ("Manolis", "Koutsoudakis","1985-06-10", "2500");
insert into students (firstName, lastName, dateOfBirth, tuitionFees) values ("Stratos", "Kontelos","1985-08-11", "2500");
insert into students (firstName, lastName, dateOfBirth, tuitionFees) values ("Bruna", "Doga","1985-07-01", "2500");
insert into students (firstName, lastName, dateOfBirth, tuitionFees) values ("Efi", "Likoudi","1985-02-10", "2500");
insert into students (firstName, lastName, dateOfBirth, tuitionFees) values ("Olga", "Giftaki","1985-08-01", "2500");

insert into courses (title, stream1, type1, start_date, end_date) values ("Coding Bootcamp 1", "java", "Full Time", "2021-10-10", "2022-10-10");
insert into courses (title, stream1, type1, start_date, end_date) values ("Coding Bootcamp 2", "python", "Part Time", "2021-10-10", "2022-10-10");
insert into courses (title, stream1, type1, start_date, end_date) values ("Coding Bootcamp 3", "c++", "Full Time", "2021-10-10", "2022-10-10");
insert into courses (title, stream1, type1, start_date, end_date) values ("Coding Bootcamp 4", "sql", "Part Time", "2021-10-10", "2022-10-10");
insert into courses (title, stream1, type1, start_date, end_date) values ("Coding Bootcamp 5", "python", "Full Time", "2021-10-10", "2022-10-10");

insert into trainers (firstName, lastName, subject1) values ("Stefanos", "Papadopoulos", "python");
insert into trainers (firstName, lastName, subject1) values ("Ilias", "Mantalos", "java");
insert into trainers (firstName, lastName, subject1) values ("Georgia", "Paraskeuopoulou", "c++, java");
insert into trainers (firstName, lastName, subject1) values ("Nikolaos", "Kamitsos", "sql");
insert into trainers (firstName, lastName, subject1) values ("Antonis", "Karavas", "javascript");

insert into assignments (title, description1, subDateTime, oralMark, totalMark) values ("Evaluation","Evaluation","2021-10-10", "10","10");
insert into assignments (title, description1, subDateTime, oralMark, totalMark) values ("Total Cost","Total Cost","2021-10-10", "8","8");
insert into assignments (title, description1, subDateTime, oralMark, totalMark) values ("Total Loss","Total Loss","2021-10-10", "7","7");
insert into assignments (title, description1, subDateTime, oralMark, totalMark) values ("Balance","Balance","2021-10-10", "9","9");
insert into assignments (title, description1, subDateTime, oralMark, totalMark) values ("Costs","Costs","2021-10-10", "8","8");

insert into student_per_course (stid, cid) values ( 1, 1);
insert into student_per_course (stid, cid) values ( 2, 2);
insert into student_per_course (stid, cid) values ( 1, 3);
insert into student_per_course (stid, cid) values ( 2, 3);
insert into student_per_course (stid, cid) values ( 3, 5);

insert into trainer_per_course (trid, cid) values ( 1, 1);
insert into trainer_per_course (trid, cid) values ( 2, 2);
insert into trainer_per_course (trid, cid) values ( 3, 4);
insert into trainer_per_course (trid, cid) values ( 4, 3);
insert into trainer_per_course (trid, cid) values ( 4, 5);

insert into assignment_per_course (asid, cid) values ( 2, 3);
insert into assignment_per_course (asid, cid) values ( 1, 3);
insert into assignment_per_course (asid, cid) values ( 3, 1);
insert into assignment_per_course (asid, cid) values ( 4, 1);
insert into assignment_per_course (asid, cid) values ( 2, 5);

insert into assignment_per_student_per_course (asid, stid, cid) values ( 2, 3, 3);
insert into assignment_per_student_per_course (asid, stid, cid) values ( 1, 2, 1);
insert into assignment_per_student_per_course (asid, stid, cid) values ( 3, 3, 4);
insert into assignment_per_student_per_course (asid, stid, cid) values ( 1, 1, 1);
insert into assignment_per_student_per_course (asid, stid, cid) values ( 2, 4, 5);

-- select all from tables
select * from students;
select * from trainers;
select * from assignments;
select * from courses;

-- a list of students per course
select  student_per_course.st_per_c_id, students.firstName,students.lastName, courses.title
from students
inner join student_per_course on student_per_course.stid = students.stid
inner join courses on courses.cid= student_per_course.cid
order by student_per_course.st_per_c_id, students.firstName,students.lastName, courses.title;

-- a list of trainers per course
select trainer_per_course.tr_per_c_id, trainers.firstName,trainers.lastName, courses.title
from trainers
inner join trainer_per_course on trainer_per_course.trid = trainers.trid
inner join courses on courses.cid= trainer_per_course.cid
order by trainer_per_course.tr_per_c_id, trainers.firstName,trainers.lastName, courses.title;

-- a list of assignments per course
select assignment_per_course.as_per_c_id, assignments.title, courses.title
from assignments
inner join assignment_per_course on assignment_per_course.asid = assignments.asid
inner join courses on courses.cid= assignment_per_course.cid
order by assignment_per_course.as_per_c_id, assignments.title, courses.title;

-- a list of assignments per student per course
select  assignment_per_student_per_course.as_per_st_per_c_id, assignments.title, courses.title, students.firstName, students.lastName
from assignments
inner join assignment_per_student_per_course on assignment_per_student_per_course.asid = assignments.asid
inner join courses on courses.cid= assignment_per_student_per_course.cid
inner join students on students.stid = assignment_per_student_per_course.stid
order by  assignment_per_student_per_course.as_per_st_per_c_id, assignments.title, courses.title, students.firstName, students.lastName;

-- a list of students that belong in more than one courses
select students.firstName, students.lastName, courses.title
from student_per_course
inner join students on students.stid =student_per_course.stid
inner join courses on courses.cid= student_per_course.cid
where student_per_course.stid in ( select stid from student_per_course group by stid having count(*)>1);






