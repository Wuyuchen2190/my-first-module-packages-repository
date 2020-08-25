def p_time_1(func):#计算程序耗时的装饰器,接受单一参数（被装饰后的函数实际上是tiemcost,所以只能传入一个参数）
    def timecost(x):
        import time
        time_1=time.time()
        func(x)
        time_2=time.time()
        result=time_2-time_1
        return "耗时:{0}".format(result)
    return timecost

def p_time_2(func):#计算程序耗时的装饰器,接受两个参数
    def timecost(x_1,x_2):
        import time
        time_1=time.time()
        func(x_1,x_2)
        time_2=time.time()
        result=time_2-time_1
        return "耗时:{0}".format(result)
    return timecost

def p_time_3(func):#计算程序耗时的装饰器,接受三个参数
    def timecost(x_1,x_2,x_3):
        import time
        time_1=time.time()
        func(x_1,x_2,x_3)
        time_2=time.time()
        result=time_2-time_1
        return "耗时:{0}".format(result)
    return timecost
