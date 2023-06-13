import moves as MP
import Pokedata as PK
import random as rnd

random = (rnd.randint(85, 101))/100
Level = 50
IV = 31
EV = 250
ap = PK.leer_pokedata("pokemon_data.csv")

print("Bienvenido al simulador")
b = str(input("Ingrese el nombre de un Pokémon: "))

idx = -1
while b != ap[idx][0]:
    idx += 1
    x = ap[idx][0]
    if b == x:
        print(f"\nNombre del Pokémon seleccionado: {x.capitalize()}\n\nEstadísticas base del Pokémon:"
              f"\n - HP = {ap[idx][2]}\n - Ataque = {ap[idx][3]}\n - Defensa = {ap[idx][4]}"
              f"\n - Ataque especial = {ap[idx][5]}\n - Defensa especial = {ap[idx][6]}"
              f"\n - Velocidad = {ap[idx][7]}")
        hp = ((((ap[idx][2] + IV) * 2 + ((EV ** (1 / 2)) / 4)) * Level) / 100) + Level + 10
        # OtherStats
        atk = ((((ap[idx][3] + IV) * 2 + ((EV ** (1 / 2)) / 4)) * Level) / 100) + 5
        dfn = ((((ap[idx][4] + IV) * 2 + ((EV ** (1 / 2)) / 4)) * Level) / 100) + 5
        spa = ((((ap[idx][5] + IV) * 2 + ((EV ** (1 / 2)) / 4)) * Level) / 100) + 5
        spd = ((((ap[idx][6] + IV) * 2 + ((EV ** (1 / 2)) / 4)) * Level) / 100) + 5
        spe = ((((ap[idx][7] + IV) * 2 + ((EV ** (1 / 2)) / 4)) * Level) / 100) + 5
        # Ataques
        print(f"\nMovimientos que puede aprender el Pokémon:")
        z = ap[idx][8].split(";")
        c = -1
        for i in z:
            c += 1
            print(f"{c} - {i}")

        CG = int(input("Seleccione un ataque a ejecutar: "))
        if CG in range(0, len(z) - 1):
            print(f"El ataque seleccionado es: {z[CG]}")
            a = MP.get_move(f"{z[CG]}")
            print(f"Poder de ataque es: {a[1]}")
        else:
            while CG not in range(0, len(z) - 1):
                CG = int(input("Seleccione otro ataque a ejecutar: "))
                if CG in range(0, len(z) - 1):
                    print(f"El ataque seleccionado es: {z[CG]}")
                    a = MP.get_move(f"{z[CG]}")
                    print(f"Poder de ataque es: {a[1]}")

        # Habilidades Level
        print(f"El hp al nivel {Level} de {x.capitalize()} es {hp}\n"
              f"El atk al nivel {Level} de {x.capitalize()} es {atk}\n"
              f"El def al nivel {Level} de {x.capitalize()} es {dfn}\n"
              f"El spa al nivel {Level} de {x.capitalize()} es {spa}\n"
              f"El spd al nivel {Level} de {x.capitalize()} es {spd}\n"
              f"El spe al nivel {Level} de {x.capitalize()} es {spe}")

        # Pokémon defensor
        bn = str(input("Ingrese el nombre a atacar Pokémon: "))
        ix = -1
        while bn != ap[ix][0]:
            ix += 1
            xb = ap[ix][0]
            if bn == xb:
                hp2 = ((((ap[ix][2] + IV) * 2 + ((EV ** (1 / 2)) / 4)) * Level) / 100) + Level + 10
                atk2 = ((((ap[ix][3] + IV) * 2 + ((EV ** (1 / 2)) / 4)) * Level) / 100) + 5
                dfn2 = ((((ap[ix][4] + IV) * 2 + ((EV ** (1 / 2)) / 4)) * Level) / 100) + 5
                spa2 = ((((ap[ix][5] + IV) * 2 + ((EV ** (1 / 2)) / 4)) * Level) / 100) + 5
                spd2 = ((((ap[ix][6] + IV) * 2 + ((EV ** (1 / 2)) / 4)) * Level) / 100) + 5
                spe2 = ((((ap[ix][7] + IV) * 2 + ((EV ** (1 / 2)) / 4)) * Level) / 100) + 5
                # Habilidades Level
                print(f"\nNombre del Pokémon seleccionado: {xb.capitalize()}\n"
                      f"\nEl hp al nivel {Level} de {xb.capitalize()} es {hp2}")

                # Atacante ATK y Defensor DFN
                A = a[3]
                if A == "physical":
                    A = atk
                else:
                    A = spa
                if A == "special":
                    D = dfn2
                else:
                    D = spd2
                # STAB
                if a[2] == ap[idx][1]:
                    STAB = 1.2
                else:
                    STAB = 1
                # Type
                bp = PK.leer_efectividad("tabla_efectividad.csv")
                lpx = -1
                while a[2] != bp[lpx][0]:
                    lpx += 1
                    G = bp[lpx][0]
                    if a[2] == G:
                        lx = -1
                        while ap[ix][1] != bp[lx][0]:
                            lx += 1
                            GT = bp[lx][0]
                            if ap[ix][1] == GT:
                                Type = float(bp[lpx][lx])
                                # Modifier
                                Modifier = (Type * STAB * random * 1)
                                # Damage
                                Damage = ((((((2 * Level) / 5) + 2) * a[1] * (A / D)) / 50) + 2) * Modifier
                                print(f"El daño que realizó {x.capitalize()} a {xb.capitalize()} fue de: {Damage}")
                                # Final
                                HP_restante = hp2 - Damage
                                print(f"\n{xb.capitalize()} quedó con un HP de: {HP_restante}")