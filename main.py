import random

wins = 0
losses = 0
swapping = True

for i in range(1000):
  # Shown all all_doors
  all_doors = [0, 1, 2]
  print(f"All doors: {all_doors}")

  # Car is behind a random all_doors
  car_door = random.randrange(3)
  print(f"Car door: {car_door}")

  # Pick a random door
  picked_door = random.randrange(3)
  print(f"Picked door: {picked_door}")

  # Presenter knows which doors have goats
  goat_doors = all_doors.copy()
  goat_doors.remove(car_door)
  print(f"Goat doors: {goat_doors}")

  # Presenter shows you a goat door
  goat_doors_could_show = goat_doors.copy()
  if picked_door in goat_doors_could_show:
    goat_doors_could_show.remove(picked_door)
  print(f"Goat doors could show: {goat_doors_could_show}")
  shown_goat_door = random.choice(goat_doors_could_show)
  print(f"Shown goat door: {shown_goat_door}")

  # Swap the door you picked
  remaining_doors = all_doors.copy()
  remaining_doors.remove(shown_goat_door)
  remaining_doors.remove(picked_door)

  if swapping:
    picked_door = remaining_doors[0]

  print(f"New picked door: {picked_door}")

  # Does the picked door have the car?
  if picked_door == car_door:
    print("Win")
    wins += 1
  else:
    print("Lose")
    losses += 1

print(f"Wins: {wins}")
print(f"Losses: {losses}")
