sklep = {
    "Marchew" : "kilogramy",
    "Mleko" : "litry",
    "Baton" : "sztuki",
    "Chleb" : "bochenki",
    "Cola" : "litry",
    "Czipsy" : "sztuki"
}

print(sklep)

a = {key for key, value in sklep.items() if value == "sztuki"}

print(a)




