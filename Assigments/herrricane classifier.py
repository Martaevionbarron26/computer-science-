print("hurricane classifier")

hurricane_speed = input("What is the wind speed\n>")
hurricane_speed = int(hurricane_speed)

if hurricane_speed < 74:
    print("tropical storm")

elif hurricane_speed < 96:
    print("category 1")

elif hurricane_speed < 11:
    print("category 2")

elif hurricane_speed < 130:
    print("catogory3")

elif hurricane_speed < 157:
    print("category4")

elif hurricane_speed >= 157:
    print("catogory5")