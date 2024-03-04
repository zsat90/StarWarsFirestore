from flask import Flask, request, jsonify
from model.planet_model import PlanetModel

app = Flask(__name__)
planet_model = PlanetModel()

# Add Planet
@app.route('planet', method=['POST'])
def add_planet():
    

# Get planet by id

# Update planet

# Delete planet

# Get list