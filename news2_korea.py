import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# 데이터 저장 리스트
korea_model_data = []

# Chrome 실행
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

# 특정 URL 접근
driver.get('https://auto.danawa.com/')
time.sleep(1)

# 자동차백과 클릭
try:
    dict_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="gnbMenu"]/div/div/div[4]/a')))
    dict_btn.click()
except NoSuchElementException:
    print("자동차 백과 버튼을 찾을 수 없습니다.")
    driver.quit()
    exit()

# 국내 브랜드 목록 가져오기
brands = driver.find_elements(By.CSS_SELECTOR, ".domestic .branditem a")

for brand in brands:
    try:
        brand_name = brand.find_element(By.CLASS_NAME, "name").text
        brand_link = brand.get_attribute("href")

        # 새 탭에서 브랜드 페이지 열기
        driver.execute_script("window.open(arguments[0]);", brand_link)
        WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
        driver.switch_to.window(driver.window_handles[-1])

        models = driver.find_elements(By.CSS_SELECTOR, ".modelList li a")

        for model in models:
            model_data = {
                "brand": brand_name,
                "model_name": "정보 없음",
                "news_title": "뉴스 없음",
                "news_link": "링크 없음",
            }

            try:
                model_name = model.find_element(By.CLASS_NAME, "name").text
                model_data["model_name"] = model_name
                model_link = model.get_attribute("href")

                # 새 탭에서 모델 페이지 열기
                driver.execute_script("window.open(arguments[0]);", model_link)
                WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 2)
                driver.switch_to.window(driver.window_handles[-1])

                try:
                    news = driver.find_element(By.CSS_SELECTOR, 'li[tab="news"] a.sendGAExcpt')
                    news_url = news.get_attribute("href")

                    # 새 탭에서 뉴스 페이지 열기
                    driver.execute_script("window.open(arguments[0]);", news_url)
                    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 3)
                    driver.switch_to.window(driver.window_handles[-1])

                    try:
                        news_area = driver.find_element(By.CSS_SELECTOR, ".newsTable")
                        title = news_area.find_element(By.CSS_SELECTOR, ".title").text
                        href = news_area.find_element(By.CSS_SELECTOR, "div.title a").get_attribute("href")
                        model_data["news_title"] = title
                        model_data["news_link"] = href
                    except NoSuchElementException:
                        pass  # 뉴스 정보가 없으면 넘어감

                    driver.close()
                    driver.switch_to.window(driver.window_handles[-1])

                except NoSuchElementException:
                    pass  # 뉴스 탭이 없으면 넘어감

                korea_model_data.append(model_data)
                print(model_data)

                driver.close()
                driver.switch_to.window(driver.window_handles[-1])

            except NoSuchElementException:
                pass  # 모델 정보 없으면 넘어감

        driver.close()
        driver.switch_to.window(driver.window_handles[-1])

    except NoSuchElementException:
        pass  # 브랜드 정보 없으면 넘어감

# CSV 파일로 저장 (헤더 없이 데이터만 저장)
csv_filename = "korea3_model_data.csv"
with open(csv_filename, mode="w", newline=",", encoding="utf-8") as file:
    writer = csv.writer(file)
    
    # 데이터 저장 (헤더 없음)
    for model in korea_model_data:
        writer.writerow([f'"model_name":{model["model_name"]}, "news_title"={model["news_title"]},"news_link"={model["news_link"]}'])

print(f"데이터가 {csv_filename} 파일로 저장되었습니다.")

# 브라우저 종료
driver.quit()
