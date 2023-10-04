#D'écrir un programme qui va donnée les données d'un emploiyée du clavier
#les donnée:nom,ID,salaire,adresse,marié ou ou nom
nom = input("saisir votre nom:")
salaire = float(input("veuillez saisir votre salaire:"))
adresse = input("saisir votre Adresse:")
id = int(input("saisir votre id:"))
statut = bool(input("éte vous marié?[true|false]"))
print("Le nom de l'emplyé est:",nom)
print("Le salaire de l'emplyé est:", salaire)
print("L'adresse de l'emplyé est:", adresse)
print("id de l'emplyé est:", id)
print("statut de l'emplyé est:", statut)