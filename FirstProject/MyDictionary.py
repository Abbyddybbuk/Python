my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}
print(my_dict["key2"])  # Output the value associated with 'key2'

prices = {"apple": 0.5, "banana": 0.3, "orange": 0.8}
print(prices["banana"])  # Output the price of banana

myMixedDict = {"name": "Alice", "age": 30, "is_student": False, "grades": [85, 90, 95], "subjects": {"math": "A", "science": "B+"}}
print(myMixedDict["grades"])  # Output the list of grades   
print(myMixedDict["subjects"]["science"])  # Output the grade in science
myMixedDict["address"] = "123 Main St"  # Add a new key-value pair
print(myMixedDict)  # Output the updated dictionary 

print(myMixedDict.keys())
print(myMixedDict.values())
myMixedDict.pop("is_student")  # Remove the key 'is_student'    
print(myMixedDict)  # Output the dictionary after removing 'is_student'