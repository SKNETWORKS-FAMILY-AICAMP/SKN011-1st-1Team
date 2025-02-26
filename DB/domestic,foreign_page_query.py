import mysql.connector

connection= mysql.connector.connect(
    host='localhost',
    user='',
    password='',
    database='catcardb',
)

def domesticShowBrand(): # brand 테이블의 브랜드명 조회 # 국내 차종 검색 페이지

    cursor = connection.cursor(dictionary=True) # 딕셔너리 형태로 반환

    sql='SELECT brand_seq,brand_name FROM brand WHERE brand_country=0'
    cursor.execute(sql)
    result=cursor.fetchall()

    cursor.close()
    
    return result

# print(domesticShowBrand())

def foreignShowBrand(): # brand 테이블의 브랜드명 조회 # 외제 차종 검색 페이지

    cursor = connection.cursor(dictionary=True) # 딕셔너리 형태로 반환

    sql='SELECT brand_seq,brand_name FROM brand WHERE brand_country=1'
    cursor.execute(sql)
    result=cursor.fetchall()

    cursor.close()
    
    return result

# print(foreignShowBrand())

def showModel(brand_seq): # 선택한 브랜드를 기반으로 해당 브랜드의 모델명 조회

    cursor = connection.cursor(dictionary=True)

    sql=f'SELECT model_seq,model_name FROM model WHERE brand_seq= (SELECT brand_seq FROM brand WHERE brand_seq={brand_seq})'
    cursor.execute(sql)
    result=cursor.fetchall()

    cursor.close()
    
    return result

# print(showModel(1))


def showModelDetail(model_seq): # 모델 번호 기반 관련 데이터 조회

    cursor = connection.cursor(dictionary=True)

    sql_model=f'SELECT * FROM model WHERE model_seq={model_seq}' # 상세 모델 정보 데이터 딕셔너리
    cursor.execute(sql_model)
    model_data=cursor.fetchall()

    sql_sales=f'SELECT * FROM sales WHERE model_seq={model_seq}' # 모델 기반 실적 데이터 딕셔너리
    cursor.execute(sql_sales)
    sales_data=cursor.fetchall()

    sql_news=f'SELECT * FROM news WHERE model_seq={model_seq}' # 모델 기반 기사 데이터 딕셔너리
    cursor.execute(sql_news)
    news_data=cursor.fetchall()

    cursor.close()
    
    result={
        'model' : model_data,
        'sales' : sales_data,
        'news' : news_data
    }

    return result

# print(showModelDetail(1))

def showAnotherModelDetail(model_seq,limit): # 해당 model_seq와 카테고리 값이 같은 데이터들을 총 판매량을 기준으로 내림차순으로 limit개까지 딕셔너리로 산출함

    cursor=connection.cursor(dictionary=True)
    sql= f'SELECT * FROM total_sales_desc WHERE model_category=(SELECT model_category FROM model WHERE model_seq={model_seq}) AND model_seq != {model_seq} LIMIT {limit}'
    cursor.execute(sql)
    result=cursor.fetchall()

    cursor.close()

    return result

# print(showAnotherModelDetail(1,3))
