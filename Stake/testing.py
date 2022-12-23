with open('config.txt', 'r') as f:
    LINES = f.readlines()
    bet_amount = LINES[2].strip()
    on_loss = LINES[6].strip()
    stop_on_profit = LINES[10].strip()
    target = LINES[14].strip()
    fairness = LINES[18].strip()
    print(bet_amount, on_loss, stop_on_profit, target, fairness)