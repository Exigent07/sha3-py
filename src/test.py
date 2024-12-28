from sha3 import sha3_256
import hashlib

hash_value_implementation = sha3_256("Testing")
print(f"[+] Implemented: {hash_value_implementation}")

sha = hashlib.sha3_256()
sha.update(b"Testing")
hash_value_lib = sha.hexdigest()
print(f"[+] Library: {hash_value_lib}")

print(f"[+] {"Passed" if hash_value_lib == hash_value_implementation else "Failed"}")