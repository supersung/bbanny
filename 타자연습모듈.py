import 타자연습
import os

file_list = os.listdir()                                                        #해당 디렉토리에 존재하는 모든 항목의 이름을 리스트로 반환

txt_list = [ ]                                                                        #텍스트 파일들만을 새로운 리스트로 구성

for path in file_list:
    if path[ -3: ] == "txt":
        txt_list.append(path)

for i in range(len(txt_list)):
    file_name = txt_list[i].split(".")[0]
    print(f"{i+1}) {file_name}")                                                       # 번호를 1번부터 괄호까지 출력하기

sel = input("> ")
idx = int(sel) - 1   

타자연습.play_game(txt_list[idx])
    


