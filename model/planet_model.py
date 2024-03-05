from firebase_admin import firestore


class PlanetModel:
    def __init__(self):
        self.db = firestore.client()
        self.collection = self.db.collection('planets')

    # Add planet
    def add_planet(self, planet_data):
        try:
            return self.collection.add(planet_data), None
        except Exception as e:
            return None, str(e)

    # Get planet by id
    def get_planet_by_id(self, planet_id):
        try:
            ref_to_id = self.collection.document(planet_id)
            doc = ref_to_id.get()
            if doc.exists:
                return doc.to_dict(), None
            else:
                return None, "Planet not found"
        except Exception as e:
            return None, str(e)

    # Update planet
    def update_planet(self, planet_id, udpate_data):
        try:
            ref_to_id = self.collection.document(planet_id)
            ref_to_id.update(udpate_data)
            return ref_to_id.get().to_dict(), None
        except Exception as e:
            return None, str(e)

    # Delete planet
    def delete_planet(self, planet_id):
        try:
            self.collection.document(planet_id).delete()
            return "Planet deleted Successfully", None
        except Exception as e:
            return None, str(e)

    # Get planet list
    def list_planets(self):
        try:
            planets = self.collection.stream()
            return [doc.to_dict() for doc in planets], None
        except Exception as e:
            return None, str(e)
