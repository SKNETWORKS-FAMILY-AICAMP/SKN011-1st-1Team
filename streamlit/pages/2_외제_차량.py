import streamlit as st
import pandas as pd

st.title("외제 차량 검색")
    
# 세로 정렬을 위한 컨테이너
with st.container():
    brand = st.text_input("브랜드 검색", key="brand2_search")

with st.container():
    model = st.text_input("모델 검색", key="model2_search")

if st.button("✅"):

    empty1,con1,empty2 = st.columns([0.1,1.0,0.1])
    empty1,con2,con3,empty2 = st.columns([0.1,0.5,0.5,0.1])
    empty1,con4,empty2 = st.columns([0.1,1.0,0.1])

        
    def get_sales_data():
        return pd.DataFrame({

        })

    def get_comparison_data():
        return pd.DataFrame({

        })
        
    def get_news_articles():
        return[
                
        ]



    def main():
        with empty1:
            print("")



        with con2:
            st.subheader('판매 실적')
            sales_data = get_sales_data()
            # if search_button:
            #     if brand:
            #         sales_data = sales_data[sales_data["브랜드"].str.contains(brand, case=False, na=False)]
            #     if model:
            #         sales_data = sales_data[sales_data["모델"].str.contains(model, case=False, na=False)]
                    
            #     if sales_data.empty:
            #         st.warning("❌ 해당 브랜드 또는 모델을 찾을 수 없습니다.")
            #     else:
            #         st.dataframe(sales_data)

        with con3:
            st.subheader("비교 실적")
            comparison_data = get_comparison_data()
            st.dataframe(comparison_data)
                        

        with con4:
            st.subheader("📰 뉴스 기사")
            news_articles = get_news_articles()
            for article in news_articles:
                st.write(article)
            
        with empty2:
            print("")

        


    if __name__ == "__main__":
        main()
