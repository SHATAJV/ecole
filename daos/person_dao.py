# -*- coding: utf-8 -*-

"""
Classe Dao[Course]
"""

from models.person import Person
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional


@dataclass
class CourseDao(Dao[Person]):
    def create(self, person: Person) -> int:
        """Crée en BD l'entité Course correspondant au cours obj

        :param course: à créer sous forme d'entité Course en BD
        :return: l'id de l'entité insérée en BD (0 si la création a échoué)
        """
        with Dao.connection.cursor() as cursor:
            sql = "INSERT INTO course (first_name, last_name, age) VALUES (%s, %s, %s)"
            cursor.execute(sql, (person.first_name, person.last_name, person.age))
            Dao.connection.commit()
            return cursor.lastrowid


    def read(self, id_course: int) -> Optional[Person]:
        """Renvoit le cours correspondant à l'entité dont l'id est id_course
           (ou None s'il n'a pu être trouvé)"""
        with Dao.connection.cursor() as cursor:
            sql = "SELECT * FROM course WHERE id_person=%s"
            cursor.execute(sql, (id_person))
            result = cursor.fetchone()
        return result

    def update(self, course: Person) -> bool:
        """Met à jour en BD l'entité Course correspondant à course, pour y correspondre

        :param course: cours déjà mis à jour en mémoire
        :return: True si la mise à jour a pu être réalisée
        """
        with Dao.connection.cursor() as cursor:
            sql = "UPDATE course SET first_name=%s, last_name=%s, age=%s WHERE id_person=%s"

            cursor.execute(sql, (course.first_name, course.last_name, course.age))
            Dao.connection.commit()
            return cursor.rowcount > 0

    def delete(self, person: Person) -> bool:
        """Supprime en BD l'entité Course correspondant à course

        :param course: cours dont l'entité Course correspondante est à supprimer
        :return: True si la suppression a pu être réalisée
        """
        with Dao.connection.cursor() as cursor:
            sql = "DELETE FROM course WHERE id_course=%s"
            cursor.execute(sql, (person.id_person,))
            Dao.connection.commit()
            return cursor.rowcount > 0

