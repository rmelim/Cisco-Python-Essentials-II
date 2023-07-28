from sys import path
 
path.append('d:\\Users\\Rui\\Documents\\Development\\Python\\Cisco - Python Essentials II\\Modulo 1\\1.3.3_Mi_Primer_Paquete')

from modules.module import suml, prodl

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))
