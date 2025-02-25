CREATE USER 'catcar'@'localhost' IDENTIFIED BY 'catcar';
GRANT ALL PRIVILEGES ON catcardb.* TO 'catcar'@'localhost';
CREATE DATABASE catcardb;

USE catcardb;

CREATE TABLE `brand` (
    `brand_seq` INT NOT NULL AUTO_INCREMENT COMMENT 'auto increment',
    `brand_name` VARCHAR(50) NOT NULL,
    `brand_detail` VARCHAR(3000) NULL,
    `brand_country` TINYINT NOT NULL COMMENT '0 - 국산, 1 - 외제',
    PRIMARY KEY (`brand_seq`)
);

CREATE TABLE `model` (
    `model_seq` INT NOT NULL AUTO_INCREMENT COMMENT 'auto increment',
    `model_name` VARCHAR(30) NULL,
    `model_image` VARCHAR(300) NULL,
    `model_price` INT NULL,
    `model_category` VARCHAR(30) NULL,
    `brand_seq` INT NOT NULL COMMENT 'foreign key referencing brand',
    PRIMARY KEY (`model_seq`),
    CONSTRAINT `FK_MODEL_BRAND` FOREIGN KEY (`brand_seq`) REFERENCES `brand` (`brand_seq`) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE `news` (
    `news_seq` INT NOT NULL AUTO_INCREMENT COMMENT 'auto increment',
    `news_title` VARCHAR(50) NOT NULL,
    `news_detail` VARCHAR(3000) NOT NULL,
    `news_url` VARCHAR(255) NOT NULL,
    `model_seq` INT NOT NULL,
    PRIMARY KEY (`news_seq`),
    CONSTRAINT `FK_NEWS_MODEL` FOREIGN KEY (`model_seq`) REFERENCES `model` (`model_seq`) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE `sales` (
    `sales_month` TINYINT NOT NULL COMMENT '1-12',
    `sales_year` YEAR NOT NULL,
    `sales_price_cnt` INT NULL COMMENT '판매 수량',
    `model_seq` INT NOT NULL,
    PRIMARY KEY (`sales_month`, `sales_year`, `model_seq`),
    CONSTRAINT `FK_SALES_MODEL` FOREIGN KEY (`model_seq`) REFERENCES `model` (`model_seq`) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE VIEW total_sales_desc AS
SELECT model_seq,model_name,model_image,model_price,model_category,brand_seq,SUM(sales_price_cnt) AS 'total_sales'
	FROM model
    JOIN sales USING (model_seq)
    GROUP BY model_seq,model_name,model_image,model_price,model_category,brand_seq
    ORDER BY SUM(sales_price_cnt) DESC;