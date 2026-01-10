1: neighbourchecker:
  kijken of een bepaald getal een buur heeft of niet
2: eerste filter:
  kijken of er 0 jokers zijn:
    kijken of ieder getal een buur heeft of niet, zoniet kan het fysiek niet bij 0 jokers.
3: extended neighbourchecker
  als er 1+ joker(s) is(zijn):
    probeert te kijken bij de buurlozen, of ze door 1 joker ertussen te plaatsen, theoretisch kunnen gelegd worden
    voorbeeld: blauwe 1, blauwe 3, blauwe 4, joker --> 3 en 4 zijn buren, 1 is buurloos, we hebben 1 joker, dus we kunnen hier geraken.
      3 en 4 worden niet gecheckt hier, want ze hebben een theoretische legpositie van 2 naast elkaar, dus je kan een joker erachter of ervoor toevoegen, dit is voor later
      1 wordt hier wel gecheckt, er is geen getal voor 1, dus daar wordt ook niet naar gekeken, maar er zijn wel getallen na 1, dus kijkt de code als je een joker zou leggen,
      zou je de 1 wel een buur kunnen geven:
        1x3? --> mogelijk
      DEZE CHECKER IS ALLEEN VOOR ZELFDE KLEUR (voor zelfde cijfer ander kleur wordt al naar elke buur gekeken, dus gaat dit geen impact hebben, en dus nutteloos zijn)
4: tweede filter
  als er 1 joker is:
    kijkt of ieder getal in 1 van de twee lijsten staat (buren of verre buren)
      als er 1 getal niet in beide lijsten staat, kan dit niet opgelost worden.
5: alle mogelijke unieke 3 tile rijen vormen:
    ALS ER EEN RIJ GEVONDEN IS, HERHAAL DAT GETAL TOT ER GEEN NIEUWE UNIEKE RIJEN MEER ZIJN
    nummers verschillend kleur zelfde:
      kijkt 2-4 getallen terug (als mogelijk) en 2-4 getallen verder (als mogelijk)
      als je een rij van 3 kunt vormen, kijk of deze al in de lijst staat, zoniet, voeg deze gesorteerd (optellend) toe aan de lijst in een array met de 3 getallen, anders naar volgende cyclus gaan
    nummers zelfde, kleur verschillend:
      kijkt 0-6 getallen terug en 0-6 getallen verder (als nummer%10 = 1, 6 getallen maximaal verder, 0 getallen terug, gelijk bij buren)
      zelfde regel als bij nummers verschillend kleur zelfde, maar apparte lijst
6: derde filter:
  als er 0 jokers zijn:
    als er bij de 3 tile rijen 1 getal niet in zit, is het niet mogelijk
7: een lijst die bijhoud hoeveel van elk getal er voorkomt (0/1/2)
  soort van lib



simpel uitgelegd:
stap 1 maakt 2 lijsten, waar tiles  instaan die minimum 1 buur hebben
stap 2 kijkt bij 0 jokers of er een tile  niet in 1 van de 2 lijsten staat, want dan kan het niet
stap 3 alleen bij 1 of meer jokers: maakt een lijst met alle tiles die geen dichte buren hebben, maar wel buren met 1 tile tussen de 2 (dus bv 1j3).
stap 4 alleen bij 1 joker: kijkt of een getal niet in 1 van de 3 lijsten staat, als dat zo is, kan het niet allemaal gelegd worden
stap 5 vormt alle mogelijke unieke 3 tile combinaties, exclusief jokers
stap 6 kijkt bij 0 jokers of 1 getal daar niet instaat, want als er 1 getal daar niet instaat, kan dit niet

wat zou dit al filtreren:
theoretisch onmogelijke games bij 0 en 1 joker(s)

nog niet gefiltreerd:
praktisch onmogelijke games bij alle variaties

wat moet er gebeuren voor alles te kunnen filtreren (vast traag maar gaat nrml werken):
  een stap/meerdere stappen die  

