sample = {"name": "Kelly", "age":25, "salary": 8000, "city": "New york"}
sample["location"] = sample.pop("city")  
print(sample)