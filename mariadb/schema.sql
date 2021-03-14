create database if not exists furnitures;
use furnitures;

create table if not exists channels (
	id int auto_increment,
	name varchar(80) unique not null,
	primary key (id)
);

create table if not exists nodes (
	id int auto_increment,
	name varchar(80) unique not null,
	primary key (id)
);

create table if not exists channels_nodes (
	channel_id int,
	node_id int,
	foreign key (channel_id) references channels(id),
	foreign key (node_id) references nodes(id)
);

create table if not exists products (
	id int auto_increment,
	name varchar(80) unique not null,
	image varchar(80) default "default.jpg",
	node_id int,
	primary key (id),
	foreign key (node_id) references nodes(id)
);

create table if not exists skus (
	id int auto_increment,
	name varchar(80) unique not null,
	quantity int not null,
	price float not null,
	promotion float default 1,
	image varchar(80) default "default.jpg",
	product_id int,
	primary key (id),
	foreign key (product_id) references products(id)
);
