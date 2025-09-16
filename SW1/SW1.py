def convert_curr(dollars):
    p_rate = 57.17
    y_rate = 146.67  

    peso = dollars * p_rate
    yen = dollars * y_rate
    return peso, yen

def process(dollar_string):
    dol_part = dollar_string.split(',')
    Pesoconvert = []
    Yenconvert = []

    for part in dol_part:
        part_value = float(part)
        peso, yen = convert_curr(part_value)

        Pesoconvert.append(peso)
        Yenconvert.append(yen)

    return dol_part, Pesoconvert, Yenconvert

                    #MAIN METHOD
dollarval = input("Enter currency in ($): ")
dol_part, Pesoconvert, Yenconvert = process(dollarval)

print("\n{:<15} {:<20} {:<20}".format("Dollar($)", "Phil Peso(P)", "Jpn Yen(Y)"))

for i in range(len(dol_part)):
    print("{:<15} {:<20,.2f} {:<20,.2f}".format(
        dol_part[i], Pesoconvert[i], Yenconvert[i]
    ))