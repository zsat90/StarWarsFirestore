from flask import Flask, request, jsonify
from model.planet_model import PlanetModel

app = Flask(__name__)
planet_model = PlanetModel()


# Add Planet
def add_planet():
    planet_data = request.json
    result, error = planet_model.add_planet(planet_data)
    if error:
        return jsonify({"Error": error}), 400
    return jsonify({"message": "Planet added successfully", "planet_id": result[1].id}), 201


# Get planet by id
def get_planet_by_id(planet_id):
    result, error = planet_model.get_planet_by_id(planet_id)
    if error:
        return jsonify({"Error": error}), 404
    return jsonify(result), 200


# Update planet
def update_planet(planet_id):
    update_data = request.json
    result, error = planet_model.update_planet(planet_id, update_data)
    if error:
        return jsonify({"Error": error}), 400
    return jsonify({"message": "Planet updated successfully", "planet": result}), 200


# Delete planet
def delete_planet(planet_id):
    message, error = planet_model.delete_planet(planet_id)
    if error:
        return jsonify({"error": error}), 400
    return jsonify({"message": message}), 200


# Get list
def get_planets():
    result, error = planet_model.list_planets()
    if error:
        return jsonify({"error": error}), 500
    return jsonify(result), 200


if __name__ == '__main__':
    app.run(debug=True)
