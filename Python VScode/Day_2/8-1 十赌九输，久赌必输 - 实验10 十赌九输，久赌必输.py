import random, math

def gambleOnce():
    # 根据随机数返回表示赌局胜负的布尔值
    # 50% 概率赢，50% 概率输（简单模拟）
    return random.random() < 0.5  

def gambleDay(money):
    if money < 1:
        # 赌本不足以下注，直接返回
        return money

    wager = 1  # 第 1 局赌注一元
    money -= wager

    while not gambleOnce():
        # 赌注翻倍（这里用 *= 实现翻倍逻辑）
        wager *= 2  
        money -= wager
        if money <= 0:
            return money

    # 赌本 = 剩余赌本 + 胜局下注额的 2 倍（赢了就把之前输掉的 wager 赚回来，同时净赚 wager）
    money += wager * 2  
    return money

if __name__ == '__main__':
    moneyHold = 1024  # 初始赌本
    moneyHolds = []   # 用于存放每日结余赌本的列表

    dayNumber = 30    # 赌博天数
    for x in range(dayNumber):
        moneyHold = gambleDay(moneyHold)
        # 当日结余赌本加入列表
        moneyHolds.append(moneyHold)  

    from matplotlib import pyplot as plt
    plt.scatter(list(range(1, dayNumber+1)), moneyHolds, s=1)
    plt.title(f'Every day\'s money during {dayNumber} days')
    plt.show()