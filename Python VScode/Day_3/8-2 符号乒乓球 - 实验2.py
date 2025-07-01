import time 

# 设置黄色字体、蓝色背景（可根据需求调整）
print("\033[33;44m", end="")  

# 乒乓球动画的符号序列，模拟球的运动姿态变化
frames = [
    "▐⠂       ▌",
    "▐⠈       ▌",
    "▐ ⠠      ▌",
    "▐  ⢀     ▌",
    "▐   ⡀    ▌",
    "▐    ⢀   ▌",
    "▐     ⡀  ▌",
    "▐      ⢀ ▌",
    "▐       ⡀▌",
    "▐      ⢀ ▌",
    "▐     ⡀  ▌",
    "▐    ⢀   ▌",
    "▐   ⡀    ▌",
    "▐  ⢀     ▌",
    "▐ ⠠      ▌",
    "▐⠈       ▌",
    "▐⠂       ▌",
]

try:
    while True:
        for frame in frames:
            print(f"\r{frame}", end="")
            time.sleep(0.2)
except KeyboardInterrupt:
    # 捕获 Ctrl + C 终止信号，清理终端格式
    print("\033[0m")