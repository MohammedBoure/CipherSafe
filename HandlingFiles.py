from CHfiles.EncryptionCH import *

def readfile(namefile):
    with open(namefile,'r') as file:
        return file.read()
    
def writefile(namefile,returntext):
    with open(namefile,'wb') as file:
        file.write(returntext)
        
        
def LoadFileDecrypted(namefile,key):
    data = readfile(namefile)
    try:
        return decrypt_text(data[5:],key)
    except:
        return None
    
    
def SaveDataWithEncryped(namefile,key):
    data = readfile(namefile)
    vale = data[:5]
    if not vale == "hello":
        generate_key(key)
        writefile(namefile,b"hello\n"+encrypt_text(data,key))
        
"""STEAM gamer123@gmail.com XyZpLq19&Ws
:RIOTGAMES player456@yahoo.com AbCdEf23#Kt  to :
[['STEAM', 'gamer123', 'XyZpLq19\n'], ['RIOTGAMES', 'player456', 'AbCdEf23#Kt']]"""
def DataPreparationTuple(data):
    listdata = data.split(":")
    listdata = [i.split(" ") for i in listdata]
    return listdata

def GetModelFromList(listdata, var):
    listmodels = [[i[0], 0] for i in listdata]

    for char in var.lower():
        for model in listmodels:
            if char in model[0].lower():
                model[1] += 1

    chosen_model = max(listmodels, key=lambda x: x[1], default=None)

    if chosen_model:
        for item in listdata:
            if item[0] == chosen_model[0]:
                return item

    return None 


if __name__ == "__main__":
    #tests:
    SaveDataWithEncryped("myfile.txt",b"eif1nzzXWilSJBeRJclHK7TnXjMoDfpeJf_DZuCCwLo=")
    print()
    
    x = (DataPreparationTuple(LoadFileDecrypted("myfile.txt",b"eif1nzzXWilSJBeRJclHK7TnXjMoDfpeJf_DZuCCwLo=")))
    while True:
        a = input(">>> ")
        print(GetModelFromList(x,a))
    
    
    