import base64

def int_to_fernet_key(num,val):
    num_bytes = num.to_bytes(val, 'big')  # Ensure it's 32 bytes
    return base64.urlsafe_b64encode(num_bytes)

# This function implements a simple 64-bit hash using the FNV-1a algorithm.
# It does not rely on any external libraries.
def simple_hash_64(input_string):
    # FNV-1a 64-bit offset basis
    hash_value = 0xcbf29ce484222325  
    # FNV-1a 64-bit prime
    fnv_prime = 0x100000001b3  

    # Iterate through each character in the input string
    for char in input_string:
        # XOR the lower 8 bits of the hash with the current character's ASCII code
        hash_value ^= ord(char)
        # Multiply by the FNV prime and ensure we stay within 64 bits by masking
        hash_value = (hash_value * fnv_prime) & 0xFFFFFFFFFFFFFFFF

    return int_to_fernet_key(hash_value,8)

def simple_hash_32(input_string):
    hash_value = 0x811c9dc5
    fnv_prime = 0x01000193
    mask = 0xFFFFFFFF

    for char in input_string:
        hash_value ^= ord(char)
        hash_value = (hash_value * fnv_prime) & mask

    return int_to_fernet_key(hash_value,4)

def simple_hash_128(input_string):
    hash_value = 0x6c62272e07bb014262b821756295c58d
    fnv_prime = 0x1000000000000000000013B
    mask = (1 << 128) - 1

    for char in input_string:
        hash_value ^= ord(char)
        hash_value = (hash_value * fnv_prime) & mask

    return int_to_fernet_key(hash_value,16)

def simple_hash_256(input_string):
    hash_value = 10002925795805258090707096862062570483709279601424119394522528450174120299367
    fnv_prime = 374144419156711147060143317175368453031918731002211
    mask = (1 << 256) - 1

    for char in input_string:
        hash_value ^= ord(char)
        hash_value = (hash_value * fnv_prime) & mask

    return int_to_fernet_key(hash_value,32)




if __name__ == "__main__":
    test_string = "Hello, World!"
    
    hash32 = simple_hash_32(test_string)
    hash64 = simple_hash_64(test_string)
    hash128 = simple_hash_128(test_string)
    hash256 = simple_hash_256(test_string)

    print(f"32-bit hash for '{test_string}': {hash32}")
    print(f"64-bit hash for '{test_string}': {hash64}")
    print(f"128-bit hash for '{test_string}': {hash128}")
    print(f"256-bit hash for '{test_string}': {hash256}")
    
