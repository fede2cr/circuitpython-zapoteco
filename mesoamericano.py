"""
Módulo para manipular y aprender numeración mesoamericana, en diferentes idiomas indígenas.

Este módulo permite traducir entre numeración decimal y numeración mesoamericana, con el fin de utilizarlo para difundir esta forma de numeración presente en glifos y escrituras de múltiples culturas indígenas americanas, así como también su pronunciación en diversas lenguas locales de Centroamérica y México. También puede ser utilizada para fines de epigrafía, comparación de idiomas o culturas.

"""

import board
from analogio import AnalogIn
try:
    import urandom as random
except ImportError:
    import random

unconnected_pin = board.A0
pin = AnalogIn(unconnected_pin)
random.seed(pin.value)
pin.deinit()

num_zapoteco = [ "0", "Chāga", "Cāto", "Cāyo", "Taà", "Gaàyú",
        "Guàyú-bichāga", "Guàyú-bicāto", "Guàyú-bicāyo", "Guàyú-bitaà", "Chiì",
        "Chiì-bichāga", "Chiì-bicāto", "Chiì-bicāyo", "Chiì-bitaà", "Chiìnu",
        "Chiìnu-bichāga", "Chiìnu-bicāto", "Chiìnu-bicāyo", "Chiìnu-bitaà", "Gāndé"]

num_bribri = [ "0", 'E\'köl', 'Böl', 'Māñál','Tkél', 'Skél',
        'Tèröl', 'Kúl', 'Pàköl', 'Sūlítu', 'Dabòm']


def traductor(lang, num):
    if lang == "bribri":
        return (num_bribri[num])
    if lang == "zapoteco":
        return (num_zapoteco[num])

def quiz(lang, marcador):
    if lang == "bribri":
        num = random.randint(1, len(num_bribri))
        return (num, num_bribri[num])
    if lang == "zapoteco":
        num = random.randint(1, len(num_zapoteco))
        print(num_zapoteco[num])
        respuesta = int(input("¿A que numero corresponde? "))
    if respuesta == num:
        print("Numero correcto")
        marcador = marcador + 1
    else:
        print("Numero incorrecto, el correcto es el numero ", num)
        marcador = marcador - 1
    return marcador

