# -*- coding: UTF-8 -*-
from itertools import product
from random import shuffle
from time import time
import hashlib, timeit


def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEn$
    """
    printProgressBar adopted from: https://gist.github.com/greenstick/b23e475d2bfdc3a82e34eaa1f6781ee4
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)

#PWTESTER
print ("Tervetuloa salasanan murtoaikojen esimerkkilaskuriin")
#Pyydetään sallitut merkit
merkit = ""
while merkit == "":
        merkit = input("Anna sallitut merkit:\n")
merkit = list(dict.fromkeys(merkit))
shuffle(merkit) #Sekoitetaan, jotta 
merkkien_lkm = len(merkit)
print (f"\nYhteensä {merkkien_lkm} eri merkkiä")

                      
# Pyydetään käyttäjältä "murrettava" salasana
salasana = ""
while salasana == "":
        salasana = input("Anna \"murrettava\" salasana:\n")
        for c in salasana:
                if c not in merkit:
                        salasana = ""
                        print ("Käytä vain antamiasi sallittuja merkkejä!\n")
                        break

salasanan_pit = len(salasana)
salasana_tuple = tuple(salasana)
print (f"\nSalasanan pituus: {salasanan_pit} merkkiä")
salasanoja = pow(merkkien_lkm,salasanan_pit)
print (f"\nMahdollisia salasanoja yhteensä: {salasanoja}kpl. Katsotaan kauanko tietokoneella kestäisi löytää antamasi salasana!")

i = 0
n = 0
limit = int(salasanoja/1000)
if limit == 0:
        limit = 1
##Lähdetään kokeilemaan salasanoja
print("\n")
printProgressBar(0, salasanoja, prefix = 'Eteneminen:', suffix = 'salasanoista käyty läpi', length = 50)
aloitus = time()
for pw in product(merkit,repeat=salasanan_pit):                                                                                            
        i += 1
        n = (n+1)%limit
        if pw == salasana_tuple:
                printProgressBar(i, salasanoja, prefix = 'Eteneminen:', suffix = 'salasanoista käyty läpi', length = 50)
                print ("\nSalasana murrettu!")
                print ("\n Oikea salasana on: {pw}")
                break
        if n == 0:
                printProgressBar(i, salasanoja, prefix = 'Eteneminen:', suffix = 'salasanoista käyty läpi', length = 50)

lopetus = time()
kulunut_aika = lopetus - aloitus
aika_per_pw = kulunut_aika/i
print (f"\nOikean salasanan löytämiseksi piti tällä kertaa kokeilla {i+1} salasanaa {salasanoja} mahdollisesta salasanasta. Tämän ohjelman kokeilujärjestys on melko satunnainen.\n")
print (f"Aikaa kului {kulunut_aika} sekuntia, {aika_per_pw} sekuntia per salasana.\n")
print ("Mitataan tiivisteiden laskemiseen menevä aika koneellasi:\n")
md5_aika = timeit.timeit('hashlib.md5(passwd.encode("utf-8"))',setup='import hashlib,os;passwd="salasana123";salt=os.urandom(32)',number=1000)/1000
pbkds2_hmac_aika = timeit.timeit('hashlib.pbkdf2_hmac("sha256",passwd.encode("utf-8"),salt,100000)',setup='import hashlib,os;passwd="salasana123";salt=os.urandom(32)',number=10)/10
print (f"Salasanoihin tarkoitetun pythonin pbkds2_hmac -funktiolla lasketun tiivisteen (käyttäen SHA-256-tiivistettä ja 100000 laskukierrosta) laskemisaika on {pbkds2_hmac_aika} sekuntia.")
print (f"Jos salasanan murtamiseksi olisi pitänyt laskea jokaisen salasanaehdokkaan kohdalla kyseinen tiiviste, aikaa olisi kulunut noin {i*pbkds2_hmac_aika} sekuntia enemmän! Eli toisin sanottuna {i*pbkds2_hmac_aika/60} minuuttia tai {i*pbkds2_hmac_aika/60/60} tuntia! --- Oikeanlainen tiivisteen käyttö siis kasvattaa murtamisaikaa melkoisesti.");
print (f"\n\nVastaavasti pelkän turvattoman MD5-tiivisteen laskemisaika on {md5_aika} sekuntia, eli laskenta-aika olisi kasvanut MD5-tiivisteiden laskemisesta vain {i*md5_aika} sekuntia - ei kovin suurta vaikutusta! Huomaatko miten tärkeää oikeanlaisen tiivistefunktion oikea käyttö on?")
print (f"Kokeile rohkeasti: vaihtele merkkien määrää ja salasanan pituuksia, niin näet niiden vaikutuksen laskenta-aikaan!")

                      
