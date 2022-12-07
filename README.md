# LINFO1252_Projet

Année académique : 2022 - 2023
Auteurs :  
Hugolin Louis - Maxime Delacroix   

## Intérêt de notre programme :

Notre programme résoud trois problèmes connue de programmation multi-threadé (Philosophes, producteurs-consomateurs, lecteurs-ecrivains), on peut trouvé ces trois programmes dans le dossier src/Posix. Nous avons aussi implementer un programme d'attente active (attente_active/*.c). Les trois problèmes on été aussi résolu en utilisant notre methode d'attente active (dans src/attente_active/*.c) 

## Structure du projet:

Le projet est composé de 3 dossiers :
- src : Contient deux implémentation différente des 3 problèmes, et le fichier stack.c qui implémente la stack nescessaire pour les autres problèmes.
    - src/Posix : contient les programmes multi-threadé (Philosophes, producteurs-consomateurs, lecteurs-ecrivains)
    - src/attente_active : contient les programmes multi-threadé avec notre methode d'attente active (Philosophes, producteurs-consomateurs, lecteurs-ecrivains)

