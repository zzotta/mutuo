#!/usr/bin/env python

def calcolaRata(capitale, tasso, mesi):

  tas12 = tasso / 12
  tas = (1 + tas12)**mesi
  rata = (tas * capitale * tas12)/(tas - 1)

  return rata

def stampaAmmortamento(capitale, tassi):
  mesi = len(tassi)
  mesiRimanenti = mesi
  interessiTotali = 0
  rataMax = 0

  for i in range(mesi):
    rata = calcolaRata(capitale, tassi[i], mesiRimanenti)

    if rata > rataMax:
      rataMax = rata

    interessi = (capitale * tassi[i]) / 12
    capitale = capitale - (rata - interessi)
    mesiRimanenti = mesiRimanenti - 1 
    interessiTotali += interessi
    print i + 1, rata, interessi, interessiTotali, capitale

  print "====================="
  print "tot:", interessiTotali, rataMax

import sys

capitale = int(sys.argv[1])
#TODO: non derivare gli anni dalla lunghezza della lista dei tassi
anni = int(sys.argv[2])
tipoTasso = sys.argv[3]
#indice = numero da 0 a 2 che indica la colonna del file dei tassi
#colonna 0 = euribor 1 mese
#colonna 1 = euribor 3 mese
#colonna 2 = bce
indice = int(sys.argv[4])
tasso = float(sys.argv[5])/100
spread = float(sys.argv[6])/100
cap = float(sys.argv[7])/100
fileTassi = sys.argv[8]
 
tassi = []
mesiCap = 0

if tipoTasso == "fisso":

  for i in range(anni * 12):
    tassi.append(tasso)

else:
  
  f = open(fileTassi, "r")

  for line in f:
    tassoCorrente = (float(line.split()[indice]) / 100) + spread

    if tassoCorrente > cap:
      mesiCap = mesiCap + 1
      tassoCorrente = cap

    tassi.append(tassoCorrente)

  f.close()

print "capitale:", capitale
#print "tasso:", tasso
print "anni:", anni
#print calcolaRata(capitale, tasso, anni)
print "============================"
stampaAmmortamento(capitale, tassi)
print "mesiCap =", mesiCap

