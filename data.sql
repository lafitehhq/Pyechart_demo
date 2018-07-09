create table Nation_Demo (
  id           int(8) not null primary key auto_increment,
  nation_name  nvarchar(20),
  nation_quant int
)

insert into Nation_Demo values (null,'中国',1500);
insert into Nation_Demo values (null,'美国',2500);
insert into Nation_Demo values (null,'英国',1200);
insert into Nation_Demo values (null,'俄罗斯',900);
insert into Nation_Demo values (null,'日本',2100);
insert into Nation_Demo values (null,'越南',500);