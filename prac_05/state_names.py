CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales",
                "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria",
                "TAS": "Tasmania", "SA": "South Australia"}

print("Available state codes:", ", ".join(CODE_TO_NAME.keys()))

state = input("Enter short state: ").upper()
while state != "":
    if state in CODE_TO_NAME:
        print(state, "is", CODE_TO_NAME[state])
    else:
        print("Invalid short state")
    state = input("Enter short state: ").upper()