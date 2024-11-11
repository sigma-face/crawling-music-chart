from selenium import webdriver # pip install selenium bs4
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# ChromeDriver를 자동으로 다운로드하고 설정
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # 브라우저 창 표시 없이 실행
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # 멜론 차트 페이지 열기
    driver.get('https://www.melon.com/chart/index.htm')
    time.sleep(3)  # 페이지가 로드될 때까지 잠시 대기

    # 페이지 소스 가져오기
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # 노래 제목과 가수명 크롤링
    chart_data = []
    songs = soup.select('div.ellipsis.rank01 > span > a')  # 노래 제목
    artists = soup.select('div.ellipsis.rank02 > span')  # 가수명

    for song, artist in zip(songs, artists):
        chart_data.append({
            'title': song.get_text(),
            'artist': artist.get_text()
        })

    # 결과 출력
    for rank, data in enumerate(chart_data, 1):
        print(f"{rank}. {data['title']} - {data['artist']}")

finally:
    driver.quit()
