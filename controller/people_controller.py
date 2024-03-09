from flask import Flask, request, jsonify
from model.people_model import PeopleModel

app = Flask(__name__)
people_model = PeopleModel()


# Add a person
def add_person():
    person_data = request.json
    result, error = people_model.add_person(person_data)
    if error:
        return jsonify({"Error": error}), 400
    return jsonify({"message": "Person added successfully", "person_id": result[1].id}), 201


# Get person by id
def get_person(person_id):
    result, error = people_model.get_by_id(person_id)
    if error:
        return jsonify({"Error": error}), 404
    return jsonify(result), 200


# Update a person
def update_person(person_id):
    update_data = request.json
    result, error = people_model.update_person(person_id, update_data)
    if error:
        return jsonify({"Error": error}), 400
    return jsonify({"message": "Person updated successfully", "person": result}), 200


# Delete a person
def delete_person(person_id):
    message, error = people_model.delete_person(person_id)
    if error:
        return jsonify({"error": error}), 400
    return jsonify({"message": message}), 200


# Get list
def get_people():
    result, error = people_model.get_people()
    if error:
        return jsonify({"error": error}), 500
    return jsonify(result), 200


if __name__ == '__main__':
    app.run(debug=True)
