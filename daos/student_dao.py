# -*- coding: utf-8 -*-

"""
Classe Dao[Student]
"""

from models.student import Student
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional


@dataclass
class StudentDao(Dao[Student]):
    def create(self, student: Student) -> int:
        """Crée en BD l'entité Student correspondant à l'objet student

        :param student: Étudiant à créer sous forme d'entité Student en BD
        :return: l'id de l'entité insérée en BD (0 si la création a échoué)
        """
        with Dao.connection.cursor() as cursor:
            sql = "INSERT INTO student (student_nbr, id_person) VALUES (%s, %s)"
            cursor.execute(sql, (student.student_nbr, student.id_person))
            Dao.connection.commit()
            return cursor.lastrowid

    def read(self, id_person: int) -> Optional[Student]:
        """Renvoie l'étudiant correspondant à l'entité dont l'id est id_person
           (ou None s'il n'a pu être trouvé)"""
        with Dao.connection.cursor() as cursor:
            sql = "SELECT * FROM student WHERE id_person=%s"
            cursor.execute(sql, (id_person,))
            result = cursor.fetchone()
            if result:
                return Student(*result)
            return None

    def update(self, student: Student) -> bool:
        """Met à jour en BD l'entité Student correspondant à student

        :param student: Étudiant déjà mis à jour en mémoire
        :return: True si la mise à jour a pu être réalisée
        """
        with Dao.connection.cursor() as cursor:
            sql = "UPDATE student SET student_nbr=%s WHERE id_person=%s"
            cursor.execute(sql, (student.student_nbr, student.id_person))
            Dao.connection.commit()
            return cursor.rowcount > 0

    def delete(self, student: Student) -> bool:
        """Supprime en BD l'entité Student correspondant à student

        :param student: Étudiant dont l'entité Student correspondante est à supprimer
        :return: True si la suppression a pu être réalisée
        """
        with Dao.connection.cursor() as cursor:
            sql = "DELETE FROM student WHERE id_person=%s"
            cursor.execute(sql, (student.id_person,))
            Dao.connection.commit()
            return cursor.rowcount > 0
