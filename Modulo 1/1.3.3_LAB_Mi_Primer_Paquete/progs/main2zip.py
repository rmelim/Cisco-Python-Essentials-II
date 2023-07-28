from sys import path

path.append('d:\\Users\\Rui\\Documents\\Development\\Python\\Cisco - Python Essentials II\\Modulo 1\\1.3.3_Mi_Primer_Paquete∖∖packages∖∖extrapack.zip')
#path.append('..∖∖packages∖∖extrapack.zip')

import extra.good.best.sigma as sig
import extra.good.alpha as alp
from extra.iota import funI
from extra.good.beta import funB


print(sig.funS())
print(alp.funA())
print(funI())
print(funB())
