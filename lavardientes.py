# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 08:09:10 2020

@author: Luis Felipe Cruz
"""

print("Revisar que tiene cepillo, responder si o no")
cepillo = input()
while cepillo != "si":
    print("Busque cepillo, y vuelva nuevamente")
    print("Tiene cepillo ?")
    cepillo = input()
print("Revisar que tiene agua, responder si o no")
agua = input()
while agua != "si":
    print("Busque agua, y vuelva nuevamente")
    print("Tiene agua ?")
    agua = input()
print("Revisar que tiene crema, responder si o no")
agua = input()
while agua != "si":
    print("Busque crema, y vuelva nuevamente")
    print("Tiene crema ?")
    crema = input()
print("Aplicaque la crema en el cepillo de dientes, lo hizo? responda si o no")
cremacepillo = input()
while cremacepillo != "si":
    print("aplique la crema en el cepillo y vuelva nuevamente")
    print("ya aplico la crema en el cepillo ?")
    cremacepillo = input()
while True:    #This simulates a Do Loop
    print("cepille los dientes en toda la boca")
    print("tome agua y elimine el exceso de crema")
    print("lave el cepillo")
    print("frote el cepillo en los dientes y tome agua para eliminar el exceso de crema en la boca")
    print("Presenta restos de comida o de crema dental en la boca, responda si o no")
    limpio = input()
    if not(limpio != "si"): break   #Exit loop
print("Felicitaciones tiene los dientes y boca limpios, vuelva pronto")
