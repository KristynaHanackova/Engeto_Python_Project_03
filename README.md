# Engeto_Python_Project_03
Elections Scraper

Elections scraper - výsledky z volby.cz

Tento Python script stahuje a ukládá výsledky parlamentních voleb v ČR z portálu volby.cz pro vybraný územní celek (okres).
Výsledky ukládá do CSV souboru, kde každý řádek představuje jednu obec.

Požadavky: 
Seznam knihoven pro spuštění scriptu je v souboru requirements.txt

Spuštění:
Skript se spouští v příkazovém řádku se dvěma argumenty:
- 1. argument - URL adresa konkrétního územního celku z volby.cz, musí být zadáno v uvozovkách
- 2. argument - název souboru, kam se výsledky uloží, musí být zadáno v uvozovkách

Příklad: python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2102" "vysledky.csv"

Ukázka výsledku pro okres Beroun: 
<img width="1000" height="168" alt="image" src="https://github.com/user-attachments/assets/7f84f38e-8506-4e54-90b9-c8ad5059bf7c" />



Jak skrip funguje:
1. Validace argumentů - script ověří, že jsou zadány oba argumenty a že první argument je platná URL adresa z volby.cz.
2. Stažení hlavní stránky okresu - script získá seznam obcí, jejich kódů a odkazů na detailní výsledky.
3. Získání seznamu politických stran - script postupně získává názvy všech polických stran
4. Stažení výsledků pro každou obec - počet registrovaných voličů, odevzdaných obálek, platných hlasů a hlasů pro každou politickou stranu.
5. Uložení do CSV - vysvětlení sloupců:
- Code - kód obce
- Location - název obce
- Registered - počet registrovaných voličů
- Envelopes - počet vydaných obálek
- Valid - počet platných hlasů
- Party name - počet hlasů pro každou politickou stranu


