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
Code,Location,Registered,Envelopes,Valid,Občanská demokratická strana,Řád národa 
534421,Bavoryně,239,151,150,18,0,0,6,0,8,7,5,2,4,0,0,16
531057,Beroun,14 804,9 145,9 076,1 363,16,11,576,1,433,651,140,78,205,8,12,1 290

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


