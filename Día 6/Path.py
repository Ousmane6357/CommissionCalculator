from pathlib import Path

guia = Path('Africa','CostaMarfil','Abidjan','Yopougon.txt')

en_africa = guia.relative_to(Path('Africa'))
en_CostaMarfil = guia.relative_to(Path("Africa","CostaMarfil"))
print(en_africa)
print(en_CostaMarfil)
