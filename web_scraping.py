from requests import get
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs

language = input("일을 알아보고 싶은 언어를 영어로 입력해 주세요")
extract = extract_wwr_jobs(language)
if extract == None:
  print(f"죄송합니다 {language}와 관련된 일이 나오지 않습니다.")
else:
  for extracts in extract:
    print(extracts)
    print("///////")
