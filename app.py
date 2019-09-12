import random

room = 0
guess_count = 0
guess_limit = 3
try:
    for room in range(100):
        while guess_count < guess_limit:
            secret_wall = random.randint(1, 3)
            guess = int(input("Guess: "))
            guess_count += 1
            if guess > 4 or guess < 1:
                print("zła liczba")
            if guess == secret_wall:
                guess_count = 0
                print("Brawo idziesz dalej")
                room += 1

        else:
            print("niestety zostajesz w tym pokoju na zawsze")
            break
except ValueError:w
    print("Miała być liczba !!")

print(f"Jesteś w pokoju {room + 1}")
