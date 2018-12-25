-- 准备表和数据
create table insert_syntax_demo (
  id int unsigned not null primary key auto_increment,
  user_name varchar(255) not null,
  sex tinyint not null default 0,
  age int unsigned not null,
  bornTime datetime not null default now(),
  deadTime datetime null, 

  unique key `UK_insert_syntax_demo_user_name` (`user_name`(32) asc)
) engine=InnoDB;

create table insert_syntax_tmp (
  user_name varchar(255) not null,
  sex tinyint not null default 0,
  age int unsigned not null 
) engine=InnoDB;

-- insert的使用

insert into insert_syntax_demo
values
(1, 'test', 0, 12, now(), null);



insert into insert_syntax_demo
values
(2, 'test', 0, 12, now(), null)
on duplicate key update 
age=23, deadTime=now();

-- 列名和列值都为空