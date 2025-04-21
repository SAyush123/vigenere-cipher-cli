# vigenere-cipher-cli
A Python-based command-line tool to encrypt and decrypt messages using the Vigenère cipher.
# 🔐 Vigenère Cipher - Python CLI App

A simple command-line tool to encrypt and decrypt messages using the **Vigenère Cipher**, built with core Python.

---

## 📌 Features

- Encrypt or decrypt using a user-provided key.
- Ignores non-alphabet characters (spaces, punctuation).
- Simple CLI interface — no external libraries required.
- Beginner-friendly logic using loops, strings & modular arithmetic.

---

## 🧠 How It Works

Each letter of the message is shifted using a letter from the repeating key.

```python
new_index = (index_of_char + offset_from_key * direction) % 26
```

- For **encryption**: `direction = +1`
- For **decryption**: `direction = -1`

---

3. Example:
   ```
   Enter the message you want to encrypt/decrypt: hello world
   Enter the key: python
   Press (E) if you want to Encrypt or (D) if you want to Decrypt: E
   Encrypted message: ulaml xzdbm
   ```

---

## 🧾 Code Snippet

```python
def vigenere_cipher(message, key, direction=1):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''
    key_index = 0

    for char in message.lower():
        if not char.isalpha():
            final_message += char
        else:
            key_char = key[key_index % len(key)].lower()
            key_index += 1

            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]

    return final_message
```

👉 Full code in [`vigenere.py`](./vigenere.py)

---

## 🛠️ Requirements

- Python 3.x  
- Works on Windows, macOS, and Linux

---

## 📂 Folder Structure

```
vigenere-cipher/
├── vigenere.py
└── README.md
```

---

## 📣 Author

Made with 💻 by [Ayush Sharma]  
🔗 [your-portfolio-link.com](https://www.linkedin.com/in/ayush-s-5b3a18336/) | [GitHub](https://github.com/SAyush123) | [LinkedIn]((https://www.linkedin.com/in/ayush-s-5b3a18336/))

---

