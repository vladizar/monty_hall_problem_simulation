from random import randint

# Simulates one Monty Hall game played optimal if optimal = True else not optimal
# Returns True if the player guessed the door with a car behind it else False
def play_monty(optimal = False):
  # Set up the 'doors' Boolean array with all Falses (goats) except 1 True value on random index (car)
  car = randint(0, 2)
  doors = [i == car for i in range(3)]
  
  # Make a random guess
  guess = randint(0, 2)
  
  # Monty chooses a door with goat to open
  for i in range(3):
    if i != guess and i != car:
      opened = i
      break
  
  # If player decides to play optimal, change their guess to another door that wasn't opened by Monty
  if optimal:
    for i in range(3):
      if i != guess and i != opened:
        guess = i
        break
  
  # Return if there was a car behind the guessed door
  # Because the 'doors' array looks like this "[False, True, False]" we can just return the 'doors' on 'guess' index
  # For this example doors[0] returns False, doors[1] returns True and doors[2] returns False
  return doors[guess]

# Set the number of games to play (more games => better accuracy)
N = 100000

# Play both optimal and not optimal and store the results of each game
results = [play_monty() for _ in range(N)]
opt_results = [play_monty(optimal=True) for _ in range(N)]

# Print the results for not optimal plays
print(f"Results for NOT optimal play:")
print(f"Win chance: {results.count(True) / N}")

# Print the results for optimal plays
print(f"Results for optimal play:")
print(f"Win chance: {opt_results.count(True) / N}")