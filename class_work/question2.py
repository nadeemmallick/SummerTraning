def decrease_health(current_health, damage):
    new_health = current_health - damage
    return max(new_health, 0) 

try:
    health = int(input("Enter player's current health: "))
    damage = int(input("Enter damage taken: "))

    remaining = decrease_health(health, damage)
    print(f"Player's remaining health: {remaining}")

except ValueError:
    print("Please enter valid integer values.")