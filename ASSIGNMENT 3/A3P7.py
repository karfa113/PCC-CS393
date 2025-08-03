from math import ceil

def fare(source, dest):
    dist = 0
    stations = ["TH", "GA", "IC", "HA", "TE", "LU", "NI", "CA"]
    path = [800, 600, 750, 900, 1400, 1200, 1100, 1500]
    if source == dest:
        print("Invalid Input")
        exit()
    start = stations.index(source)
    end = stations.index(dest)
    if start < end:
        dist += sum(path[start:end])
    else:
        dist += sum(path[start:])
        dist += sum(path[:end])
    
    cpm = 5.0 / 1000
    fare = ceil(cpm * dist)
    print(f"Distance - {dist} Meter \nFare - {fare} INR")

st = {
    "TH" : "THANERAILWAYSTN", 
    "GA" : "GAONDEVI", 
    "IC" : "ICEFACTROY",
    "HA" : "HARINIWASCIRCLE",
    "TE" : "TEENHATHNAKA", 
    "LU" : "LUISWADI",
    "NI" : "NITINCOMPANYJUNCTION", 
    "CA" : "CADBURRYJUNCTION"
    }
for i in st:
    print(f"{i} : {st[i]}")

ss = input("Enter source station: ").upper()
ds = input("Enter destination station: ").upper()
fare(ss, ds)