# Cryptography with Python: Caesar Cipher & ROT13

This repository contains Python implementations of two classic cryptographic techniques: **Caesar Cipher** and **ROT13**. Both are simple substitution ciphers that are fundamental to understanding classical cryptography.

## Ciphers Implemented

### 1. Caesar Cipher
The **Caesar Cipher** is a basic encryption technique where each letter in the plaintext is shifted by a fixed number (the "key") in the alphabet. For example, with a shift of 3, 'A' becomes 'D', 'B' becomes 'E', and so on.

#### Features:
- **Encryption & Decryption:** You can both encrypt and decrypt messages by adjusting the shift/key value.
- **Customizable Shift:** The shift can be any integer value, positive or negative.
- **Support for Upper and Lowercase:** The cipher works with both uppercase and lowercase letters, leaving non-alphabetic characters unchanged.

### 2. ROT13 Cipher
**ROT13** is a specific case of the Caesar Cipher where the shift is always 13. This makes ROT13 self-inverse, meaning applying ROT13 to an already encoded message will decode it.

#### Features:
- **No Key Required:** Since ROT13 uses a fixed shift of 13, there is no need to specify a key.
- **Symmetry:** Encrypting the same message twice with ROT13 returns the original message.

## Repository Structure

- **`cypher.py`:** Python script for the Caesar Cipher implementation. Includes functions to encrypt and decrypt text based on a given shift value.
- **`rot13.py`:** Python script for ROT13 implementation, a special case of Caesar Cipher with a fixed shift of 13.

### Example Usage

1. **Caesar Cipher Example:**
   ```python
   from caesarcypher import encrypt, decrypt

   # Encrypt with a shift of 3
   encrypted_text = encrypt("HELLO WORLD", 3)
   print(encrypted_text)  # Output: KHOOR ZRUOG

   # Decrypt with a shift of 3
   decrypted_text = decrypt("KHOOR ZRUOG", 3)
   print(decrypted_text)  # Output: HELLO WORLD
   ```

2. **ROT13 Example:**
   ```python
   from rot13 import rot13

   # Encrypt/Decrypt using ROT13
   cipher_text = rot13("HELLO WORLD")
   print(cipher_text)  # Output: URYYB JBEYQ

   # Apply ROT13 again to decrypt
   original_text = rot13(cipher_text)
   print(original_text)  # Output: HELLO WORLD
   ```

## How to Use

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/cryptography-python.git
   cd cryptography-python
   ```

2. **Run the Cipher Scripts:**
   You can run the individual cipher scripts or import the cipher functions into your own projects.
   ```bash
   python cypher.py
   python rot13.py
   ```

3. **Customize Shift (Caesar Cipher Only):**
   When using the Caesar Cipher, you can customize the shift by passing an integer (positive or negative) as the key.

## Prerequisites
- **Python 3.x** installed on your system. You can download it from [here](https://www.python.org/downloads/).

## Contributing
Feel free to contribute by adding new ciphers, improving the existing code, or fixing any bugs. Contributions are welcome through pull requests.

## License
This repository is licensed under the **MIT License**. You are free to use, modify, and distribute the code, but please provide appropriate credit.

## Contact
For any questions or suggestions, feel free to open an issue or reach out.
