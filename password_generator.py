import random
import string

def generate_password(length=12, use_digits=True, use_symbols=True):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    characters = letters

    if use_digits:
        characters += digits

    if use_symbols:
        characters += symbols

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("=" * 40)
    print("      Secure Password Generator")
    print("=" * 40)

    try:
        length = int(input("Enter password length: "))

        digits_choice = input("Include digits? (y/n): ").lower() == 'y'
        symbols_choice = input("Include symbols? (y/n): ").lower() == 'y'

        password = generate_password(length, digits_choice, symbols_choice)

        print("\nGenerated Password:")
        print(password)

    except ValueError:
        print("Please enter a valid number.")


if __name__ == "__main__":
    main()
