import time

def play_game(path):
    
    with open(path, "r", encoding="utf-8") as f:
        start_time = time.time()
        string_count = 0                                                     

        for line in f.readlines():
            line = line.strip()                                                
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


    
    
        


