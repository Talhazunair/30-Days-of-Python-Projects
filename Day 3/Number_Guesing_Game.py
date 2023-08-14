import random
from art import text2art
art=text2art('Number Guesing Game')
print(art)
correct_number = random.randrange(0, 10)
life_line = 0
remaining_lifeline = 4

while (life_line < 4):
    try:
        life_line = life_line + 1
        remaining_lifeline = remaining_lifeline - 1
        get_user_input = int(input("Enter Number Between 1-10:"))

        if (get_user_input == correct_number):
            print(text2art("You Win"))
            break

        elif (get_user_input < correct_number):
            print(f"Please Enter Large Number    ========== Remaining Life Line {remaining_lifeline - 1}")

        elif (get_user_input > correct_number):
            print(f"Please Enter Small Number     ========== Remaining Life Line {remaining_lifeline - 1}")

        if (life_line == 3):
            print("----------------------Better Luck Next Time----------------------")
            print(text2art("Game Over"))
            break
    except:
        Exception(ValueError)
        print("Please Enter Number Only")