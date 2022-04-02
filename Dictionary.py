
from sqlite3 import adapt


aList = [ 
            [11, 'Karan', 'Pune'], 
            [21, 'Devendra','Hyd'], 
            [101, 'Prachi','Pune']
        ]



aDictionary = { 
                'key': 'value',
                'marks' : 100,
                11 : ['Karan', 'Pune'], 
                21 : [21, 'Devendra','Hyd'], 
                101 : [101, 'Prachi','Pune'],
                True : "Some true value",
                True : "another true value",
                None : "value null"

            }

## ---------------------------------------

print(aDictionary)

##print(aDictionary[0])       #KeyError: 0  # we can not get element with index
print(aDictionary[11])       #['Karan', 'Pune']

print(aDictionary['key'])       # value
print(aDictionary['marks'])       # 100
print(aDictionary[True])       # 100
print(aDictionary[None])       # value null


#---------------------------------------------------

# Dictionary Methods

print(aDictionary)
print(aDictionary.items())  # To get all elements in the form of tuple enclosing list
print(aDictionary.keys())   # Prints only keys in the dictionary

# Update value of key
aDictionary["marks"] = 200
print(aDictionary["marks"])

aDictionary.update({'marks':201})
print(aDictionary['marks'])

aDictionary.update({'marks2':250, 'marks3':300}) # Insert / Update values
print(aDictionary)

print(aDictionary['marks'])
print(aDictionary.get('marks'))
# print(aDictionary['marks4'])  # KeyError: 'marks4'
print(aDictionary.get('marks4'))  # None (Avoiding error when key not available)
















