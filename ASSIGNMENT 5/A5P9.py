data = [{'a': 'one', 
         'b': 'two', 
         'c': 'three', 
         'd': 'four', 
         'e': 'five', 
         'f': 'six'}]

min_key = min(data[0], key=data[0].get)
print(f"The key with the minimum value is: {min_key}")