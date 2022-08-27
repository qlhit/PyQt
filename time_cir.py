from threading import Timer

def loop_func(func, second):
    #每隔second秒执行func函数
    while True:
        timer = Timer(second, func)
        timer.start()
        timer.join()

