1: neighbourchecker: V
  kijken of een bepaald getal een buur heeft of niet V
2: eerste filter: V
  kijken of er 0 jokers zijn: V
    kijken of ieder getal een buur heeft of niet, zoniet kan het fysiek niet bij 0 jokers. V
3: extended neighbourchecker V
  als er 1+ joker(s) is(zijn):
    probeert te kijken bij de buurlozen, of ze door 1 joker ertussen te plaatsen, theoretisch kunnen gelegd worden
    voorbeeld: blauwe 1, blauwe 3, blauwe 4, joker --> 3 en 4 zijn buren, 1 is buurloos, we hebben 1 joker, dus we kunnen hier geraken.
      3 en 4 worden niet gecheckt hier, want ze hebben een theoretische legpositie van 2 naast elkaar, dus je kan een joker erachter of ervoor toevoegen, dit is voor later
      1 wordt hier wel gecheckt, er is geen getal voor 1, dus daar wordt ook niet naar gekeken, maar er zijn wel getallen na 1, dus kijkt de code als je een joker zou leggen,
      zou je de 1 wel een buur kunnen geven:
        1x3? --> mogelijk
      DEZE CHECKER IS ALLEEN VOOR ZELFDE KLEUR (voor zelfde cijfer ander kleur wordt al naar elke buur gekeken, dus gaat dit geen impact hebben, en dus nutteloos zijn)
4: tweede filter V
  als er 1 joker is:
    kijkt of ieder getal in 1 van de drie lijsten staat (buren1,buren2 of verre buren)
      als er 1 getal niet in de drie lijsten staat, kan dit niet opgelost worden.
      anders kijk of de lengte van de lijst verre buren 3 of meer is, dan kan dit ook niet opgelost worden
      anders kijk of de lengte van de lijst verre buren 2 is:
        kijk of je beide verre buren kunt linken aan elkaar, (dus eigenlijk dat ze elkaars verre buren zijn, b1, b3 en j kan wel, maar b1, r2, j kan niet)
          als dat niet zo is, kan het ook niet opgelost worden
  als er meer dan 1 joker is:
    kijk of lengte lijst verre buren > jokeramount*2, dan kan het niet opgelost worden
      
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
7: een lijst die bijhoud hoeveel van elk getal er voorkomt (1/2) V
  soort van lib --> array gekozen V



simpel uitgelegd:
stap 1 maakt 2 lijsten, waar tiles  instaan die minimum 1 buur hebben
stap 2 kijkt bij 0 jokers of er een tile  niet in 1 van de 2 lijsten staat, want dan kan het niet
stap 3 alleen bij 1 of meer jokers: maakt een lijst met alle tiles die geen dichte buren hebben, maar wel buren met 1 tile tussen de 2 (dus bv 1j3).
stap 4 alleen bij 1 joker: kijkt of een getal niet in 1 van de 3 lijsten staat, als dat zo is, kan het niet allemaal gelegd worden
+stap 4 verbeteren: als stap 4 origineel slaagt -->kijken naar lengte van verre buren lijst, als dit meer dan 2 is, kan het niet.
  als er 2 zijn, en ze kunnen niet gelinkt worden, kan het ook niet.
stap 5 vormt alle mogelijke unieke 3 tile combinaties, exclusief jokers
stap 6 kijkt bij 0 jokers of 1 getal daar niet instaat, want als er 1 getal daar niet instaat, kan dit niet

wat zou dit al filtreren:
theoretisch onmogelijke games bij 0 en 1 joker(s)

nog niet gefiltreerd:
praktisch onmogelijke games bij alle variaties

wat moet er gebeuren voor alles te kunnen filtreren (vast traag maar gaat nrml werken):
  voor 0 jokers:                                          APPARTE FUNCTIE MAKEN DIE DIT DOET &uarr;
    een stap/meerdere stappen die  iedere rij probeert-> iedere lengte die niet gesplits kan worden(dus 3-5), en zo verder gaat, tot deze iedere mogelijke optie bekeken heeft, als er niks is dat werkt, dan is het onmogelijk
    voor 0 jokers (variatie van depth first search)
  voor 1 joker:
    *eerste stap: kijken of je alle  verre buren kunt linken, door maar 1 joker te gebruiken:--> verplaats naar stap 4*
      *voorbeelden:*
       *(b = blauw)*
        *1: b1, b3, b4, b5, j --> b1 heeft een verre buur, dus moet zowiezo een joker gebruiken, en kan dus tussen b1 en b2 gelegd worden*
        *2: b1, b3, b5, j --> b1, b3 en b5 hebben allemaal verre buren, je kan b1 en b3 linken, maar b5 niet, dus kan dit niet opgelost worden*
        *verre buren gebeuren alleen maar in 1-13 zelfde kleur, dus andere kleuren maken voor stap 1 niet uit, gewoon of het mogelijk is voor alle linken te leggen.*
      tweede stap:
        als de joker al gebruikt moet worden:
          er is maar 1 mogelijke plaats voor de joker (1x3 bv):
            forceer die rij om te bestaan, maar je kan wel de lengte verlengen van deze rij, maar de 3 elementen die daarin zitten, moeten samenblijven
            doe wat je bij 0 jokers doet
          er zijn 2 mogelijke plaatsen voor de joker (123X5x789 bv):
            forceer eerst de ene variatie, doe de mogelijkheidscalculatie van 0 jokers
            als er geen oplossing gevonden is, probeer dan de andere variatie weer met de mogelijkheidscalculatie van 0 jokers (met die rij dan geforceerd)
    voor meer dan 1 joker:
      nog kijken
