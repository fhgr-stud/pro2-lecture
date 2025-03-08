gemuese = ["Karrote", "Brokkoli", "Spinat"]
fruechte = ["Apfle", "Erdbeere", "Banane"]

lebensmittel = fruechte + gemuese
# print("Lebensmittel", lebensmittel)
# print("Früchte", fruechte)

for item in sorted(lebensmittel):
    if item not in fruechte:
        print(f"{item} ist ein Gemüse")
    elif item in fruechte:
        print(f"{item} ist eine Frucht") 
