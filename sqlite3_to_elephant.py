import sqlite3
import psycopg2
import dbapi

HOST = dbapi.host
DATABASE = dbapi.database
USER = dbapi.user
PASSWORD = dbapi.password

post_conn = psycopg2.connect(
  host=HOST,
  database=DATABASE,
  user=USER,
  password=PASSWORD)

post_cur = post_conn.cursor()

lite_conn = sqlite3.connect('eda.db')
lite_cur = lite_conn.cursor()
lite_cur.execute("SELECT * FROM job")
all = lite_cur.fetchall()
print(all[0])



post_cur.execute("DROP TABLE IF EXISTS job")
post_cur.execute("""--sql
CREATE TABLE job (
  id INTEGER,
  job_type VARCHAR,
  industry VARCHAR,
  experience VARCHAR,
  education VARCHAR,
  salary VARCHAR
  );
""")
post_conn.commit()
post_cur.executemany(
  """--sql
  INSERT INTO job
  VALUES(%s, %s, %s, %s, %s, %s);
""", all)
post_conn.commit()
print("완료")