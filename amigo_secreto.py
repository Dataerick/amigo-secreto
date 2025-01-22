# -*- coding: utf-8 -*-
import os
from sys import platform
from random import randint

# 🎉 Bienvenido al script para el sorteo de Amigos Secretos 🎁

# Inicializa la lista de amigos que participarán en el sorteo
amigos = []

# Solicita al usuario la cantidad de participantes y sus nombres
print("🎈 ¡Bienvenido al sorteo de amigos secretos! 🎈")
qtd_amigos = int(input("🔢 ¿Cuántos amigos hay en tu grupo? "))
for i in range(qtd_amigos):
    amigo = input(f"✏️ Ingresa el nombre del amigo #{i + 1}: ")
    amigos.append({'id': i + 1, 'nombre': amigo})

# Inicializa la lista donde se guardará el resultado del sorteo
sorteo = []

def sortear(sorteando, amigos, sorteados, sorteio, contador):
    """
    Realiza el sorteo recursivo para asignar amigos secretos.
    """
    contador += 1
    if contador > 900:
        return False  # Reinicia el sorteo si se exceden los intentos

    sorteado = amigos[randint(0, qtd_amigos - 1)]

    # Verificaciones para evitar asignaciones no deseadas
    requisito_1 = sorteado['id'] in sorteados  # Ya fue sorteado
    requisito_2 = any(x for x in sorteio if x['sorteante'] == sorteando['id'] and x['sorteado'] == sorteando['id'])
    requisito_3 = sorteado['id'] == sorteando['id']  # No puede sortearse a sí mismo

    if requisito_1 or requisito_2 or requisito_3:
        return sortear(sorteando, amigos, sorteados, sorteio, contador)  # Reintenta el sorteo
    
    # Si pasa todas las verificaciones, agrega el resultado al sorteo
    sorteio.append({'sorteante': sorteando['id'], 'sorteado': sorteado['id']})
    return True

# Realiza el sorteo hasta que todos los amigos tengan su resultado
while len(sorteo) != qtd_amigos:
    sorteo = []
    for rodada in range(qtd_amigos):
        sorteados = [x['sorteado'] for x in sorteo]  # Lista de IDs ya sorteados
        contador = 0
        sortear(amigos[rodada], amigos, sorteados, sorteo, contador)

# Crea un archivo para guardar los resultados del sorteo
with open("resultado.txt", "w", encoding="utf-8") as file:
    file.write("🎉 Resultado del sorteo de Amigos Secretos 🎉\n\n")

    # Muestra y guarda los resultados de manera individual
    for rodada in sorteo:
        for amigo in amigos:
            if rodada['sorteante'] == amigo['id']:
                sorteante = amigo['nombre']
            elif rodada['sorteado'] == amigo['id']:
                sorteado = amigo['nombre']

        # Limpia la pantalla para mantener la sorpresa
        if platform in ['linux', 'linux2', 'darwin']:
            os.system("clear")
        elif platform in ['win32', 'cygwin']:
            os.system("cls")

        input(f"👤 {sorteante}, presiona ENTER para ver a quién has sorteado...")
        print(f"🎁 ¡Has sorteado a: {sorteado}! 🎉\n")
        input("Presiona ENTER para continuar...")

        # Guarda el resultado en el archivo
        file.write(f"{sorteante} sorteó a {sorteado}\n")

print("✅ ¡Sorteo completado! Revisa el archivo 'resultado.txt' para más detalles. 🥳")
