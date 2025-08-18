sample = {'a': 100, 'b': 200, 'c': 300}
ispresent = False

if 200 in sample.values():
    ispresent = True

print("Present" if ispresent else "Not Present")