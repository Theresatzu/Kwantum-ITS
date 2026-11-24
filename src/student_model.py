# Resultaten van de instaptoets

antwoorden = {
    1: 1,
    2: 1,
    3: 0,
    4: 1,
    5: 0,
    6: 1,
    7: 0,
    8: 1,
    9: 0,
    10: 0
}

concept_mapping = {
    "foton": [1, 2],
    "interferentie": [3, 4, 5, 8, 10],
    "buiging": [6, 7],
    "golf_deeltjedualiteit": [9, 10]
}

student_model = {}

for concept, vragen in concept_mapping.items():
    goed = 0

    for vraag in vragen:
        goed += antwoorden[vraag]

    score = goed / len(vragen)
    student_model[concept] = round(score, 2)

print("Studentmodel:")
print()

for concept, score in student_model.items():
    print(f"{concept}: {score}")

zwakste_concept = min(student_model, key=student_model.get)

print()
print("Zwakste concept:", zwakste_concept)

print()
print("Advies van de tutor:")

if zwakste_concept == "golf_deeltjedualiteit":

    uitleg = """
Licht vertoont zowel golf- als deeltjeseigenschappen.

De golfeigenschappen zie je bijvoorbeeld terug bij interferentie
en buiging.

De deeltjeseigenschappen zie je terug doordat licht bestaat
uit fotonen die energie kunnen overdragen.

Het feit dat licht beide eigenschappen bezit noemen we
golf-deeltjedualiteit.
"""

elif zwakste_concept == "interferentie":

    uitleg = """
Interferentie ontstaat wanneer twee of meer golven elkaar ontmoeten.

Bij constructieve interferentie versterken de golven elkaar.

Bij destructieve interferentie doven de golven elkaar uit.
"""

elif zwakste_concept == "buiging":

    uitleg = """
Buiging treedt op wanneer licht door een smalle opening gaat.

Hoe kleiner de opening ten opzichte van de golflengte,
hoe sterker het buigingseffect.
"""

else:

    uitleg = """
Een foton is een lichtdeeltje met een bepaalde hoeveelheid energie.

Fotonen kunnen energie opnemen of afgeven.
"""

print(uitleg)

print("Oefenvraag:")

if zwakste_concept == "golf_deeltjedualiteit":

    vraag = """
Noem één golfeigenschap en één deeltjeseigenschap van licht.
"""

    goed_antwoord = [
        "interferentie",
        "buiging",
        "foton"
    ]

elif zwakste_concept == "interferentie":

    vraag = """
Wat is het verschil tussen constructieve en destructieve interferentie?
"""

    goed_antwoord = [
        "versterken",
        "uitdoven"
    ]

elif zwakste_concept == "buiging":

    vraag = """
Waarom wordt buiging sterker wanneer een spleet smaller wordt?
"""

    goed_antwoord = [
        "golflengte",
        "opening"
    ]

else:

    vraag = """
Wat wordt bedoeld met een foton?
"""

    goed_antwoord = [
        "lichtdeeltje",
        "energie"
    ]

print(vraag)

antwoord = input("Jouw antwoord: ")

score = 0

for woord in goed_antwoord:
    if woord.lower() in antwoord.lower():
        score += 1

print()

if score > 0:
    print("Goed bezig! Je antwoord bevat belangrijke begrippen.")
else:
    print("Dit antwoord mist belangrijke begrippen. Extra uitleg nodig.")