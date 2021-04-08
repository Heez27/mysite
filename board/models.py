from django.db import models
from MySQLdb import connect, OperationalError
from MySQLdb.cursors import DictCursor

# Create your models here.

def findall(): # 전체 방명록 가져오기
    try:
        # 연결
        db = conn()

        # cursor 생성
        cursor = db.cursor(DictCursor)

        # SQL 실행
        sql = 'select no, title, contents, hit, reg_date, g_no, o_no, depth, user_no from board'
        cursor.execute(sql)

        # 결과 받아오기
        result = cursor.fetchone() # Fetches a single row from the cursor. None indicates that no more rows are available.

        # 자원 정리
        cursor.close()
        db.close()

        #결과 반환
        return result


    except OperationalError as e:
        print(f'error: {e}')


def conn():
    return connect(
        user='webdb',
        password='webdb',
        host='localhost',
        port=3306,
        db='webdb',
        charset='utf8')