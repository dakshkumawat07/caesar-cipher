from collections import Counter


def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


def brute_force(ciphertext):
    print("\n" + "=" * 50)
    print("BRUTE FORCE RESULTS")
    print("=" * 50)

    for shift in range(26):
        decrypted = decrypt(ciphertext, shift)
        print(f"Shift {shift:2}: {decrypted}")


def frequency_attack(ciphertext):
    letters = [char.upper() for char in ciphertext if char.isalpha()]

    if not letters:
        print("No alphabetic characters found.")
        return

    frequencies = Counter(letters)
    most_common_letter = frequencies.most_common(1)[0][0]

    guessed_shift = (ord(most_common_letter) - ord('E')) % 26

    print("\n" + "=" * 50)
    print("FREQUENCY ANALYSIS")
    print("=" * 50)
    print(f"Most common letter: {most_common_letter}")
    print(f"Guessed shift: {guessed_shift}")
    print(f"Possible plaintext:\n{decrypt(ciphertext, guessed_shift)}")


def text_statistics(text):
    total_chars = len(text)
    letters = sum(c.isalpha() for c in text)
    digits = sum(c.isdigit() for c in text)
    spaces = sum(c.isspace() for c in text)

    print("\n" + "=" * 50)
    print("TEXT STATISTICS")
    print("=" * 50)
    print(f"Total Characters : {total_chars}")
    print(f"Letters          : {letters}")
    print(f"Digits           : {digits}")
    print(f"Spaces           : {spaces}")


def save_result(content):
    with open("results.txt", "a", encoding="utf-8") as file:
        file.write(content + "\n")

    print("Result saved to results.txt")


def get_shift():
    while True:
        try:
            shift = int(input("Enter shift value (0-25): "))
            return shift % 26
        except ValueError:
            print("Please enter a valid number.")


def main():
    while True:
        print("\n" + "=" * 50)
        print("CAESAR CIPHER TOOL")
        print("=" * 50)
        print("1. Encrypt Text")
        print("2. Decrypt Text")
        print("3. Brute Force Attack")
        print("4. Frequency Analysis Attack")
        print("5. Text Statistics")
        print("6. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            text = input("Enter plaintext: ")
            shift = get_shift()

            encrypted = encrypt(text, shift)

            print(f"\nEncrypted Text:\n{encrypted}")

            save_result(
                f"[ENCRYPT] Shift={shift} | Input={text} | Output={encrypted}"
            )

        elif choice == "2":
            text = input("Enter ciphertext: ")
            shift = get_shift()

            decrypted = decrypt(text, shift)

            print(f"\nDecrypted Text:\n{decrypted}")

            save_result(
                f"[DECRYPT] Shift={shift} | Input={text} | Output={decrypted}"
            )

        elif choice == "3":
            text = input("Enter ciphertext: ")
            brute_force(text)

        elif choice == "4":
            text = input("Enter ciphertext: ")
            frequency_attack(text)

        elif choice == "5":
            text = input("Enter text: ")
            text_statistics(text)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
