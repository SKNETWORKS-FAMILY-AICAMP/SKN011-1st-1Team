-- brand 데이터
INSERT INTO `brand` (`brand_name`, `brand_detail`, `brand_country`) VALUES
('Samsung Electronics', 'Global leader in consumer electronics and technology. Known for its high-end smartphones and televisions.', 0),
('Apple Inc.', 'Innovative technology company known for its smartphones, tablets, and personal computers. The creator of iPhone and MacBook.', 1),
('LG Electronics', 'A multinational company specializing in consumer electronics, home appliances, and mobile communication products.', 0),
('Sony Corporation', 'A major player in consumer electronics, gaming, and entertainment, best known for PlayStation and high-quality audio products.', 1),
('Huawei Technologies', 'Chinese multinational tech company specializing in telecommunications equipment and consumer electronics, including smartphones and tablets.', 1);

-- model 데이터
INSERT INTO `model` (`model_name`, `model_image`, `model_price`, `model_category`, `brand_seq`) VALUES
('Galaxy S23 Ultra', 'galaxy_s23_ultra.jpg', 1450000, 'Smartphone', 1),
('iPhone 14 Pro', 'iphone_14_pro.jpg', 1399000, 'Smartphone', 2),
('LG OLED55C1', 'lg_oled55c1.jpg', 1500000, 'Television', 3),
('PlayStation 5', 'ps5.jpg', 550000, 'Gaming Console', 4),
('P40 Pro', 'huawei_p40_pro.jpg', 1100000, 'Smartphone', 5),
('Galaxy Watch 5', 'galaxy_watch_5.jpg', 350000, 'Wearable', 1),
('iPad Pro 12.9', 'ipad_pro_12.9.jpg', 1200000, 'Tablet', 2),
('LG Gram 17', 'lg_gram_17.jpg', 1900000, 'Laptop', 3),
('Sony WH-1000XM5', 'sony_wh_1000xm5.jpg', 450000, 'Headphones', 4),
('MateBook X Pro', 'matebook_x_pro.jpg', 1600000, 'Laptop', 5);


-- News 데이터
INSERT INTO `news` (`news_title`, `news_detail`, `news_url`, `model_seq`) VALUES
('Galaxy S23 Ultra Launched', 'Samsung has just released the Galaxy S23 Ultra, boasting incredible performance and camera capabilities.', 'http://example.com/galaxy_s23_ultra', 1),
('iPhone 14 Pro Review', 'Apple\'s iPhone 14 Pro comes with stunning display and upgraded features, making it the most advanced iPhone yet.', 'http://example.com/iphone_14_pro', 2),
('LG OLED55C1 Gets Rave Reviews', 'The LG OLED55C1 is receiving exceptional feedback for its picture quality and sleek design.', 'http://example.com/lg_oled55c1', 3),
('PlayStation 5 Supply Shortage', 'Despite high demand, the PlayStation 5 continues to face supply chain issues globally.', 'http://example.com/ps5_supply', 4),
('Huawei P40 Pro Camera Excellence', 'The Huawei P40 Pro is renowned for its photography capabilities, especially in low-light conditions.', 'http://example.com/huawei_p40_pro', 5),
('New Galaxy Watch 5 Features Revealed', 'Samsung Galaxy Watch 5 brings a host of new health monitoring features and a refined design.', 'http://example.com/galaxy_watch_5', 6),
('iPad Pro 12.9 vs Surface Pro 9', 'Apple iPad Pro 12.9 is compared to Microsoft\'s Surface Pro 9 in a battle for the best productivity tablet.', 'http://example.com/ipad_pro_12_9', 7),
('LG Gram 17: The Lightweight Powerhouse', 'The LG Gram 17 combines a lightweight design with powerful specs, perfect for professionals on the go.', 'http://example.com/lg_gram_17', 8),
('Sony WH-1000XM5: Best Noise Cancelling Headphones', 'Sony\'s WH-1000XM5 headphones are hailed as the best for noise cancellation and sound quality.', 'http://example.com/sony_wh_1000xm5', 9),
('MateBook X Pro: A Laptop for Professionals', 'Huawei\'s MateBook X Pro is being praised for its sleek design, performance, and high-resolution display.', 'http://example.com/matebook_x_pro', 10);


-- sales 데이터
INSERT INTO `sales` (`sales_month`, `sales_year`, `sales_price_cnt`, `model_seq`) VALUES
(1, 2024, 50000, 1),
(2, 2024, 45000, 1),
(1, 2024, 60000, 2),
(2, 2024, 55000, 2),
(1, 2024, 70000, 3),
(2, 2024, 65000, 3),
(1, 2024, 35000, 4),
(2, 2024, 30000, 4),
(1, 2024, 65000, 5),
(2, 2024, 60000, 5),
(1, 2024, 20000, 6),
(2, 2024, 18000, 6),
(1, 2024, 55000, 7),
(2, 2024, 50000, 7),
(1, 2024, 40000, 8),
(2, 2024, 35000, 8),
(1, 2024, 75000, 9),
(2, 2024, 70000, 9),
(1, 2024, 45000, 10),
(2, 2024, 40000, 10);
