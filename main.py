from config.firebase_config import init_firebase

init_firebase()

from controller.people_controller import add_person, get_person, update_person, delete_person, get_people
from controller.planet_controller import add_planet, get_planet_by_id, update_planet, delete_planet, get_planets
from flask import Flask

app = Flask(__name__)

# url rules for people
app.add_url_rule('/people', view_func=add_person, methods=['POST'])
app.add_url_rule('/people/<person_id>', view_func=get_person, methods=['GET'])
app.add_url_rule('/people/<person_id>', view_func=update_person, methods=['PUT'])
app.add_url_rule('/people/<person_id>', view_func=delete_person, methods=['DELETE'])
app.add_url_rule('/people', view_func=get_people, methods=['GET'])

# url rules for planets
app.add_url_rule('/planet', view_func=add_planet, methods=['POST'])
app.add_url_rule('/planet/<planet_id>', view_func=get_planet_by_id, methods=['GET'])
app.add_url_rule('/planet/<planet_id>', view_func=update_planet, methods=['PUT'])
app.add_url_rule('/planet/<planet_id>', view_func=delete_planet, methods=['DELETE'])
app.add_url_rule('/planet', view_func=get_planets, methods=['GET'])

if __name__ == '__main__':
    app.run(debug=True)

