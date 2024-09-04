from models.person import Person
from daos.person_dao import PersonDao

# Créez un objet PersonDao
person_dao = PersonDao()

# Créez une nouvelle personne
new_person = Person(first_name="John", last_name="Doe", age=25)

# Test de création
person_id = person_dao.create(new_person)
print(f"New Person ID: {person_id}")

# Test de lecture
retrieved_person = person_dao.read(person_id)
if retrieved_person:
    print(f"Retrieved Person: {retrieved_person.first_name} {retrieved_person.last_name}, Age: {retrieved_person.age}")
else:
    print("Failed to retrieve person")

# Test de mise à jour
retrieved_person.first_name = "Jane"
retrieved_person.age = 30
update_success = person_dao.update(retrieved_person)
print(f"Person update successful: {update_success}")

# Vérification après la mise à jour
updated_person = person_dao.read(person_id)
if updated_person:
    print(f"Updated Person: {updated_person.first_name} {updated_person.last_name}, Age: {updated_person.age}")
else:
    print("Failed to retrieve updated person")

# Test de suppression
delete_success = person_dao.delete(updated_person)
print(f"Person delete successful: {delete_success}")

# Vérification après la suppression
deleted_person = person_dao.read(person_id)
if deleted_person:
    print(f"Failed to delete person. Person still exists: {deleted_person.first_name} {deleted_person.last_name}")
else:
    print("Person successfully deleted")

