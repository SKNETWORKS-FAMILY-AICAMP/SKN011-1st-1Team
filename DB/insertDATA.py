import mysql.connector

connection= mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='catcardb'
)

cursor=connection.cursor()

insert_brand_sql='INSERT INTO `brand` (`brand_name`, `brand_country`) VALUES (%s,%s)'
brand_values=()
cursor.executemany(insert_brand_sql,brand_values)
connection.commit()

insert_model_sql='INSERT INTO `model` (`model_name`, `model_image`, `model_price`, `model_category`, `brand_seq`) VALUES(%s,%s,%s,%s,%s)'
model_values=()
cursor.executemany(insert_model_sql,model_values)
connection.commit()

insert_news_sql='INSERT INTO `news` (`news_title`, `news_url`, `model_seq`) VALUES (%s,%s,%s)'
news_values=()
cursor.executemany(insert_news_sql,news_values)

insert_sales_sql='INSERT INTO `sales` (`sales_month`, `sales_price_cnt`, `model_seq`) VALUES (%s,%s,%s)'
sales_values=()
cursor.executemany(insert_sales_sql,sales_values)
connection.commit()

cursor.close()
connection.close()