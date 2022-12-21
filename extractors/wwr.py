from requests import get
from bs4 import BeautifulSoup


def extract_wwr_jobs(keyword):
  base_url = "https://weworkremotely.com/remote-jobs/search?term="
  language = keyword
  url = f"{base_url}{language}"

  response = get(url)
  if not response.status_code == 200:
    print("웹사이트로 부터 데이터를 받아올 수 없습니다.")
  else:
    result = []
    soup = BeautifulSoup(
      response.text,
      "html.parser")  #response.text를 beautifulsoup 한테 html을 보낸다고 말함
    jobs = soup.find_all('section',
                         class_="jobs")  #class가 jobs인 section들을 다 찾기
    # print(len(jobs))  #jobs list가 2개로 있음을 알 수 있음
    for job_section in jobs:
      job_posts = job_section.find_all("li")
      job_posts.pop(-1)
      for post in job_posts:
        anchor = post.find_all('a')
        anchor = anchor[1]
        company_link = (anchor['href']
                        )  #href 태그만 가져오기 https://weworkremotely.com/
        company, position, region = anchor.find_all('span', class_="company")
        # print(company,position,region)
        title = anchor.find('span', class_="title")
        # print(company.string, position.string, region.string, title.string)
        job_data = {
          '사이트 주소': f"https://weworkremotely.com/{company_link}",
          '회사명': company.string,  #html 태그 지우고 string만 남김
          '근무 가능 지역': region.string,
          '기타': title.string
        }
        result.append(job_data)
      return result
