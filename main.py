import os
from CHfiles.HandlingFiles import load_file_decrypted, load_key, data_preparation_tuple, get_model_from_list,generate_key,save_data_with_encrypted

class AccountManager:
    """
    Class responsible for managing account-related operations such as
    displaying accounts, showing help options, and processing user instructions.
    """
    def __init__(self, key: str, filename: str = "myfile.txt"):
        """
        Initialize the AccountManager with the encryption key and filename.
        
        :param key: The encryption key for file operations.
        :param filename: The name of the file containing account data.
        """
        self.key = key
        self.filename = filename
        save_data_with_encrypted(filename,key)

    def display_accounts(self, instruction: str) -> None:
        """
        Decrypt the account data from file and display a filtered list based on the instruction.
        :param instruction: A string used to filter or search for accounts.
        """
        try:
            decrypted_data = load_file_decrypted(self.filename, self.key)
            accounts_tuple = data_preparation_tuple(decrypted_data)
            accounts_list = get_model_from_list(accounts_tuple, instruction)
            
            print("~~~~~~~~~~~~~~~~~")
            print("\n".join(accounts_list))
            print("~~~~~~~~~~~~~~~~~")
        except Exception as e:
            print(f"An error occurred while displaying accounts: {e}")

    def show_help(self) -> None:
        """
        Display the help options to guide the user.
        """
        help_message = (
            "- Enter [1] if you want to view all accounts\n"
            "- Enter [2] to add new data\n"
            "- Enter [3] to Extract all data without encryption\n"
            "- Enter [4] Get data from file"
        )
        print(help_message)

    def view_all_accounts(self) -> None:
        """
        Decrypt and display all account data.
        """
        try:
            data = load_file_decrypted(self.filename, self.key)
            print(data)
        except Exception as e:
            print(f"An error occurred while viewing all accounts: {e}")

    def add_new_data(self) -> None:
        """
        Placeholder for adding new account data.
        """
        print("entre data by this method"
              ": ':[name_of_account] [info1] [info2] [info3] ... [info(n)]'")
        text = input()
        save_data_with_encrypted(self.filename,self.key,"\n"+text)

    def Extract_all_data_without_encryption(self) -> None:
        filenamesaved = input("entre name file: ")
        try:
            data = load_file_decrypted(self.filename, self.key)
            with open(filenamesaved,'w') as file:
                file.write(data)
        except Exception as e:
            print(f"An error occurred while viewing all accounts: {e}")
        
    def Get_from_file(self):
        filename = input("entre name file: ")
        if not os.path.exists(filename):
            return None
        with open(filename,'r') as file:
            data = file.read()
        with open(self.filename,"w") as file:
            file.write(data)
        save_data_with_encrypted(self.filename,self.key)
        
    def process_instruction(self, instruction: str) -> None:
        """
        Process the user instruction and call the appropriate method.
        :param instruction: The user's input instruction.
        """
        self.display_accounts(instruction)
        
        if instruction == "0":
            self.show_help()
        elif instruction == "1":
            self.view_all_accounts()
        elif instruction == "2":
            self.add_new_data()
        elif instruction == "3":
            self.Extract_all_data_without_encryption()
        elif instruction == "4":
            self.Get_from_file()
        else:
            pass

def load_or_create_key(key_file: str = "secret.key") -> str:
    """
    Load the encryption key from a file if it exists,
    otherwise prompt the user to enter a key.
    
    :param key_file: The filename where the key is stored.
    :return: The encryption key as a string.
    """
    if not os.path.exists(key_file):
        key = input("Enter your key: ")
        generate_key(key)
        return key
    return load_key()

def main():
    """
    Main entry point of the application.
    Initializes the AccountManager and processes user instructions in a loop.
    """
    key = load_or_create_key()
    account_manager = AccountManager(key)

    while True:
        instruction = input(
            "Enter the account name or part of it\n"
            "You can type [0] if you want help options: "
        ).strip()
        account_manager.process_instruction(instruction)

if __name__ == "__main__":
    main()
