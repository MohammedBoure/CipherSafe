def DataPreparationTuple(data):
    """
    '''
    :steam
    gmail1@gmail.com password1 azeazeaea azeaze
    gmail2@gmail.com password2
    :riot
    gmail3@gmail.com password3
    ''' 
    to:
    {
        "steam":[["gmail1@gmail.com","password1"]["gmail2@gmail.com","password2"]],
        "riot":[["gmail3@gmail.com","password3"]]
    }  
    """
    result = {}

    sections = data.strip().split(":") 
    
    for section in sections:
        lines = section.strip().split("\n")  
        if not lines or len(lines) < 2:
            continue
        
        platform = lines[0].strip() 
        accounts = [line.split(maxsplit=1) for line in lines[1:] if line]
        
        formatted_accounts = []
        for account in accounts:
            if len(account) == 2:
                email, rest = account
                credentials = rest.split()
                formatted_accounts.append([email] + credentials)
            else:
                formatted_accounts.append(account)
            
        if platform in result:
            result[platform].extend(formatted_accounts)
        else:
            result[platform] = formatted_accounts
    
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
        for account in accounts:
            result.append(f":{platform}")  
            result.append(" ".join(account))
    return "\n".join(result)




if __name__ == "__main__":
    accounts_data = {
    "steam": [["gmail1@gmail.com", "password1"], ["gmail2@gmail.com", "password2"]],
    "riot": [["gmail3@gmail.com", "password3", "password4"]],
    "epicgames": [["gmail4@gmail.com", "password5"]],
    "steeam": [["gmail5@gmail.com", "password6"]],
    }
    query = "ste"
    results = get_best_match(accounts_data, query)

    print(results)