-- DB명은 carcatdb

USE carcatdb

CREATE TABLE `model` (
	`model_seq`	int	NOT NULL	COMMENT 'auto incresement',
	`model_name`	varchar(30)	NULL,
	`model_image`	varchar(300)	NULL,
	`model_price`	int	NULL,
	`model_category`	varchar(30)	NULL,
	`brand_seq`	int	NOT NULL	COMMENT 'auto incresement'
);

CREATE TABLE `brand` (
	`brand_seq`	int	NOT NULL	COMMENT 'auto incresement',
	`brand_name`	varchar(50)	NOT NULL,
	`brand_detail`	varchar(3000)	NULL,
	`brand_country`	tinyint	NOT NULL	COMMENT '0 - 국산, 1 - 외제'
);

CREATE TABLE `News` (
	`news_seq`	int	NOT NULL	COMMENT 'auto_incresement',
	`news_title`	varchar(50)	NOT NULL,
	`news_detail`	varchar(3000)	NOT NULL,
	`news_url`	varchar(255)	NOT NULL,
	`model_seq`	int	NOT NULL
);

CREATE TABLE `sales` (
	`sales_month`	int	NOT NULL,
	`sales_price_cnt`	int	NULL,
	`model_seq`	int	NOT NULL
);

ALTER TABLE `model` ADD CONSTRAINT `PK_MODEL` PRIMARY KEY (
	`model_seq`
);

ALTER TABLE `brand` ADD CONSTRAINT `PK_BRAND` PRIMARY KEY (
	`brand_seq`
);

ALTER TABLE `News` ADD CONSTRAINT `PK_NEWS` PRIMARY KEY (
	`news_seq`
);

