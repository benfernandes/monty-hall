import random


def pick_random_door(doors):
    return random.choice(doors)


def get_goat_doors(doors, car_door):
    goat_doors = doors.copy()
    goat_doors.remove(car_door)
    return goat_doors


def get_shown_goat_door(goat_doors, picked_door):
    goat_doors_could_show = goat_doors.copy()

    if picked_door in goat_doors_could_show:
        goat_doors_could_show.remove(picked_door)

    shown_goat_door = random.choice(goat_doors_could_show)
    return shown_goat_door


def get_swapped_door(doors, shown_goat_door, picked_door):
    remaining_doors = doors.copy()
    remaining_doors.remove(shown_goat_door)
    remaining_doors.remove(picked_door)
    return remaining_doors[0]


def main(swapping, repetitions, number_of_doors):
    all_doors = [i for i in range(number_of_doors)]
    wins = 0
    losses = 0

    for i in range(repetitions):
        # Shown all all_doors
        print(f"All doors: {all_doors}")

        # Car is behind a random all_doors
        car_door = pick_random_door(all_doors)
        print(f"Car door: {car_door}")

        # Pick a random door
        picked_door = pick_random_door(all_doors)
        print(f"Picked door: {picked_door}")

        # Presenter knows which doors have goats
        goat_doors = get_goat_doors(all_doors, car_door)
        print(f"Goat doors: {goat_doors}")

        # Presenter shows you a goat door
        shown_goat_door = get_shown_goat_door(goat_doors, picked_door)
        print(f"Shown goat door: {shown_goat_door}")

        if swapping:
            # Swap the door you picked
            picked_door = get_swapped_door(all_doors, shown_goat_door,
                                           picked_door)
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


if __name__ == "__main__":
    main(False, 1000, 3)
