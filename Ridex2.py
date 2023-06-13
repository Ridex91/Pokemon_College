from moves import get_move
import Pokedata as PK
import random as rnd

random = (rnd.randint(85, 101))/100
ap = PK.leer_pokedata("pokemon_data.csv")
Level = 50

#Pokémon Atacante
print("Bienvenido al simulador")
b = str(input("Ingrese el nombre del primer Pokémon: "))

for pokemon in ap:
    if b.lower() in pokemon:
        # Es la impresion de la interfaz de la clase
        print(PK.Pokemon(pokemon))
        # Z es la variable que almacena los movimientos del Pokémon
        z = pokemon[8].split(";")
        c = -1
        for i in z:
            c += 1
            ac = (f"{c}  -  {i}")
            print(ac)
        # Ataques
        CG = int(input("Seleccione un ataque a ejecutar: "))
        if CG in range(0, len(z) - 1):
            a = get_move(z[CG])
            if a[1] != 0:
                print(f"El ataque seleccionado es:  {z[CG]}")
                print(f"Poder de ataque es:  {a[1]}")
            else:
                if a[1] == 0:
                    while a[1] == 0:
                        CG = int(input("¡El valor POWER del movimiento escogidó es invalido para calcular DAMAGE!"
                                       "\nSeleccione otro ataque a ejecutar: "))
                        if CG in range(0, len(z) - 1):
                            a = get_move(z[CG])
                            if CG in range(0, len(z) - 1) and a[1] != 0:
                                print(f"El ataque seleccionado es:  {z[CG]}")
                                print(f"Poder de ataque es:  {a[1]}")
        else:
            while CG not in range(0, len(z) - 1):
                CG = int(input("¡El movimiento escogidó no es posible de aprender!"
                               "\n¡Ingrese un movimiento dentro de la lista!"
                               "\nSeleccione otro ataque a ejecutar: "))
                if CG in range(0, len(z) - 1):
                    a = get_move(z[CG])
                    if a[1] == 0:
                        CG = int(input("¡El valor POWER del movimiento escogidó es invalido para calcular DAMAGE!"
                                       "\nSeleccione otro ataque a ejecutar: "))
                        a = get_move(z[CG])
                        if CG in range(0, len(z) - 1) and a[1] != 0:
                            print(f"El ataque seleccionado es:  {z[CG]}")
                            print(f"Poder de ataque es:  {a[1]}")
                        else:
                            while a[1] == 0:
                                CG = int(input("¡El valor POWER del movimiento escogidó es invalido para calcular "
                                               "DAMAGE!\nSeleccione otro ataque a ejecutar: "))
                                if CG in range(0, len(z) - 1):
                                    a = get_move(z[CG])
                                    if CG in range(0, len(z) - 1) and a[1] != 0:
                                        print(f"El ataque seleccionado es:  {z[CG]}")
                                        print(f"Poder de ataque es:  {a[1]}")
                    else:
                        print(f"El ataque seleccionado es:  {z[CG]}")
                        print(f"Poder de ataque es:  {a[1]}")

        # Inicializacion de la clase
        Apokemon = (PK.Pokemon(pokemon))
        # Habilidades Level
        print(f"El hp al nivel {Level} de  {b.capitalize()}  es  {PK.Pokemon.PoKe_FOR(Apokemon)[0]}\n"
                f"El atk al nivel {Level} de  {b.capitalize()}  es  {PK.Pokemon.PoKe_FOR(Apokemon)[1]}\n"
                f"El def al nivel {Level} de  {b.capitalize()}  es  {PK.Pokemon.PoKe_FOR(Apokemon)[2]}\n"
                f"El spa al nivel {Level} de  {b.capitalize()}  es  {PK.Pokemon.PoKe_FOR(Apokemon)[3]}\n"
                f"El spd al nivel {Level} de  {b.capitalize()}  es  {PK.Pokemon.PoKe_FOR(Apokemon)[4]}\n"
                f"El spe al nivel {Level} de  {b.capitalize()}  es  {PK.Pokemon.PoKe_FOR(Apokemon)[5]}")
        # Pokémon Rival
        bn = str(input("Ingrese el nombre a atacar Pokémon: "))
        for pokemon in ap:
            if bn.lower() in pokemon:
                Dpokemon = (PK.Pokemon(pokemon))
                print(f"\nNombre del Pokémon seleccionado:  {bn.capitalize()}"
                        f"\n\nEl hp al nivel {Level} de  {bn.capitalize()}  es  {PK.Pokemon.PoKe_FOR(Dpokemon)[0]}")
                # Atacante ATK y Defensor DFN
                if a[3] == "physical":
                    A = PK.Pokemon.PoKe_FOR(Apokemon)[1]
                else:
                    A = PK.Pokemon.PoKe_FOR(Apokemon)[3]
                if a[3] == "special":
                    D = PK.Pokemon.PoKe_FOR(Dpokemon)[2]
                else:
                    D = PK.Pokemon.PoKe_FOR(Dpokemon)[4]
                # STAB
                if a[2] == PK.Pokemon.PoKe_FOR(Apokemon)[6]:
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
                        while PK.Pokemon.PoKe_FOR(Dpokemon)[6] != bp[lx][0]:
                            lx += 1
                            GT = bp[lx][0]
                            if PK.Pokemon.PoKe_FOR(Dpokemon)[6] == GT:
                                Type = float(bp[lpx][lx])
                                # Modifier
                                Modifier = (Type * STAB * random * 1)
                                # Damage
                                Damage = ((((((2 * Level) / 5) + 2) * a[1] * (A / D)) / 50) + 2) * Modifier
                                print(f"El daño que realizó  {b.capitalize()}  a  {bn.capitalize()}  fue de:  {Damage}")
                                # Final
                                HP_restante = PK.Pokemon.PoKe_FOR(Dpokemon)[0] - Damage
                                print(f"\n{bn.capitalize()} quedó con un HP de:  {HP_restante}")