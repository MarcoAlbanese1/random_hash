import hashlib
import os

def random_hash():
    found = False
    for attempt in range(1000):
        # Generate random data
        random_data = os.urandom(16)  # 16 bytes for MD5 input
        # Create MD5 hash
        hash_obj = hashlib.md5(random_data)
        hex_digest = hash_obj.hexdigest()
        
        # Check for two leading zeroes
        if hex_digest.startswith('00'):
            print(f"Found matching hash after {attempt + 1} attempts: {hex_digest}")
            found = True
            return True

    if not found:
        print("No hash starting with '00' found after 1000 attempts.")
        return False