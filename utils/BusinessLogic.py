def DataPreparationTuple(adress):
    """
    Parses a file containing account credentials grouped under platform names 
    and returns a structured dictionary.

    Example Input:
    '''
    :steam
    gmail1@gmail.com password1 azeazeaea azeaze
    gmail2@gmail.com password2
    :riot
    gmail3@gmail.com password3
    ''' 

    Output:
    {
        "steam": [["gmail1@gmail.com", "password1", "azeazeaea", "azeaze"], ["gmail2@gmail.com", "password2"]],
        "riot": [["gmail3@gmail.com", "password3"]]
    }  
    """

    with open(adress, 'r', encoding='utf-8') as file:
        data = file.read()

    result = {}
    sections = data.strip().split(":")  
    
    for section in sections:
        lines = section.strip().split("\n")  #
        
        if not lines or len(lines[0].strip()) == 0:
            continue 
        
        platform = lines[0].strip() 
        
        accounts = []
        for line in lines[1:]:  
            parts = line.split()
            if parts:  
                accounts.append(parts)
        
        if platform in result:
            result[platform].extend(accounts)  
        else:
            result[platform] = accounts

    return result

def get_best_match(data, query):
    """
    Search for the best matching key in the dictionary based on character occurrences.

    :param data: Dictionary containing account data.
    :param query: Search term.
    :return: The best matching key and its associated data, or None if no match is found.
    """
    if not query:
        return data  
    
    match_scores = {key: 0 for key in data.keys()}

    for char in query.lower():
        for key in match_scores.keys():
            if char in key.lower():
                match_scores[key] += 1

    best_match = max(match_scores, key=match_scores.get, default=None)

    return {best_match: data[best_match]} if best_match and match_scores[best_match] > 0 else {}

def convert_data_format(data):
    result = []
    for platform, accounts in data.items():
        result.append(f":{platform}")
        for account in accounts:
            result.append(" ".join(account))  
        
        result.append("") 
    return "\n".join(result).strip()

def save_data(namefile,data):
    with open(namefile,'w') as file:
        file.write(data)



if __name__ == "__main__":
    a = {'gog': [['hjesxsjd@gmail.com', 'zDJHpFFpAw', 'd', 'i', 'y', 'k', 'l'], ['0deusfzm@gmail.com', 'qdbI6LnF8p', 'o', 'j', 'g', 's', 'n'], ['ye0ak369@yahoo.com', 'fVlfVFLjgU', 'v', 'p', 'q', 'c', 'p']], 'google': []}
    
    print(convert_data_format(a))