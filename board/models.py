from django.db import models
from MySQLdb import connect, OperationalError
from MySQLdb.cursors import DictCursor

# Create your models here.

def findbyno(no):
    try:
        db = conn()
        cursor = db.cursor(DictCursor)

        sql = 'select no, name, title, contents, hit, reg_date, g_no, o_no, depth from board join user using (no) where no= %s'
        cursor.execute(sql, (no, ))
        result = cursor.fetchone()

        # 자원 정리
        cursor.close()
        db.close()

        return result

    except OperationalError as e:
        print(f'error: {e}')


def findall():
    try:
        # 연결
        db = conn()

        # cursor 생성
        cursor = db.cursor(DictCursor)

        # SQL 실행
        sql = 'select no, name, title, contents, hit, reg_date, g_no, o_no, depth from board join user using (no)'
        cursor.execute(sql)

        # 결과 받아오기
        result = cursor.fetchall() # Fetches a single row from the cursor. None indicates that no more rows are available.

        # 자원 정리
        cursor.close()
        db.close()

        #결과 반환
        return result


    except OperationalError as e:
        print(f'error: {e}')




def write(no, title, content):
    try:
        # 연결
        db = conn()

        # cursor 생성
        cursor = db.cursor()

        # SQL 실행
        sql = 'insert into board values(null, %s, %s, 0, now(), 0, 0, 0, %s)'
        count = cursor.execute(sql, (title, content, no))

        # commit
        db.commit()

        # 자원 정리
        cursor.close()
        db.close()

        # 결과 반환
        return count == 1

    except OperationalError as e:
        print(f'error: {e}')


def update(no, title, content):
    try:
        # 연결
        db = conn()

        # cursor 생성
        cursor = db.cursor()

        # SQL 실행
        sql = 'update board set title = %s, contents=%s where no=%s'
        count = cursor.execute(sql, (title, content, no))

        # commit
        db.commit()

        # 자원 정리
        cursor.close()
        db.close()

        # 결과 반환
        return count == 1

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