import os

def get_desktop_files():
    # 1. 바탕화면 경로 설정 (Windows 기준)
    # 'USERPROFILE' 환경 변수를 사용하여 현재 사용자의 홈 디렉토리를 가져옵니다.
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    
    try:
        # 2. 해당 경로의 파일 및 폴더 목록 가져오기
        files = os.listdir(desktop_path)
        
        print(f"--- 바탕화면 목록 ({desktop_path}) ---")
        
        # 3. 목록 출력
        if not files:
            print("바탕화면이 비어 있습니다.")
        else:
            for file in files:
                print(file)
                
    except FileNotFoundError:
        print("바탕화면 경로를 찾을 수 없습니다.")
    except Exception as e:
        print(f"오류가 발생했습니다: {e}")

# 함수 실행
if __name__ == "__main__":
    get_desktop_files()