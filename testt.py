import os
import shutil
import sqlite3
from datetime import datetime, timedelta

def get_chrome_history_all():
    history_path = os.path.expandvars(r'%LOCALAPPDATA%\Google\Chrome\User Data\Default\History')
    temp_history = 'History_temp'
    shutil.copy2(history_path, temp_history)

    conn = sqlite3.connect(temp_history)
    cursor = conn.cursor()

    cursor.execute("SELECT url, title, last_visit_time FROM urls ORDER BY last_visit_time DESC")

    rows = cursor.fetchall()
    conn.close()
    os.remove(temp_history)

    def chrome_time_to_readable(chrome_time):
        if chrome_time:
            epoch_start = datetime(1601, 1, 1)
            delta = timedelta(microseconds=chrome_time)
            return epoch_start + delta
        else:
            return None

    with open("결과.txt", "w", encoding="utf-8") as f:
        for url, title, last_visit in rows:
            visit_time = chrome_time_to_readable(last_visit)
            time_str = visit_time.strftime('%Y-%m-%d %H:%M:%S') if visit_time else "Unknown"
            f.write(f"{time_str} - {title} - {url}\n")

if __name__ == "__main__":
    get_chrome_history_all()
    print("결과.txt 파일에 저장 완료")
