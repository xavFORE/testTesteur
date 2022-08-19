# -*- coding: utf-8 -*-

from datetime import datetime as dt


age         = 19
hasLicense  = False


def afficheLheure():
    print( dt.now() )

def donneLheure( ):
    return  dt.now() 

def afficheSomme( a, b):
    print( additione( a, b ) )


def additione( a, b ):
    somme =  a + b
    return somme

afficheLheure()

print( additione( 12, 3 ) )

print( donneLheure() )



def determineConduite( age, hasLicense ):
    print( 'age    :', age)
    print( 'permis :', hasLicense)
    if age > 16 and age < 18:
        return 'tu peux conduire en accompagné'
    elif age > 18 :
        return  'tu peux conduire seul si tu as ton permis \nou en accompagné'



print( determineConduite( 17, False ) )


if  determineConduite( 17, False ) == 'tu peux conduire en accompagné':
    print( 'OK')
else:
    print( 'KO')

if  determineConduite( 19, False ) == 'tu peux conduire en accompagné':
    print( 'OK')
else:
    print( 'KO')

if  determineConduite( 19, True ) == 'tu peux conduire seul':
    print( 'OK')
else:
    print( 'KO')

if  determineConduite( 12, False ) == 'tu dois attendre 16 ans':
    print( 'OK')
else:
    print( 'KO')

if  determineConduite( 12, True ) == 'tu es un menteur':
    print( 'OK')
else:
    print( 'KO')



