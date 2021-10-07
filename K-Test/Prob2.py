import sys
import json



def main():
    # Opening JSON file
    f = open(sys.argv[1],)
 
    # returns JSON object as a dict
    data = json.load(f)
    
    #print(data)
    splitKeys = sys.argv[2].split('/')

    #print( splitKeys )
    tempData = data
    try: 
        for index in range(len(splitKeys)):
            if type(tempData) is dict:
                if splitKeys[index] in tempData.keys():    
                    
                    #print('TempDATA before assigning:', tempData[splitKeys[index]])
                    tempData = tempData[splitKeys[index]]
                    #print('TempDATA after assigning:', tempData)
                else:
                    raise Exception("Key is not present in Object")
            else:
                raise Exception("Following Key is not present in Object :", tempData)        


        print (tempData)
    except Exception as e:
        print("An Error Cccurred : ", e)
        return       
    
	
	
 


if __name__ == "__main__":
    main()