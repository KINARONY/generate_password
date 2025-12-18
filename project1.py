import random
import string

def generate_password(length):
    все_символы = string.ascii_lowercase + string.digits + string.punctuation
    password = ""
    for _ in range(length):
        password += random.choice(все_символы)
    return password

варианты = string.ascii_lowercase + string.digits + string.punctuation
import random
random.choice(варианты)
пароль = ""

import string

def check_password_strength(password):
    has_letter = any(char.isalpha() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    if len(password) == 8 and has_letter and not has_digit and not has_special:
        return "Слабый"
    elif len(password) == 8 and has_letter and has_digit and not has_special:
        return "Средний"
    elif len(password) >= 10 and has_letter and has_digit and has_special:
        return "Сильный"
    else:
        return "Неопределённая сила пароля"

def main():
    try:
        length = int(input("Введите длину пароля: "))
        password = generate_password(length)
        print(f"Сгенерированный пароль: {password}")
        strength = check_password_strength(password)
        print(f"Сила пароля: {strength}")
    except ValueError:
        print("Ошибка: введите целое число.")

if __name__ == "__main__":
    main()
