def dutching_calculator(odds1, odds2, odds3, stake=5.0):
    total_odds = 1 / odds1 + 1 / odds2 + 1 / odds3
    stake1 = round((stake * (1 / odds1) / total_odds),2)
    stake2 = round((stake * (1 / odds2) / total_odds), 2)
    stake3 = round((stake * (1 / odds3) / total_odds),2)
    return stake1, stake2, stake3

odds1 = (10/3)+1
odds2 = (6/1)+1
odds3 = (4/1)+1
#odds1 = 5.2
#odds2 = 7.8
#odds3 = 8.2
stake = 5.0

stake1, stake2, stake3 = dutching_calculator(odds1, odds2, odds3, stake)
print(f'Stake on horse 1: {stake1}')
print(f'Stake on horse 2: {stake2}')
print(f'Stake on horse 3: {stake3}')
