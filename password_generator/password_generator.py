import string
import random


def main():
    password_length = get_length()
    password_difficulty = get_difficulty()
    password = generate_password(password_length, password_difficulty)
    print(f"Generated Password: {password}")


def get_length():
    while True:
        desired_length = get_int(
            "How Long Should the Password be? [Hint: must be greater than or equal to 8]: "
        )
        if desired_length < 8:
            print("Length must be 8 or more characters!")
        else:
            return desired_length


def get_difficulty():
    while True:
        desired_difficulty = get_int(
            "Difficulty Level? [Hint: 1-easy, 2-hard, 3-impossible]: "
        )
        if desired_difficulty > 0 and desired_difficulty < 4:
            return desired_difficulty
        else:
            print(
                "Values allowed are 1, 2, and 3 only! [Hint: 1-easy, 2-hard, 3-impossible]"
            )


def get_int(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Value entered must be a number.")


def generate_password(length, difficulty):
    sequence_symbols = ["l", "u", "n", "s"]
    sequence = generate_sequence(sequence_symbols, length, difficulty)
    password = sequence_to_password(sequence)
    return password


def generate_sequence(symbols, length, difficulty):
    while True:
        holder = []
        count_l = 0
        count_u = 0
        count_n = 0
        count_s = 0
        for i in range(length):
            random_symbol = random.choice(symbols)
            holder.append(random_symbol)
        for item in holder:
            if item == "l":
                count_l += 1
            elif item == "u":
                count_u += 1
            elif item == "n":
                count_n += 1
            elif item == "s":
                count_s += 1
        if difficulty == 1 and count_s == 0 and (count_l + count_u) / length >= 0.5:
            return holder
        elif (
            difficulty == 2
            and count_s > 0
            and count_l > 0
            and count_u > 0
            and count_n > 0
        ):
            return holder
        elif (
            difficulty == 3
            and count_s >= 0.3 * length
            and count_l >= 0.1 * length
            and count_u >= 0.1 * length
        ):
            return holder


def sequence_to_password(sequence):
    lowercase_letters = list(string.ascii_lowercase)
    uppercase_letters = list(string.ascii_uppercase)
    numbers = list(string.digits)
    special_characters = list(string.punctuation)
    password = ""
    for character in sequence:
        temp = ""
        if character == "l":
            temp = random.choice(lowercase_letters)
            password += temp
        elif character == "u":
            temp = random.choice(uppercase_letters)
            password += temp
        elif character == "n":
            temp = random.choice(numbers)
            password += temp
        elif character == "s":
            temp = random.choice(special_characters)
            password += temp
    return password


if __name__ == "__main__":
    main()
