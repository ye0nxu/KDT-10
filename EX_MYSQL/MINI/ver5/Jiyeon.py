# Jiyeon.py
import datetime as dt
from function import get_connection, ATT_TABLE


def checkIn_Delay(emp_id):
    """
    근태 테이블에서 emp_id에 해당하는 출근시간(check_in)을 읽어와
    09:00:00 이후면 '지각', 이하면 '출근'으로 status를 갱신.
    """
    try:
        conn = get_connection()
    except Exception as e:
        print("DB 연결 오류:", e)
        return "db_error"

    SQL = f"""
        SELECT emp_id, att_date, check_in, status
        FROM {ATT_TABLE}
        WHERE emp_id = %s
        ORDER BY att_date;
    """

    UPDATE_SQL = f"""
        UPDATE {ATT_TABLE}
        SET status = %s, check_in = %s
        WHERE emp_id = %s AND att_date = %s;
    """

    with conn.cursor() as cursor:
        cursor.execute(SQL, (emp_id,))
        records = cursor.fetchall()

        if not records:
            conn.close()
            return "no_records"

        start = dt.datetime.strptime("09:00:00", "%H:%M:%S").time()

        for row in records:
            emp_id_val = row["emp_id"]
            raw = row["check_in"]

            # MySQL TIME → 파이썬 timedelta/time/str 다양한 경우 처리
            if isinstance(raw, dt.timedelta):
                check_time = (dt.datetime.min + raw).time()
            elif isinstance(raw, dt.time):
                check_time = raw
            else:
                check_time = dt.datetime.strptime(str(raw), "%H:%M:%S").time()

            status = "출근" if check_time <= start else "지각"

            cursor.execute(
                UPDATE_SQL,
                (status, check_time, emp_id_val, row["att_date"])
            )

        conn.commit()

    conn.close()
    print("근태 상태 업데이트 완료")
    return "updated"


def checkOut_work(emp_id):
    try:
        conn = get_connection()
    except Exception as e:
        print("DB 연결 오류:", e)
        return "db_error"
    
    
    SQL = """
        SELECT emp_id, att_date, check_out, status_2 
        FROM attendance
        WHERE emp_id = %s 
        ORDER BY att_date;
        """

    UPDATE_SQL = """
        UPDATE attendance 
        SET status_2 = %s,
            check_out = %s
        WHERE emp_id = %s AND att_date = %s;
        """

    with conn.cursor() as cursor:
        cursor.execute(SQL, (emp_id,))
        records = cursor.fetchall()

        if records == None:
            return "연차"

        end = dt.datetime.strptime("18:00:00", "%H:%M:%S").time()
        limit = dt.datetime.strptime("19:00:00", "%H:%M:%S").time()

        for row in records:
            emp_id = row["emp_id"]

            # timedelta → datetime.time 변환
            check_dt = (dt.datetime.min + row["check_out"]).time()

            # time → 문자열 "HH:MM:SS"
            check_out_str = check_dt.strftime("%H:%M:%S")

            # 상태 분류
            if check_dt <= end:
                status2 = "조퇴"
            elif check_dt < limit:
                status2 = "퇴근"
            else:
                status2 = "야근"

            # UPDATE 실행
            cursor.execute(
                UPDATE_SQL,
                (status2, check_out_str, emp_id, row["att_date"])
            )

        conn.commit()

    print("업데이트완료")