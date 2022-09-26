#Créé par Dev Patel
#Créé le 16 septembre 2022
#Recevoir le nombre de mots d'un argument type string situé dans une fonction appelée count_word

chaine = input("Écrit une phrase:")
def count_word(chaine):

    # nombre_de_mots est le nom de la variable qui va nous permettre de déterminer le nombre de mots dans la phrase
    nombre_de_mots = len(chaine.split(" "))
    return nombre_de_mots


print(count_word(chaine))
