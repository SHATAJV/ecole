# -*- coding: utf-8 -*-

"""
Classe Dao[Person]
"""

from models.person import Person
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional


@dataclass
class PersonDao(Dao[Person]):
    def create(self, person: Person) -> int:
        """Crée en BD l'entité Person correspondant à l'objet person

        :param person: Personne à créer sous forme d'entité Person en BD
        :return: l'id de l'entité insérée en BD (0 si la création a échoué)
        """

        with Dao.connection.cursor() as cursor:
                sql = "INSERT INTO person (first_name, last_name, age) VALUES (%s, %s, %s)"
                cursor.execute(sql, (person.first_name, person.last_name, person.age))
                Dao.connection.commit()
                return cursor.lastrowid
    def read(self, id_person: int) -> Optional[Person]:
        """Renvoie la personne correspondant à l'entité dont l'id est id_person."""
        with Dao.connection.cursor() as cursor:
            sql = "SELECT id_person, first_name, last_name, age FROM person WHERE id_person=%s"
            cursor.execute(sql, (id_person,))
            result = cursor.fetchone()
            if result:
                return Person(
                    id_person=result['id_person'],
                    first_name=result['first_name'],
                    last_name=result['last_name'],
                    age=result['age']
                )
            return None

    def update(self, person: Person) -> bool:
        """Met à jour en BD l'entité Person correspondant à person."""
        with Dao.connection.cursor() as cursor:
            sql = "UPDATE person SET first_name=%s, last_name=%s, age=%s WHERE id_person=%s"
            cursor.execute(sql, (person.first_name, person.last_name, person.age, person.id_person))
            Dao.connection.commit()
            return cursor.rowcount > 0

    def delete(self, person: Person) -> bool:
        """Supprime en BD l'entité Person correspondant à person."""
        with Dao.connection.cursor() as cursor:
            sql = "DELETE FROM person WHERE id_person=%s"
            cursor.execute(sql, (person.id_person,))
            Dao.connection.commit()
            return cursor.rowcount > 0