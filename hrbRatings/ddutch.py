def dutching_calculator(odds1, odds2, odds3, stake):
    total_odds = 1 / odds1 + 1 / odds2 + 1 / odds3
    stake1 = stake * (1 / odds1) / total_odds
    stake2 = stake * (1 / odds2) / total_odds
    stake3 = stake * (1 / odds3) / total_odds
    return stake1, stake2, stake3

odds1 = 5.0
odds2 = 4.5
odds3 = 3.0
stake = 100

stake1, stake2, stake3 = dutching_calculator(odds1, odds2, odds3, stake)
print("Stake on horse 1:", stake1)
print("Stake on horse 2:", stake2)
print("Stake on horse 3:", stake3)
