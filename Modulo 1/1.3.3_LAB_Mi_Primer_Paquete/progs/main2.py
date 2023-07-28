from sys import path

path.append('d:\\Users\\Rui\\Documents\\Development\\Python\\Cisco - Python Essentials II\\Modulo 1\\1.3.3_Mi_Primer_Paquete')
# path.append('..\\packages')

import packages.extra.good.alpha as alp
import packages.extra.good.best.sigma as sig
from packages.extra.iota import funI

print(funI())

print(sig.funS())

print(alp.funA())
