from json import dump, load, dumps, loads

produkte =[]
with open("obst.json", "r") as f:
    produkte = load(f)

    for produkt in produkte:
        print(produkt)


