def reduce(s):
    stack = list()
    for i in s:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    return "".join(stack) if stack else "Empty string"

sample = input("Enter a string: ")
print(f"Input - {sample}")
print(f"Output - {reduce(sample)}")