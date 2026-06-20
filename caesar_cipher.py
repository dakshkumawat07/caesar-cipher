def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def brute_force(text):
    print("\nBrute Force - Trying all possible shifts:")
    print("-" * 50)
    for shift in range(1, 26):
        print(f"Shift {shift:2}: {decrypt(text, shift)}")
    print("-" * 50)

def main():
    print("=" * 50)
    print("Caesar Cipher Tool - Cybersecurity Project")
    print("=" * 50)

    while True:
        print("\n1. Encrypt")
        print("2. Decrypt")
        print("3. Brute Force Decrypt (unknown shift)")
        print("4. Exit")
        choice = input("\nChoose an option (1-4): ")

        if choice == "1":
            text = input("Enter text to encrypt: ")
            shift = int(input("Enter shift value (1-25): "))
            print(f"Encrypted: {encrypt(text, shift)}")

        elif choice == "2":
            text = input("Enter text to decrypt: ")
            shift = int(input("Enter shift value (1-25): "))
            print(f"Decrypted: {decrypt(text, shift)}")

        elif choice == "3":
            text = input("Enter encrypted text: ")
            brute_force(text)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
