import base64

def int_to_fernet_key(num, val):
    num_bytes = num.to_bytes(val, 'big')
    return base64.urlsafe_b64encode(num_bytes).decode("utf-8")  


def simple_hash_64(input_string):
    hash_value = 0xcbf29ce484222325  
    fnv_prime = 0x100000001b3  

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
    
    test_string = input("Enter your text and you are hashing\n"
                            "Like this : hash32 [text]\n"
                            "            hash64 [text]\n"
                            "            hash128 [text]\n"
                            "            hash256 [text]\n>")
    
    while True:
        
        if "hash32" in test_string:
            test_string = test_string.split(" ")[1]
            hash32 = simple_hash_32(test_string)
            print(hash32)
        elif "hash64" in test_string:
            test_string = test_string.split(" ")[1]
            hash64 = simple_hash_64(test_string)
            print(hash64)
        elif "hash128" in test_string:
            test_string = test_string.split(" ")[1]
            hash128 = simple_hash_128(test_string)
            print(hash128)
        elif "hash256" in test_string:
            test_string = test_string.split(" ")[1]
            hash256 = simple_hash_256(test_string)
            print(hash256)

        test_string = input(">")
