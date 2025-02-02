def simple_hash_64(input_str):
    hash_value = 0x6f6e6c617267656e  
    prime = 0x9e3779b97f4a7c15 
    
    for char in input_str:
        char_code = ord(char)
        
        hash_value = (hash_value << 7) | (hash_value >> (64 - 7))
        hash_value ^= char_code * prime
        hash_value &= 0xFFFFFFFFFFFFFFFF 
    
    return f"{hash_value:016x}"
if __name__=="__main__":
    test_input = "hello"
    print(f"'{test_input}': {simple_hash_64(test_input)}")

    test_input2 = "hellp"
    print(f"'{test_input2}': {simple_hash_64(test_input2)}")