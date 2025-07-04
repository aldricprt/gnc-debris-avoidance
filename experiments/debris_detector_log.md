# Log: Intégration d'un module de détection de débris (approche simple)

**Date de début : 2025-07-04**

## Objectif
Intégrer un module de détection de débris basé sur la distance dans la simulation GNC, et documenter chaque étape/test/choix technique.

## Étape 1 : Création du module de détection de débris

- Créer un fichier `src/gnc/debris_detector.py`.
- Définir une classe `DebrisDetector` qui prend une liste de positions de débris et un rayon de détection.
- Méthode `detect(sat_position)` qui retourne True si un débris est détecté à proximité.

## Étape 2 : Tests unitaires

- Créer un test dans `tests/test_debris_detector.py` pour valider le comportement du module.

## Étape 3 : Intégration dans la simulation

- Appeler le module de détection à chaque pas de temps.
- Logguer les cas où un débris est détecté.

## Étape 4 : Améliorations et variantes

- Tester avec plusieurs débris, différents rayons, positions bruitées, etc.

---

*Ce fichier sera complété à chaque étape pour garder une trace claire de l'évolution du module.*


## Résultat du 2025-07-04T15:56:20
Débris simulés aux positions : [[450], [390]] (rayon 5.0 km)
Nombre de détections : 214
- Débris détecté à t=344s, altitude estimée=393.4 km
- Débris détecté à t=345s, altitude estimée=393.6 km
- Débris détecté à t=353s, altitude estimée=394.7 km
- Débris détecté à t=354s, altitude estimée=393.9 km
- Débris détecté à t=355s, altitude estimée=394.2 km
- Débris détecté à t=356s, altitude estimée=394.5 km
- Débris détecté à t=357s, altitude estimée=393.6 km
- Débris détecté à t=358s, altitude estimée=393.7 km
- Débris détecté à t=359s, altitude estimée=393.4 km
- Débris détecté à t=360s, altitude estimée=393.4 km
- Débris détecté à t=361s, altitude estimée=393.6 km
- Débris détecté à t=362s, altitude estimée=393.1 km
- Débris détecté à t=363s, altitude estimée=391.5 km
- Débris détecté à t=364s, altitude estimée=392.6 km
- Débris détecté à t=365s, altitude estimée=393.0 km
- Débris détecté à t=366s, altitude estimée=391.9 km
- Débris détecté à t=367s, altitude estimée=393.2 km
- Débris détecté à t=368s, altitude estimée=393.2 km
- Débris détecté à t=369s, altitude estimée=393.4 km
- Débris détecté à t=370s, altitude estimée=392.9 km
- Débris détecté à t=371s, altitude estimée=393.5 km
- Débris détecté à t=372s, altitude estimée=393.4 km
- Débris détecté à t=373s, altitude estimée=393.9 km
- Débris détecté à t=374s, altitude estimée=393.0 km
- Débris détecté à t=375s, altitude estimée=394.0 km
- Débris détecté à t=376s, altitude estimée=393.0 km
- Débris détecté à t=377s, altitude estimée=393.1 km
- Débris détecté à t=378s, altitude estimée=393.8 km
- Débris détecté à t=383s, altitude estimée=394.8 km
- Débris détecté à t=386s, altitude estimée=394.8 km
- Débris détecté à t=387s, altitude estimée=394.5 km
- Débris détecté à t=388s, altitude estimée=393.6 km
- Débris détecté à t=389s, altitude estimée=394.3 km
- Débris détecté à t=390s, altitude estimée=395.0 km
- Débris détecté à t=394s, altitude estimée=395.0 km
- Débris détecté à t=395s, altitude estimée=393.3 km
- Débris détecté à t=396s, altitude estimée=393.8 km
- Débris détecté à t=397s, altitude estimée=392.8 km
- Débris détecté à t=398s, altitude estimée=392.8 km
- Débris détecté à t=399s, altitude estimée=395.0 km
- Débris détecté à t=400s, altitude estimée=394.6 km
- Débris détecté à t=401s, altitude estimée=393.8 km
- Débris détecté à t=402s, altitude estimée=393.6 km
- Débris détecté à t=403s, altitude estimée=393.4 km
- Débris détecté à t=404s, altitude estimée=392.6 km
- Débris détecté à t=405s, altitude estimée=392.2 km
- Débris détecté à t=406s, altitude estimée=391.4 km
- Débris détecté à t=407s, altitude estimée=391.6 km
- Débris détecté à t=408s, altitude estimée=392.9 km
- Débris détecté à t=409s, altitude estimée=391.3 km
- Débris détecté à t=410s, altitude estimée=390.4 km
- Débris détecté à t=411s, altitude estimée=391.7 km
- Débris détecté à t=412s, altitude estimée=391.2 km
- Débris détecté à t=413s, altitude estimée=390.9 km
- Débris détecté à t=414s, altitude estimée=390.9 km
- Débris détecté à t=415s, altitude estimée=391.8 km
- Débris détecté à t=416s, altitude estimée=391.2 km
- Débris détecté à t=417s, altitude estimée=391.0 km
- Débris détecté à t=418s, altitude estimée=389.6 km
- Débris détecté à t=419s, altitude estimée=387.6 km
- Débris détecté à t=420s, altitude estimée=388.7 km
- Débris détecté à t=421s, altitude estimée=389.3 km
- Débris détecté à t=422s, altitude estimée=390.2 km
- Débris détecté à t=423s, altitude estimée=390.2 km
- Débris détecté à t=424s, altitude estimée=389.1 km
- Débris détecté à t=425s, altitude estimée=389.5 km
- Débris détecté à t=426s, altitude estimée=389.7 km
- Débris détecté à t=427s, altitude estimée=390.0 km
- Débris détecté à t=428s, altitude estimée=390.1 km
- Débris détecté à t=429s, altitude estimée=389.6 km
- Débris détecté à t=430s, altitude estimée=390.5 km
- Débris détecté à t=431s, altitude estimée=389.9 km
- Débris détecté à t=432s, altitude estimée=389.4 km
- Débris détecté à t=433s, altitude estimée=388.9 km
- Débris détecté à t=434s, altitude estimée=390.4 km
- Débris détecté à t=435s, altitude estimée=390.2 km
- Débris détecté à t=436s, altitude estimée=389.7 km
- Débris détecté à t=437s, altitude estimée=390.0 km
- Débris détecté à t=438s, altitude estimée=389.5 km
- Débris détecté à t=439s, altitude estimée=389.5 km
- Débris détecté à t=440s, altitude estimée=389.0 km
- Débris détecté à t=441s, altitude estimée=389.0 km
- Débris détecté à t=442s, altitude estimée=388.4 km
- Débris détecté à t=443s, altitude estimée=388.7 km
- Débris détecté à t=444s, altitude estimée=389.2 km
- Débris détecté à t=445s, altitude estimée=388.8 km
- Débris détecté à t=446s, altitude estimée=389.8 km
- Débris détecté à t=447s, altitude estimée=390.4 km
- Débris détecté à t=448s, altitude estimée=391.4 km
- Débris détecté à t=449s, altitude estimée=389.5 km
- Débris détecté à t=450s, altitude estimée=388.2 km
- Débris détecté à t=451s, altitude estimée=388.7 km
- Débris détecté à t=452s, altitude estimée=390.0 km
- Débris détecté à t=453s, altitude estimée=389.9 km
- Débris détecté à t=454s, altitude estimée=388.9 km
- Débris détecté à t=455s, altitude estimée=388.7 km
- Débris détecté à t=456s, altitude estimée=387.8 km
- Débris détecté à t=457s, altitude estimée=389.6 km
- Débris détecté à t=458s, altitude estimée=389.3 km
- Débris détecté à t=459s, altitude estimée=388.1 km
- Débris détecté à t=460s, altitude estimée=387.3 km
- Débris détecté à t=461s, altitude estimée=387.1 km
- Débris détecté à t=462s, altitude estimée=387.6 km
- Débris détecté à t=463s, altitude estimée=387.5 km
- Débris détecté à t=464s, altitude estimée=386.8 km
- Débris détecté à t=465s, altitude estimée=386.0 km
- Débris détecté à t=466s, altitude estimée=386.9 km
- Débris détecté à t=467s, altitude estimée=387.7 km
- Débris détecté à t=468s, altitude estimée=387.4 km
- Débris détecté à t=469s, altitude estimée=387.7 km
- Débris détecté à t=470s, altitude estimée=385.3 km
- Débris détecté à t=471s, altitude estimée=385.4 km
- Débris détecté à t=472s, altitude estimée=387.5 km
- Débris détecté à t=473s, altitude estimée=388.3 km
- Débris détecté à t=474s, altitude estimée=390.0 km
- Débris détecté à t=475s, altitude estimée=389.7 km
- Débris détecté à t=476s, altitude estimée=390.5 km
- Débris détecté à t=477s, altitude estimée=390.8 km
- Débris détecté à t=478s, altitude estimée=390.2 km
- Débris détecté à t=479s, altitude estimée=390.8 km
- Débris détecté à t=480s, altitude estimée=390.6 km
- Débris détecté à t=481s, altitude estimée=391.7 km
- Débris détecté à t=482s, altitude estimée=392.7 km
- Débris détecté à t=483s, altitude estimée=392.4 km
- Débris détecté à t=484s, altitude estimée=390.1 km
- Débris détecté à t=485s, altitude estimée=390.8 km
- Débris détecté à t=486s, altitude estimée=389.8 km
- Débris détecté à t=487s, altitude estimée=389.0 km
- Débris détecté à t=488s, altitude estimée=388.5 km
- Débris détecté à t=489s, altitude estimée=388.1 km
- Débris détecté à t=490s, altitude estimée=390.5 km
- Débris détecté à t=491s, altitude estimée=390.4 km
- Débris détecté à t=492s, altitude estimée=391.1 km
- Débris détecté à t=493s, altitude estimée=389.5 km
- Débris détecté à t=494s, altitude estimée=390.1 km
- Débris détecté à t=495s, altitude estimée=390.3 km
- Débris détecté à t=496s, altitude estimée=390.4 km
- Débris détecté à t=497s, altitude estimée=389.8 km
- Débris détecté à t=498s, altitude estimée=389.4 km
- Débris détecté à t=499s, altitude estimée=389.0 km
- Débris détecté à t=500s, altitude estimée=389.9 km
- Débris détecté à t=501s, altitude estimée=391.2 km
- Débris détecté à t=502s, altitude estimée=391.1 km
- Débris détecté à t=503s, altitude estimée=391.2 km
- Débris détecté à t=504s, altitude estimée=391.2 km
- Débris détecté à t=505s, altitude estimée=390.4 km
- Débris détecté à t=506s, altitude estimée=391.3 km
- Débris détecté à t=507s, altitude estimée=390.6 km
- Débris détecté à t=508s, altitude estimée=387.6 km
- Débris détecté à t=509s, altitude estimée=387.9 km
- Débris détecté à t=510s, altitude estimée=388.6 km
- Débris détecté à t=511s, altitude estimée=388.8 km
- Débris détecté à t=512s, altitude estimée=388.0 km
- Débris détecté à t=513s, altitude estimée=387.8 km
- Débris détecté à t=514s, altitude estimée=390.9 km
- Débris détecté à t=515s, altitude estimée=391.2 km
- Débris détecté à t=516s, altitude estimée=393.1 km
- Débris détecté à t=517s, altitude estimée=393.4 km
- Débris détecté à t=518s, altitude estimée=394.3 km
- Débris détecté à t=519s, altitude estimée=394.1 km
- Débris détecté à t=520s, altitude estimée=393.7 km
- Débris détecté à t=521s, altitude estimée=393.5 km
- Débris détecté à t=522s, altitude estimée=393.4 km
- Débris détecté à t=523s, altitude estimée=392.6 km
- Débris détecté à t=524s, altitude estimée=393.0 km
- Débris détecté à t=525s, altitude estimée=392.3 km
- Débris détecté à t=526s, altitude estimée=392.1 km
- Débris détecté à t=527s, altitude estimée=391.8 km
- Débris détecté à t=528s, altitude estimée=390.5 km
- Débris détecté à t=529s, altitude estimée=393.1 km
- Débris détecté à t=530s, altitude estimée=391.5 km
- Débris détecté à t=531s, altitude estimée=391.1 km
- Débris détecté à t=532s, altitude estimée=389.2 km
- Débris détecté à t=533s, altitude estimée=389.2 km
- Débris détecté à t=534s, altitude estimée=387.8 km
- Débris détecté à t=535s, altitude estimée=390.0 km
- Débris détecté à t=536s, altitude estimée=390.0 km
- Débris détecté à t=537s, altitude estimée=389.4 km
- Débris détecté à t=538s, altitude estimée=388.4 km
- Débris détecté à t=539s, altitude estimée=390.0 km
- Débris détecté à t=540s, altitude estimée=391.0 km
- Débris détecté à t=541s, altitude estimée=391.4 km
- Débris détecté à t=542s, altitude estimée=391.6 km
- Débris détecté à t=543s, altitude estimée=391.1 km
- Débris détecté à t=544s, altitude estimée=390.7 km
- Débris détecté à t=545s, altitude estimée=390.6 km
- Débris détecté à t=546s, altitude estimée=390.7 km
- Débris détecté à t=547s, altitude estimée=390.0 km
- Débris détecté à t=548s, altitude estimée=390.1 km
- Débris détecté à t=549s, altitude estimée=389.4 km
- Débris détecté à t=550s, altitude estimée=387.5 km
- Débris détecté à t=551s, altitude estimée=387.8 km
- Débris détecté à t=552s, altitude estimée=388.6 km
- Débris détecté à t=553s, altitude estimée=389.9 km
- Débris détecté à t=554s, altitude estimée=390.6 km
- Débris détecté à t=555s, altitude estimée=391.4 km
- Débris détecté à t=556s, altitude estimée=390.4 km
- Débris détecté à t=557s, altitude estimée=391.0 km
- Débris détecté à t=558s, altitude estimée=392.2 km
- Débris détecté à t=559s, altitude estimée=393.3 km
- Débris détecté à t=560s, altitude estimée=393.7 km
- Débris détecté à t=561s, altitude estimée=394.9 km
- Débris détecté à t=573s, altitude estimée=394.0 km
- Débris détecté à t=574s, altitude estimée=393.5 km
- Débris détecté à t=575s, altitude estimée=393.7 km
- Débris détecté à t=576s, altitude estimée=394.9 km
- Débris détecté à t=577s, altitude estimée=393.6 km
- Débris détecté à t=578s, altitude estimée=393.9 km
- Débris détecté à t=579s, altitude estimée=393.5 km
- Débris détecté à t=580s, altitude estimée=394.0 km
- Débris détecté à t=581s, altitude estimée=395.0 km
- Débris détecté à t=582s, altitude estimée=393.9 km
- Débris détecté à t=583s, altitude estimée=394.6 km
- Débris détecté à t=589s, altitude estimée=394.3 km
