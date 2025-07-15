cookies = int(input("Enter the number of cookies: "))

box = int(cookies / 24)
cookies_left = int(cookies % 24)
container = int(box / 75)
box_left = int(box % 75)

print(f"Total number of boxes: {box}")
print(f"Total cookies left: {cookies_left}")
print(f"Total number of containers: {container}")
print(f"Total boxes left: {box_left}")