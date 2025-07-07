def collecting_coins(player_coins, new_coins):
    return player_coins + new_coins

player_coins = int(input("Enter the number of coins you player currently have: ")) 

new_coins = int(input("Enter the number of coins player collected: "))         

player_coins = collecting_coins(player_coins, new_coins)

print("Total Coins:", player_coins)
