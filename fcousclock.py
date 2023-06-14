# 导入time模块
import time

# 定义一个Clock类
class Clock:

    # 初始化方法，设置时、分、秒
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    # 定义一个run方法，让时钟走动
    def run(self):
        # 每秒增加一秒
        self.second += 1
        # 如果秒数等于60，分钟增加一分钟，秒数归零
        if self.second == 60:
            self.minute += 1
            self.second = 0
        # 如果分钟等于60，小时增加一小时，分钟归零
        if self.minute == 60:
            self.hour += 1
            self.minute = 0
        # 如果小时等于24，小时归零
        if self.hour == 24:
            self.hour = 0

    # 定义一个show方法，显示时钟的时间
    def show(self):
        # 格式化输出时间，补零对齐
        print(f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}")

# 创建一个Clock对象，设置初始时间为10:00:00
clock = Clock(10, 0, 0)

# 循环执行run和show方法，每隔一秒显示一次时间
while True:
    clock.run()
    clock.show()
    time.sleep(1)
