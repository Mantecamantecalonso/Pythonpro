ARG = {
    "4 de copas": "Persona insignificante, sin autoridad o que no aporta nada",
    "wachin": "Persona joven ignorante",
    "mufa": "Cuando alguien dice algo y ocurre al reves, ejemplo: decir que Argentina gana y pierde",
    "Cabala": "acción o objeto que da suerte en (por ejemplo) un partido",
    "vos": "tú, para referirse a alguien",
    "pibe": "niño o persona joven",
    "mi viejo/a": "mi papá/mamá",
    "y mi abuela plancha resorte": "se usa cuando alguien dice una mentira descarada"}
word = input("Escribe una palabra que no entiendas :")
if word in ARG.keys():
    print(ARG[word])
else:
    print("ni idea amigo, me compra media?")
