sample = {'a': 100, 'b': 200, 'c': 300}
ispresent = False

for i in sample:
    if(sample[i] == 200):
        ispresent = True
        break

print("Present" if ispresent else "Not Present")