import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("service_account.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

star_wars_characters = [
    {"name": "Luke Skywalker", "height": "172", "hair_color": "blond", "eye_color": "blue", "birth_year": "19BBY", "species": "Human", "homeworld": "Tatooine"},
    {"name": "Leia Organa", "height": "150", "hair_color": "brown", "eye_color": "brown", "birth_year": "19BBY", "species": "Human", "homeworld": "Alderaan"},
    {"name": "Han Solo", "height": "180", "hair_color": "brown", "eye_color": "brown", "birth_year": "29BBY", "species": "Human", "homeworld": "Corellia"},
    {"name": "Chewbacca", "height": "228", "hair_color": "brown", "eye_color": "blue", "birth_year": "200BBY", "species": "Wookiee", "homeworld": "Kashyyyk"},
    {"name": "Darth Vader", "height": "202", "hair_color": "none", "eye_color": "yellow", "birth_year": "41.9BBY", "species": "Human", "homeworld": "Tatooine"},
    {"name": "Yoda", "height": "66", "hair_color": "white", "eye_color": "green", "birth_year": "896BBY", "species": "Yoda's species", "homeworld": "unknown"},
    {"name": "Obi-Wan Kenobi", "height": "182", "hair_color": "auburn, white", "eye_color": "blue-gray", "birth_year": "57BBY", "species": "Human", "homeworld": "Stewjon"},
    {"name": "R2-D2", "height": "96", "hair_color": "none", "eye_color": "red", "birth_year": "33BBY", "species": "Droid", "homeworld": "Naboo"},
    {"name": "C-3PO", "height": "167", "hair_color": "none", "eye_color": "yellow", "birth_year": "112BBY", "species": "Droid", "homeworld": "Tatooine"},
    {"name": "Boba Fett", "height": "183", "hair_color": "black", "eye_color": "brown", "birth_year": "31.5BBY", "species": "Human", "homeworld": "Kamino"}
]

# Ran this to add the list of characters into Firestore
for character in star_wars_characters:
    db.collection('people').add(character)


star_wars_planets = [
    {"name": "Tatooine", "climate": "arid", "gravity": "1 standard", "terrain": "desert", "population": "200000"},
    {"name": "Alderaan", "climate": "temperate", "gravity": "1 standard", "terrain": "grasslands, mountains", "population": "2000000000"},
    {"name": "Naboo", "climate": "temperate", "gravity": "1 standard", "terrain": "grassy hills, swamps, forests, mountains", "population": "4500000000"},
    {"name": "Bespin", "climate": "temperate", "gravity": "1.5 (surface), 0 (Cloud City)", "terrain": "gas giant", "population": "6000000"},
    {"name": "Endor", "climate": "temperate", "gravity": "0.85 standard", "terrain": "forests, mountains, lakes", "population": "30000000"},
    {"name": "Hoth", "climate": "frozen", "gravity": "1.1 standard", "terrain": "tundra, ice caves, mountain ranges", "population": "unknown"},
    {"name": "Dagobah", "climate": "murky", "gravity": "N/A", "terrain": "swamp, jungles", "population": "unknown"},
    {"name": "Coruscant", "climate": "temperate", "gravity": "1 standard", "terrain": "cityscape, mountains", "population": "1 trillion"},
    {"name": "Kamino", "climate": "temperate", "gravity": "1 standard", "terrain": "ocean", "population": "1000000000"},
    {"name": "Mustafar", "climate": "hot", "gravity": "1 standard", "terrain": "volcanoes, lava rivers, mountains, caves", "population": "20000"}
]


# Ran this to add the list of planets in Firestore
for planet in star_wars_planets:
    db.collection('planets').add(planet)








