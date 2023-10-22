import threading
import time

# 스레드에서 실행할 함수


# def work():
#     print("[sub]")
#     keyword = input("[sub] keyword: ")
#     print(f"[sub] searching {keyword}")
#     print("[sub] end")


# # 메인스레드 실행
# print("[main]")

# worker = threading.Thread(target=work)
# # worker.daemon = True # 메인스레드가 종료되면 함께 종료
# worker.start()

# print("[main] working...")
# print("[main] end")

print("=========================================")


def buyer():
    for i in range(5):
        print("[매수] 데이터 요청 중...")
        time.sleep(1)
        print("[매수] 데이터 분석 중...")
        time.sleep(1)
        print("[매수] 매수 신호 방생!")
        time.sleep(1)
        print("[매수] 매수 신청 완료!")
        time.sleep(1)


def seler():
    for i in range(5):
        print("[매도] 데이터 요청 중...")
        time.sleep(1)
        print("[매도] 데이터 분석 중...")
        time.sleep(1)
        print("[매도] 매도 신호 방생!")
        time.sleep(1)
        print("[매도] 매도 신청 완료!")
        time.sleep(1)


print("[main] start")
buyer = threading.Thread(target=buyer)
seler = threading.Thread(target=seler)
buyer.start()
seler.start()

# join() 메서드를 호출한 스레드가 종료될 때까지 메인 스레드가 기다린다.
buyer.join()
seler.join()
print("[main] end")
