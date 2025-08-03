from math import ceil

def fare(source, dest):
    stations = [
        "BWN", "GRP", "SKG", "PLAE", "RSLR", "NMF", "MYM", "BGF", "DBP", "BOI",
        "BCGM", "SLG", "PDA", "KHN", "TLO", "MUG", "ADST", "BDC", "HGY", "CNS",
        "CGR", "MUU", "BHR", "BBAE", "SHE", "SRP", "RIS", "KOG", "HMZ", "UPA",
        "BLY", "BEQ", "LLH", "HWH"
    ]

    path = [
        11000, 4300, 3700, 3900, 3100, 2900, 4600, 2900, 3600, 2800, 2300, 2000,
        1800, 2600, 3000, 2300, 4200, 4500, 4400, 2500, 1900, 1900, 2600, 1800,
        2300, 2700, 1900, 1800, 1800, 1700, 1600, 1400, 4700
    ]

    if source == dest:
        print("Invalid input: source and destination are the same.")
        return

    try:
        start = stations.index(source)
        end = stations.index(dest)
    except ValueError:
        print("Invalid station code entered.")
        return

    if start < end:
        dist = sum(path[start:end])
    else:
        dist = sum(path[end:start])

    if dist <= 15000:
        fare = 5
    elif dist <= 45000:
        fare = 10
    elif dist <= 75000:
        fare = 15
    elif dist <= 150000:
        fare = 20
    else:
        fare = ceil(20 + ((dist - 150000) / 15000)) * 5  

    print(f"\nTotal Distance: {dist} meters (~{dist / 1000:.2f} km)")
    print(f"Approximate Fare: ₹{fare}")

st = {
    "HWH": "Howrah Junction",       "LLH": "Liluah",              "BEQ": "Belur",
    "BLY": "Bally",                 "UPA": "Uttarpara",           "HMZ": "Hind Motor",
    "KOG": "Konnagar",              "RIS": "Rishra",              "SRP": "Serampore",
    "SHE": "Seoraphuli Junction",   "BBAE": "Baidyabati",         "BHR": "Bhadreshwar",
    "MUU": "Mankundu",              "CGR": "Chandan Nagar",       "CNS": "Chuchura",
    "HGY": "Hooghly",               "BDC": "Bandel Junction",     "ADST": "Adi Saptagram",
    "MUG": "Magra",                 "TLO": "Talandu",             "KHN": "Khanyan",
    "PDA": "Pundooah",              "SLG": "Simlagarh",           "BCGM": "Bainchigram",
    "BOI": "Bainchi",               "DBP": "Debipur",             "BGF": "Bagila",
    "MYM": "Memari",                "NMF": "Nimo",                "RSLR": "Rasulpur",
    "PLAE": "Palsit",               "SKG": "Saktigarh",           "GRP": "Gangpur",
    "BWN": "Barddhaman Junction"
}

print("\nAvailable Stations:\n")
for code, name in st.items():
    print(f"{code} : {name}", end="   ")
print()
ss = input("\nEnter source station code (e.g., BWN): ").upper()
ds = input("Enter destination station code (e.g., HWH): ").upper()
fare(ss, ds)