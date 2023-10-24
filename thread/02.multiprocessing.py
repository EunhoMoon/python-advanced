import multiprocessing as mp

# 프로세스에서 실행할 함수


# def sub_process(name):
#     print("[sub] start")
#     print(name)
#     cp = mp.current_process()
#     print(f"[sub] pid: {cp.pid}")
#     print("[sub] end")


# #  메인 프로세스
# if __name__ == "__main__":
#     print("[main] start")
#     p = mp.Process(target=sub_process, args=("janek",))
#     p.start()
#     cp = mp.current_process()
#     print(f"[main] pid: {cp.pid}")
#     print("[main] end")

from multiprocessing import Process
import time


class Subprocess(Process):

    def __init__(self, name):
        Process.__init__(self)
        self.name = name

    def run(self):
        print(f"[sub] {self.name} start")
        time.sleep(5)
        print(f"[sub] {self.name} end")


if __name__ == "__main__":
    print("[main] start")
    p = Subprocess(name="janek")
    p.start()
    # p.join()
    time.sleep(1)
    # 프로세스가 살아있는지 검사
    print(p.is_alive())
    print("[main] end")
