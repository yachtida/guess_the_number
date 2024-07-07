import sys
import random

args = sys.argv
limit = int(args[1]) if len(args) > 1 else 9999

sys.stdout.buffer.write(b"lets play the game \n")
sys.stdout.buffer.write(b"enter min number")
sys.stdout.flush()

min = sys.stdin.buffer.readline().decode().strip()
while int(min) < 0:
    sys.stdout.buffer.write(b"enter min number. min number is bigger than 0")
    sys.stdout.flush()
    min = sys.stdin.buffer.readline().decode().strip()

sys.stdout.buffer.write(b"enter max number. max number is bigger than min number")
sys.stdout.flush()

max = sys.stdin.buffer.readline().decode().strip()
while int(min) >= int(max):
    sys.stdout.buffer.write(b"max number is bigger than min number")
    sys.stdout.flush()
    max = sys.stdin.buffer.readline().decode().strip()


random = random.randint(int(min), int(max))

user_guess = -1
counter = 0
while user_guess != random:
    if counter == limit:
        sys.stdout.buffer.write(b"you reached the limit")
        sys.stdout.flush()
        break
    sys.stdout.buffer.write(b"guess the number")
    sys.stdout.flush()
    user_guess = int(sys.stdin.buffer.readline().decode().strip())
    counter += 1
    if user_guess < random:
        sys.stdout.buffer.write(b"too low")
        sys.stdout.flush()
    elif user_guess > random:
        sys.stdout.buffer.write(b"too high")
        sys.stdout.flush()
    else:
        sys.stdout.buffer.write(b"you got it")
        sys.stdout.flush()
        break
