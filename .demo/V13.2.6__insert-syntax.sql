create database insert_syntax;

create table insert_syntax_demo (
  id int unsigned not null primary key auto_increment,
  user_name varchar(255) not null,
  sex tinyint not null default 0,

  unique key `UK_insert_syntax_demo_user_name` (`user_name`(32) asc)
) engine=InnoDB;

