import time

def play_game(path):
    
    with open(path, "r", encoding="utf-8") as f:
        start_time = time.time()
        string_count = 0                                                     # 문자열의 개수를 세는 변수

        for line in f.readlines():
            line = line.strip()                                                # 필요없는 부분 제거
            if line == "":
                continue
            string_count = string_count + len(line) 

            while True:
                print(line)
                user = input()
                if line.strip() == user:
                    break
                else:
                    print("잘못 입력하셨습니다.")

        end_time = time.time()
        elapsed_time = end_time - start_time
    print(int(string_count / elapsed_time * 60))

# 사용하고자 하는 파일 경로를 인자로 넣어 함수 호출
''' play_game("data/test.txt") '''
 # 실수로 변환
    
''' play_game("data/서시.txt") '''
    
    
        


