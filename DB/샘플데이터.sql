-- brand 데이터 삽입
INSERT INTO `brand` (`brand_name`, `brand_detail`, `brand_country`) VALUES
('Samsung', '한국의 대표적인 전자 브랜드', 0),
('Apple', '미국의 글로벌 테크 기업', 1),
('Sony', '일본의 전자 및 엔터테인먼트 기업', 1),
('LG', '한국의 전자 및 가전제품 제조업체', 0),
('Huawei', '중국의 글로벌 통신 및 전자 기업', 1);

-- model 데이터 삽입 (각 브랜드별 2개씩)
INSERT INTO `model` (`model_name`, `model_image`, `model_price`, `model_category`, `brand_seq`) VALUES
('Galaxy S24', 's24.jpg', 1200000, 'Smartphone', 1),
('Galaxy Z Flip5', 'zflip5.jpg', 1400000, 'Smartphone', 1),
('iPhone 15', 'iphone15.jpg', 1500000, 'Smartphone', 2),
('MacBook Air M3', 'macbook_air_m3.jpg', 1800000, 'Laptop', 2),
('PlayStation 5', 'ps5.jpg', 700000, 'Gaming Console', 3),
('Sony Alpha 7', 'alpha7.jpg', 2500000, 'Camera', 3),
('LG OLED TV', 'lg_oled.jpg', 2200000, 'TV', 4),
('LG Gram 16', 'lg_gram.jpg', 1700000, 'Laptop', 4),
('Huawei Mate 60', 'mate60.jpg', 1300000, 'Smartphone', 5),
('Huawei P50', 'p50.jpg', 1100000, 'Smartphone', 5);

-- News 데이터 삽입 (각 model 별 1개씩)
INSERT INTO `News` (`news_title`, `news_detail`, `news_url`, `model_seq`) VALUES
('Galaxy S24 출시', '삼성전자가 최신 스마트폰 Galaxy S24를 출시했습니다.', 'https://news.com/galaxy_s24', 1),
('Galaxy Z Flip5 인기', '접이식 스마트폰 시장에서 Galaxy Z Flip5가 돌풍을 일으키고 있습니다.', 'https://news.com/zflip5', 2),
('iPhone 15 리뷰', 'iPhone 15가 뛰어난 성능과 디자인으로 주목받고 있습니다.', 'https://news.com/iphone15', 3),
('MacBook Air M3 발표', '애플이 새로운 MacBook Air M3을 공개했습니다.', 'https://news.com/macbook_m3', 4),
('PS5 재입고', '소니가 PlayStation 5의 공급을 확대하고 있습니다.', 'https://news.com/ps5', 5),
('Sony Alpha 7 신제품', '소니가 Alpha 7 시리즈의 신제품을 발표했습니다.', 'https://news.com/alpha7', 6),
('LG OLED TV 출시', 'LG가 최신 OLED TV를 선보였습니다.', 'https://news.com/lg_oled', 7),
('LG Gram 16 경량 노트북', 'LG의 Gram 16이 초경량 노트북 시장에서 주목받고 있습니다.', 'https://news.com/lg_gram', 8),
('Huawei Mate 60 공개', '화웨이가 Mate 60을 정식 출시했습니다.', 'https://news.com/mate60', 9),
('Huawei P50 인기 상승', 'Huawei P50의 판매량이 급증하고 있습니다.', 'https://news.com/p50', 10);

-- sales 데이터 삽입 (각 model 당 2개씩, 202401 ~ 202402)
INSERT INTO `sales` (`sales_month`, `sales_price_cnt`, `model_seq`) VALUES
(202401, 5000, 1), (202402, 4800, 1),
(202401, 4200, 2), (202402, 4300, 2),
(202401, 7000, 3), (202402, 6800, 3),
(202401, 3100, 4), (202402, 2900, 4),
(202401, 8000, 5), (202402, 7500, 5),
(202401, 2200, 6), (202402, 2100, 6),
(202401, 5400, 7), (202402, 5200, 7),
(202401, 3600, 8), (202402, 3500, 8),
(202401, 2500, 9), (202402, 2400, 9),
(202401, 2700, 10), (202402, 2600, 10);
