import hashlib

def hash_with_sha256(data):
  if isinstance(data, str):
    # Encode text input 
    encoded_data = data.encode()
    hasher = hashlib.sha256(encoded_data)
    return hasher.hexdigest()
  elif isinstance(data, str) and data.startswith("file://"):
    # Handle file input
    try:
      with open(data[7:], 'rb') as f:
        # Read file content
        hasher = hashlib.sha256()
        for chunk in iter(lambda: f.read(4096), b''):
          hasher.update(chunk)
        return hasher.hexdigest()
    except FileNotFoundError:
      print("Error: File not found!")
      return None
    except Exception as e:
      print(f"Error processing file: {e}")
      return None
  else:
    print("Invalid input type. Please provide text or a file path starting with 'file://'")
    return None

while True:
  choice = input("Enter 'text' for text input or 'file' for file path: ").lower()
  if choice == 'text':
    user_input = input("Enter your text: ")
    hash_value = hash_with_sha256(user_input)
    print("SHA-256 hash:", hash_value)
  elif choice == 'file':
    file_path = input("Enter the file path (starting with 'file://'): ")
    hash_value = hash_with_sha256(file_path)
    if hash_value:
      print("SHA-256 hash:", hash_value)
  else:
    print("Invalid choice. Please try again.")
  break
