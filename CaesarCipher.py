def caesar_cipher(text, shift, mode):
  """
  Encrypts or decrypts text using Caesar Cipher algorithm.

  Args:
      text: The text to encrypt or decrypt.
      shift: The number of positions to shift letters.
      mode: 'encrypt' or 'decrypt'.

  Returns:
      The encrypted or decrypted text.
  """
  result = ""
  for char in text:
    if char.isalpha():
      # Check uppercase or lowercase
      base = ord('A') if char.isupper() else ord('a')
      # Handle wrapping around the alphabet
      new_ord = ord(char) + shift if mode == 'encrypt' else ord(char) - shift
      new_ord = (new_ord - base) % 26 + base
      result += chr(new_ord)
    else:
      # Keep non-alphabetic characters
      result += char
  return result

def main():
  """
  Prompts user for input and performs encryption/decryption.
  """
  while True:
    print("Caesar Cipher")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
      text = input("Enter message to encrypt: ")
      shift = int(input("Enter shift value: "))
      encrypted_text = caesar_cipher(text, shift, 'encrypt')
      print("Encrypted message:", encrypted_text)
    elif choice == '2':
      text = input("Enter message to decrypt: ")
      shift = int(input("Enter shift value: "))
      decrypted_text = caesar_cipher(text, shift, 'decrypt')
      print("Decrypted message:", decrypted_text)
    elif choice == '3':
      break
    else:
      print("Invalid choice. Please try again.")

if __name__== "__main__":
  main()