from CHfiles.EncryptionCH import *
import os

# Read the content of the file
def read_file(namefile):
    if not os.path.exists(namefile):
        open(namefile,"w")
    with open(namefile, 'r') as file:
        return file.read()


# Write encrypted content back to the file
def write_file(namefile, return_text):
    with open(namefile, 'wb') as file:
        file.write(return_text)


# Decrypt and return the data, excluding the "hello" prefix
def load_file_decrypted(namefile, key):
    data = read_file(namefile)
    try:
        return decrypt_text(data[5:], key)
    except Exception as e:
        return ""
    
# Ensure the data starts with 'hello' before encrypting it
def save_data_with_encrypted(namefile, key,text=""):
    data = load_file_decrypted(namefile,key)
    if text:
        generate_key(key)
        write_file(namefile, b"hello\n" + encrypt_text(data+text, key))
        
    data = read_file(namefile)
    if not data.startswith("hello"):
        write_file(namefile, b"hello\n" + encrypt_text(data+text, key))
        
        
# Convert the data into a list of lists
def data_preparation_tuple(data):
    listdata = data.split(":")
    listdata = [i.split(" ") for i in listdata]
    return listdata


# Count character matches between the input and the models
def get_model_from_list(listdata, var):
    listmodels = [[i[0], 0] for i in listdata]
    for char in var.lower():
        for model in listmodels:
            if char in model[0].lower():
                model[1] += 1

    # Find the model with the highest match
    chosen_model = max(listmodels, key=lambda x: x[1], default=None)

    if chosen_model:
        for item in listdata:
            if item[0] == chosen_model[0]:
                return item
    return None 

if __name__ == "__main__":
    save_data_with_encrypted("myfile.txt", b"eif1nzzXWilSJBeRJclHK7TnXjMoDfpeJf_DZuCCwLo=")

    decrypted_data = load_file_decrypted("myfile.txt", b"eif1nzzXWilSJBeRJclHK7TnXjMoDfpeJf_DZuCCwLo=")
    if decrypted_data:
        x = data_preparation_tuple(decrypted_data)
        while True:
            a = input(">>> ")
            result = get_model_from_list(x, a)
            print(result)
