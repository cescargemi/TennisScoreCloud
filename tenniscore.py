partits = []

def introdueix_partit():
    jugador_a = input("Nom jugador A: ")
    jugador_b = input("Nom jugador B: ")
    sets_a = int(input(f"Sets guanyats per {jugador_a}: "))
    sets_b = int(input(f"Sets guanyats per {jugador_b}: "))
    guanyador = jugador_a if sets_a > sets_b else jugador_b

    partit = {
        "jugador_a": jugador_a,
        "jugador_b": jugador_b,
        "sets_a": sets_a,
        "sets_b": sets_b,
        "guanyador": guanyador
    }
    partits.append(partit)
    print("\nResultat enregistrat:")
    print(partit)

def mostra_historial():
    for p in partits:
        print(f"{p['jugador_a']} vs {p['jugador_b']} — {p['sets_a']}:{p['sets_b']} (Guanyador: {p['guanyador']})")

while True:
    print("\n1) Afegeix resultat\n2) Mostra historial\n0) Sortir")
    opcio = input("Opció: ")
    if opcio == "1":
        introdueix_partit()
    elif opcio == "2":
        mostra_historial()
    elif opcio == "0":
        break
    else:
        print("Opció incorrecta.")
