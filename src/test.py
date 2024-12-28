from sha3 import sha3_256, sha3_224, sha3_384
import hashlib

test_string = "Testing"
test_bytes = test_string.encode()

hash_value_implementation = sha3_256(test_bytes)
print(f"[+] Implemented: {hash_value_implementation}")

sha = hashlib.sha3_256()
sha.update(test_bytes)
hash_value_lib = sha.hexdigest()
print(f"[+] Library: {hash_value_lib}")

# Compare results
if hash_value_lib == hash_value_implementation:
    print("[+] Test Passed: Both hashes match.")
else:
    print("[!] Test Failed: Hashes do not match.")

print("\nTesting SHA3-224:")
hash_value_implementation_224 = sha3_224(test_bytes)
sha224 = hashlib.sha3_224()
sha224.update(test_bytes)
hash_value_lib_224 = sha224.hexdigest()
print(f"[+] Implemented: {hash_value_implementation_224}")
print(f"[+] Library: {hash_value_lib_224}")
if hash_value_lib_224 == hash_value_implementation_224:
    print("[+] Test Passed: Both SHA3-224 hashes match.")
else:
    print("[!] Test Failed: SHA3-224 hashes do not match.")

print("\nTesting SHA3-384:")
hash_value_implementation_384 = sha3_384(test_bytes)
sha384 = hashlib.sha3_384()
sha384.update(test_bytes)
hash_value_lib_384 = sha384.hexdigest()
print(f"[+] Implemented: {hash_value_implementation_384}")
print(f"[+] Library: {hash_value_lib_384}")
if hash_value_lib_384 == hash_value_implementation_384:
    print("[+] Test Passed: Both SHA3-384 hashes match.")
else:
    print("[!] Test Failed: SHA3-384 hashes do not match.")
