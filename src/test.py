from sha3 import sha3_256, sha3_224, sha3_384
import hashlib
import timeit

test_string = "Testing"
test_bytes = test_string.encode()

print("[*] Testing SHA3-256:")
def implemented_sha3_256():
    return sha3_256(test_bytes)

def library_sha3_256():
    sha = hashlib.sha3_256()
    sha.update(test_bytes)
    return sha.hexdigest()

implemented_hash_256 = implemented_sha3_256()
library_hash_256 = library_sha3_256()
print(f"[+] Hash Output (Implemented): {implemented_hash_256}")
print(f"[+] Hash Output (Library): {library_hash_256}")
if implemented_hash_256 == library_hash_256:
    print("[+] Test Passed: SHA3-256 outputs match.")
else:
    print("[-] Test Failed: SHA3-256 outputs do not match.")

implemented_time_256 = timeit.timeit(implemented_sha3_256, number=10000)
library_time_256 = timeit.timeit(library_sha3_256, number=10000)

print(f"[+] Implemented SHA3-256 time: {implemented_time_256:.6f} seconds")
print(f"[+] Library SHA3-256 time: {library_time_256:.6f} seconds")
print(f"[*] Efficiency Ratio (Implemented/Library): {implemented_time_256/library_time_256:.2f}")

print("\n[*] Testing SHA3-224:")
def implemented_sha3_224():
    return sha3_224(test_bytes)

def library_sha3_224():
    sha = hashlib.sha3_224()
    sha.update(test_bytes)
    return sha.hexdigest()

implemented_hash_224 = implemented_sha3_224()
library_hash_224 = library_sha3_224()
print(f"[+] Hash Output (Implemented): {implemented_hash_224}")
print(f"[+] Hash Output (Library): {library_hash_224}")
if implemented_hash_224 == library_hash_224:
    print("[+] Test Passed: SHA3-224 outputs match.")
else:
    print("[-] Test Failed: SHA3-224 outputs do not match.")

implemented_time_224 = timeit.timeit(implemented_sha3_224, number=10000)
library_time_224 = timeit.timeit(library_sha3_224, number=10000)

print(f"[+] Implemented SHA3-224 time: {implemented_time_224:.6f} seconds")
print(f"[+] Library SHA3-224 time: {library_time_224:.6f} seconds")
print(f"[*] Efficiency Ratio (Implemented/Library): {implemented_time_224/library_time_224:.2f}")

print("\n[*] Testing SHA3-384:")
def implemented_sha3_384():
    return sha3_384(test_bytes)

def library_sha3_384():
    sha = hashlib.sha3_384()
    sha.update(test_bytes)
    return sha.hexdigest()

implemented_hash_384 = implemented_sha3_384()
library_hash_384 = library_sha3_384()
print(f"[+] Hash Output (Implemented): {implemented_hash_384}")
print(f"[+] Hash Output (Library): {library_hash_384}")
if implemented_hash_384 == library_hash_384:
    print("[+] Test Passed: SHA3-384 outputs match.")
else:
    print("[-] Test Failed: SHA3-384 outputs do not match.")

implemented_time_384 = timeit.timeit(implemented_sha3_384, number=10000)
library_time_384 = timeit.timeit(library_sha3_384, number=10000)

print(f"[+] Implemented SHA3-384 time: {implemented_time_384:.6f} seconds")
print(f"[+] Library SHA3-384 time: {library_time_384:.6f} seconds")
print(f"[*] Efficiency Ratio (Implemented/Library): {implemented_time_384/library_time_384:.2f}")
