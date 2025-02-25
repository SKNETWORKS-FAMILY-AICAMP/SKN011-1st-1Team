import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("국내 차량 검색")

#페이지 설정
# st.set_page_config(page_title = 'Introduction',layout='wide')

#세션 초기화
# if 'page' not in st.session_state:
#     st.session_state.page = "Introduction"

#사이드 바
# pg = st.navigation([st.Page("국내_차량.py")])

# pg.run()
# st.sidebar.title("🚗MENU")

# if st.sidebar.button("Introduction"):
#     st.session_state.page = "Introduction"
# if st.sidebar.button("국내 차량"):
#     st.session_state.page = "국내 차량"
# if st.sidebar.button("외제 차량"):
#     st.session_state.page = "외제 차량"
# if st.sidebar.button("FAQ"):
#     st.session_state.page = "FAQ"

#홈화면
# if st.session_state.page == 'Introduction':
#     st.title("CATCAR")
#     st.markdown("## ⭐차량을 구매하시려는 분들의 합리적인 소비를 \n ## 도와드리기 위한 페이지 입니다.")
#     st.write(" ")
#     st.write(" 🔴이 분석은 어떤 데이터를 기반으로 하나요?")
#     st.write(" ➡️자동차 제조사 발표 자료, 시장 조사 데이터, 중고차 가격 변동, 소비자 리뷰,\n 검색 트렌드, 전기차 및 자율주행 기술 발전 상황 등을 종합적으로 분석합니다.")
#     st.write("🔴 이 분석이 실제 차량 구매에 어떻게 도움이 되나요?")
#     st.write("➡️소비자들은 현재 인기 있는 차량과 향후 가치가 상승할 가능성이 있는 모델을 \n 쉽게 파악할 수 있으며, 차량 구매 시 합리적인 선택을 할 수 있습니다.")


#국내 차량 페이지
# elif st.session_state.page == "국내 차량":

# 세로 정렬을 위한 컨테이너
with st.container():
    brand = st.text_input("브랜드 검색", key="brand1_search")

with st.container():
    model = st.text_input("모델 검색", key="model1_search")

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



#외제 차량 페이지
# elif st.session_state.page == "외제 차량":
#     st.title("국내 차량 검색")
    
#     # 세로 정렬을 위한 컨테이너
#     with st.container():
#         brand = st.text_input("브랜드 검색", key="brand_search")

#     with st.container():
#         model = st.text_input("모델 검색", key="model_search")

    
#         if st.button("✅"):
    

#             empty1,con1,empty2 = st.columns([0.3,1.0,0.3])
#             empty1,con2,con3,empty2 = st.columns([0.3,0.5,0.5,0.3])
#             empty1,con4,empty2 = st.columns([0.3,1.0,0.3])

        
#         def get_sales_data():
#             return pd.DataFrame({

#             })

#         def get_comparison_data():
#             return pd.DataFrame({

#             })
        
#         def get_news_articles():
#             return[
                
#             ]



#         def main():
#             with empty1:
#                 print("")

#             with con1:
#                 st.subheader("🔍 차량 검색")
#                 brand = st.text_input("브랜드 검색")
#                 model = st.text_input("모델 검색")
#                 search_button = st.button("✅")

#             with con2:
#                 st.subheader('판매 실적')
#                 sales_data = get_sales_data()
#                 if search_button:
#                     if brand:
#                         sales_data = sales_data[sales_data["브랜드"].str.contains(brand, case=False, na=False)]
#                     if model:
#                         sales_data = sales_data[sales_data["모델"].str.contains(model, case=False, na=False)]
                    
#                     if sales_data.empty:
#                         st.warning("❌ 해당 브랜드 또는 모델을 찾을 수 없습니다.")
#                     else:
#                         st.dataframe(sales_data)

#             with con3:
#                 st.subheader("비교 실적")
#                 comparison_data = get_comparison_data()
#                 st.dataframe(comparison_data)
                        

#             with con4:
#                 st.subheader("📰 뉴스 기사")
#                 news_articles = get_news_articles()
#                 for article in news_articles:
#                     st.write(article)
            
#             with empty2:
#                 print("")

        


#         if __name__ == "__main__":
#             main()




# #FAQ 페이지
# elif st. session_state.page == "FAQ":
#     st.title("❓자주 묻는 질문 FAQ")

#     faq_list = [

#     ]

#     for question, answer in faq_list:
#         with st.expander(question): #클릭하면 펼쳐짐
#             st.write(answer)






