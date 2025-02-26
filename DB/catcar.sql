CREATE USER 'catcar'@'localhost' IDENTIFIED BY 'catcar';

GRANT ALL PRIVILEGES ON catcardb.* TO catcar@'%';
CREATE DATABASE catcardb;

USE catcardb;

CREATE TABLE `brand` (
    `brand_seq` INT NOT NULL AUTO_INCREMENT COMMENT 'auto increment',
    `brand_name` VARCHAR(50) NOT NULL,
    `brand_detail` VARCHAR(3000) NULL,
    `brand_country` TINYINT(1) NOT NULL COMMENT '0 - 국산, 1 - 외제',
    CONSTRAINT `PK_BRAND` PRIMARY KEY (`brand_seq`)
);

CREATE TABLE `model` (
    `model_seq` INT NOT NULL AUTO_INCREMENT COMMENT 'auto increment',
    `model_name` VARCHAR(30) NULL,
    `model_image` VARCHAR(300) NULL,
    `model_price` INT NULL,
    `model_category` VARCHAR(30) NULL,
    `brand_seq` INT NOT NULL COMMENT 'foreign key reference to brand',
    CONSTRAINT `PK_MODEL` PRIMARY KEY (`model_seq`),
    CONSTRAINT `FK_MODEL_BRAND` FOREIGN KEY (`brand_seq`) REFERENCES `brand` (`brand_seq`) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE `News` (
    `news_seq` INT NOT NULL AUTO_INCREMENT COMMENT 'auto increment',
    `news_title` VARCHAR(50) NOT NULL,
    `news_detail` VARCHAR(3000) NOT NULL,
    `news_url` VARCHAR(255) NOT NULL,
    `model_seq` INT NOT NULL,
    CONSTRAINT `PK_NEWS` PRIMARY KEY (`news_seq`),
    CONSTRAINT `FK_NEWS_MODEL` FOREIGN KEY (`model_seq`) REFERENCES `model` (`model_seq`) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE `sales` (
    `sales_month` INT NOT NULL,
    `sales_price_cnt` INT NULL,
    `model_seq` INT NOT NULL,
    CONSTRAINT `PK_SALES` PRIMARY KEY (`sales_month`, `model_seq`),
    CONSTRAINT `FK_SALES_MODEL` FOREIGN KEY (`model_seq`) REFERENCES `model` (`model_seq`) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE VIEW total_sales_desc AS
SELECT model_seq,model_name,model_image,model_price,model_category,brand_seq,SUM(sales_price_cnt) AS 'total_sales'
	FROM model
    JOIN sales USING (model_seq)
    GROUP BY model_seq,model_name,model_image,model_price,model_category,brand_seq
    ORDER BY SUM(sales_price_cnt) DESC;
