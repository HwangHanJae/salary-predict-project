import psycopg2
import key
import requests
import json
import datetime
import time

HOST = key.host
DATABASE =key.database
USER = key.user
PASSWORD = key.password

conn = psycopg2.connect(
  host=HOST,
  database = DATABASE,
  user = USER,
  password = PASSWORD
)
cur = conn.cursor()

def check_table(cur):
  is_table_exist = False
  try:
    cur.execute("""--sql
      SELECT * FROM job
    """)
    is_table_exist = True
    return is_table_exist
  #에러가 나올시 존재하지 않음
  # False를 반환
  except:
    is_table_exist = False
    return is_table_exist

def create_table(cur, conn):
  cur.execute("""--sql
    CREATE TABLE job(
      job_type VARCHAR,
      industry_code VARCHAR,
      industry_name VARCHAR,
      job_mid_code VARCHAR,
      job_mid_name VARCHAR,
      experience_code VARCHAR,
      experience_min VARCHAR,
      experience_max VARCHAR,
      education_code VARCHAR,
      salary_code VARCHAR,
      salary_info VARCHAR
    );
  """)
  conn.commit()

def insert_data(cur, conn):
  api_key = key.access_key
  
  for i in range(0,451,1):
    PATH = f"https://oapi.saramin.co.kr/job-search?access-key={api_key}&start={i}&count=110&fields=count&fields=keyword-code&published_max=2022-06-22 11:00:00"
    response = requests.get(PATH)
    json_file = json.loads(response.content)
    job = json_file['jobs']['job']
    for i in range(len(job)):
      #근무형태
      try:
        job_type = job[i]['position']['job-type']['name']
      except:
        job_type = None
      #업종코드
      try:
        industry_code = job[i]['position']['industry']['code']
      except:
        industry_code = None
      #업종명
      try:
        industry_name = job[i]['position']['industry']['name']
      except:
        industry_name = None
      #직무코드
      try:
        job_mid_code = job[i]['position']['job-mid-code']['code']
      except:
        job_mid_code = None
      #직무명
      try:
        job_mid_name = job[i]['position']['job-mid-code']['name']
      except:
        job_mid_name = None
      #경력코드
      try:
        experience_code = job[i]['position']['experience-level']['code']
      except:
        experience_code = None
      #최소경력
      try:
        experience_min = job[i]['position']['experience-level']['min']
      except:
        experience_min = None
      #최대경력
      try:
        experience_max = job[i]['position']['experience-level']['max']
      except:
        experience_max = None
      #학력코드
      try:
        education_code = job[i]['position']['required-education-level']['code']
      except:
        education_code=None
      #연봉코드
      try:
        salary_code = job[i]['salary']['code']
      except:
        salary_code = None
      #연봉정보
      try:
        salary_info = job[i]['salary']['name']
      except:
        salary_info = None
      data = (
      job_type,
      industry_code,
      industry_name,
      job_mid_code,
      job_mid_name,
      experience_code,
      experience_min,
      experience_max,
      education_code,
      salary_code,
      salary_info)
      cur.execute("""--sql
        INSERT INTO job VALUES(
          %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s
        )
      """,data)
      conn.commit()
      time.sleep(1)
    time.sleep(1)  

#cur.execute('ROLLBACK')
#테이블 존재 확인
is_table_exist = check_table(cur)
#테이블이 존재한다면 패스
if is_table_exist:
  pass
#테이블이 존재하지 않다면 생성
else:
  create_table(cur, conn)
#데이터베이스 적재 시간 측정
start_time = time.time()
#데이터베이스에 적재 시작
insert_data(cur, conn)
conn.commit()

end_time = time.time()
sec = (end_time-start_time)
result_time = datetime.timedelta(seconds=sec)
#시간 확인
print(result_time)