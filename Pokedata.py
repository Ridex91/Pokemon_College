def leer_pokedata(nombre_archivo):
    libro = open(nombre_archivo, "r")
    libro = libro.readlines()
    A = []
    for linea in libro:
        linea = linea.strip().split(",")
        for i in range(2, 8):
            linea[i] = int(linea[i])
        A.append(linea)
    return A

def leer_efectividad(nombre_archivo):
    libro = open(nombre_archivo, "r")
    libro = libro.readlines()
    A = []
    for linea in libro:
        linea = linea.strip().split(",")
        A.append(linea)
    return A

class Pokemon:
    # Atributos
    def __init__(self, pokemon, Level = 50, IV = 31, EV = 250):
        self.nombre = pokemon[0].capitalize()
        self.Level = Level
        self.IV = IV
        self.EV = EV
        self.tipo = pokemon[1]
        self.hp, self.atk, self.dfn = pokemon[2], pokemon[3], pokemon[4]
        self.spa, self.spd, self.spe = pokemon[5], pokemon[6], pokemon[7]

    # Metodos
    # PoKe_FOR = Pokemon formulas, tanto para atacante, como para rival.
    def PoKe_FOR(self):
        HP = ((((self.hp + self.IV) * 2 + ((self.EV ** (1 / 2)) / 4)) * self.Level) / 100) + self.Level + 10
        ATK = ((((self.atk + self.IV) * 2 + ((self.EV ** (1 / 2)) / 4)) * self.Level) / 100) + 5
        DFN = ((((self.dfn + self.IV) * 2 + ((self.EV ** (1 / 2)) / 4)) * self.Level) / 100) + 5
        SPA = ((((self.spa + self.IV) * 2 + ((self.EV ** (1 / 2)) / 4)) * self.Level) / 100) + 5
        SPD = ((((self.spd + self.IV) * 2 + ((self.EV ** (1 / 2)) / 4)) * self.Level) / 100) + 5
        SPE = ((((self.spe + self.IV) * 2 + ((self.EV ** (1 / 2)) / 4)) * self.Level) / 100) + 5
        tipo = self.tipo
        A = (HP, ATK, DFN, SPA, SPD, SPE, tipo)
        return A

    # Impresion
    def __str__(self):
        k = f"\nNombre del Pokémon seleccionado:  {self.nombre}\n\nEstadísticas base del Pokémon:\n  - HP = {self.hp} " \
            f"\n  - Ataque = {self.atk}\n  - Defensa = {self.dfn}\n  - Ataque especial = {self.spa}" \
            f"\n  - Defensa especial = {self.spd}\n  - Velocidad = {self.spe}" \
            f"\n\nMovimientos que puede aprender el pokémon:"
        return k