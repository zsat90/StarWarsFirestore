from firebase_admin import firestore


class PeopleModel:
    def __init__(self):
        self.db = firestore.client()
        self.collection = self.db.collection('people')

    # add person
    def add_person(self, person_data):
        try:
            return self.collection.add(person_data), None
        except Exception as e:
            return None, str(e)

    # get person by id
    def get_by_id(self, person_id):
        try:
            ref_to_id = self.collection.document(person_id)
            doc = ref_to_id.get()
            if doc.exists:
                return doc.to_dict(), None
            else:
                return None, "Person not found"
        except Exception as e:
            return None, str(e)

    # update a person
    def update_person(self, person_id, update_data):
        try:
            ref_to_id = self.collection.document(person_id)
            ref_to_id.update(update_data)
            return ref_to_id.get().to_dict(), None
        except Exception as e:
            return None, str(e)

    # delete a person
    def delete_person(self, person_id):
        try:
            self.collection.document(person_id).delete()
            return "Person deleted successfully", None
        except Exception as e:
            return None, str(e)

    # get people list
    def get_people(self):
        try:
            people = self.collection.stream()
            return [doc.to_dict() for doc in people], None
        except Exception as e:
            return None, str(e)
