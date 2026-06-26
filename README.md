# 🔒 SHA-256 Hash Generator

A simple command-line **SHA-256 Hash Generator** built with **Python** using the built-in `hashlib` library.

This project allows users to generate a **SHA-256 cryptographic hash** for either plain text or a file. It demonstrates how hashing works and how SHA-256 can be used to verify data integrity.

---

## ✨ Features

* 🔤 Generate SHA-256 hash for plain text.
* 📄 Generate SHA-256 hash for files.
* ⚡ Processes large files efficiently using chunk-based reading.
* ❌ Handles invalid file paths with error messages.
* 💻 Simple command-line interface.

---

## 🛠️ Technologies Used

* Python 3.x
* hashlib (Built-in Python Library)
* SHA-256 Cryptographic Hash Algorithm

---

## 📂 Project Structure

```text
SHA256-Hash-Generator/
│
├── main.py          # Main application
└── README.md
```

---

## 📥 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/SHA256-Hash-Generator.git
cd SHA256-Hash-Generator
```

### 2. (Optional) Create a Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

No additional packages are required because `hashlib` is included with Python.

---

## ▶️ Running the Program

```bash
python main.py
```

---

## 📖 How It Works

When the program starts, choose one of the following options:

* **text** → Generate the SHA-256 hash of a text string.
* **file** → Generate the SHA-256 hash of a file by providing its path in the format:

```text
file://C:/Users/Username/Documents/example.pdf
```

The program reads the file in small chunks, making it efficient even for larger files.

---

## 💻 Example

### Hashing Text

```text
Enter 'text' for text input or 'file' for file path:
text

Enter your text:
Hello World

SHA-256 hash:
a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e
```

### Hashing a File

```text
Enter 'text' for text input or 'file' for file path:
file

Enter the file path (starting with 'file://'):
file://C:/Users/User/Desktop/test.txt

SHA-256 hash:
4a44dc15364204a80fe80e9039455cc1608281820fe2b24f1e5233d6f8b4c2b3
```

---

## 🔐 About SHA-256

SHA-256 (Secure Hash Algorithm 256-bit) is a cryptographic hash function that produces a fixed-length **256-bit (64-character hexadecimal)** hash.

Key characteristics:

* One-way function (cannot be reversed)
* Deterministic (same input always produces the same output)
* Fixed-length output
* Collision-resistant
* Commonly used for integrity verification, digital signatures, password storage (with salting), and blockchain technologies

Unlike encryption, hashing is **not reversible**.

---

## 📌 Future Improvements

* Compare two files using their SHA-256 hashes.
* Support multiple hashing algorithms (MD5, SHA-1, SHA-512).
* Drag-and-drop file support.
* GUI version using Tkinter or PyQt.
* Save generated hashes to a text file.

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

Developed by **Harshal Kapse**.
