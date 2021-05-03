-- public.product definition

-- Drop table

-- DROP TABLE public.product;

CREATE TABLE public.product (
	id int4 NOT NULL,
	"name" varchar(45) NULL,
	cost_price int4 NULL,
	selling_price int4 NULL,
	admin_id int4 NULL,
	product_category int4 NULL,
	is_deleted int4 NULL,
	img_address varchar(100) NULL,
	product_information varchar(200) NULL,
	CONSTRAINT product_pk_id PRIMARY KEY (id)
);


-- public.product_category definition

-- Drop table

-- DROP TABLE public.product_category;

CREATE TABLE public.product_category (
	id int4 NOT NULL,
	"name" varchar(45) NULL,
	CONSTRAINT category_pk_id PRIMARY KEY (id)
);


-- public.product_category_detail definition

-- Drop table

-- DROP TABLE public.product_category_detail;

CREATE TABLE public.product_category_detail (
	id int4 NULL,
	"name" varchar(45) NULL,
	product_category_id int4 NULL
);


-- public."user" definition

-- Drop table

-- DROP TABLE public."user";

CREATE TABLE public."user" (
	id int4 NOT NULL,
	"password" varchar(200) NULL,
	"name" varchar(45) NULL,
	phone_number varchar(20) NULL,
	status varchar(10) NULL,
	email varchar(45) NULL,
	"role" varchar(10) NULL,
	is_deleted int4 NULL
);