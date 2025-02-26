import mysql.connector
from datetime import datetime

connection= mysql.connector.connect(
    host='localhost',
    user='',
    password='',
    database='catcardb',
)

def FAQ1(model_seq):

    cursor = connection.cursor(dictionary=True) # 딕셔너리 형태로 반환

    year_avg_sales_cnt=''

     # 올해 평균 판매량 출력 (올해 데이터가 존재하지 않는다면 작년으로 변경)
    sql1=f'SELECT model_seq,model_name, AVG(sales_price_cnt) as "year_avg_sales_cnt" FROM model JOIN sales USING (model_seq) WHERE model_seq={model_seq} GROUP BY model_seq'
    cursor.execute(sql1)
    year_avg_sales_cnt=cursor.fetchall()
    if(year_avg_sales_cnt == []): # 데이터가 없는 경우 더미데이터 출력력
        year_avg_sales_cnt=[{'model_seq': -1, 'model_name': '', 'year_avg_sales_cnt': 0}]
    

    sql2=f'SELECT model_seq,model_name, sales_price_cnt FROM model JOIN sales USING (model_seq) WHERE model_seq={model_seq} LIMIT 1' # 해당 모델의 가장 최근 판매량 출력
    cursor.execute(sql2)
    last_sales_cnt=cursor.fetchall()

    appropriateness=''

    
    if(year_avg_sales_cnt[0]['year_avg_sales_cnt'] >= last_sales_cnt[0]['sales_price_cnt']): # 해당 모델의 올해 평균 판매량과 최근 판매량을 비교하여 사는 것과 사지 않는 것 판단
        appropriateness='positive' # 올해 평균 판매량이 크다면 '긍정'
    else:
         appropriateness='nagative' # 가장 최근 판매량이 크다면 '부정'


    result={
        'year_avg_sales_cnt' : year_avg_sales_cnt,
        'last_sales_cnt' : last_sales_cnt,
        'appropriateness' : appropriateness
    }

    cursor.close()
    
    return result

# print(FAQ1(1))

def FAQ3(model_seq): # 해당 모델의 월별 평균 판매량 데이터를 산출하여 판매량이 가장 높을 때부터 내림차순으로 출력

    cursor = connection.cursor(dictionary=True) # 딕셔너리 형태로 반환

    sql2=f'SELECT model_seq, model_name, sales_month, AVG(sales_price_cnt) AS month_avg_sales FROM model JOIN sales USING (model_seq) WHERE model_seq={model_seq} GROUP BY model_seq, model_name,sales_month ORDER BY AVG(sales_price_cnt) DESC LIMIT 1' 
    cursor.execute(sql2)
    result=cursor.fetchall()

    cursor.close()
    
    return result

print(FAQ3(1))
