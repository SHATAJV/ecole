# -*- coding: utf-8 -*-

"""
Classe Dao[Teacher]
"""

from models.teacher import Teacher
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional


@dataclass
class TeacherDao(Dao[Teacher]):
    def create(self, teacher: Teacher) -> int:
        """Crée en BD l'entité Teacher correspondant à l'objet teacher

        :param teacher: Enseignant à créer sous forme d'entité Teacher en BD
        :return: l'id de l'entité insérée en BD (0 si la création a échoué)
        """
        with Dao.connection.cursor() as cursor:
            sql = "INSERT INTO teacher (id_teacher, start_date, id_person) VALUES (%s, %s, %s)"
            cursor.execute(sql, (teacher.id_teacher, teacher.start_date, teacher.id_person))
            Dao.connection.commit()
            return cursor.lastrowid

    def read(self, id_person: int) -> Optional[Teacher]:
        """Renvoie l'enseignant correspondant à l'entité dont l'id est id_person
           (ou None s'il n'a pu être trouvé)"""
        with Dao.connection.cursor() as cursor:
            sql = "SELECT * FROM teacher WHERE id_person=%s"
            cursor.execute(sql, (id_person,))
            result = cursor.fetchone()
            if result:
                return Teacher(*result)
            return None

    def update(self, teacher: Teacher) -> bool:
        """Met à jour en BD l'entité Teacher correspondant à teacher

        :param teacher: Enseignant déjà mis à jour en mémoire
        :return: True si la mise à jour a pu être réalisée
        """
        with Dao.connection.cursor() as cursor:
            sql = "UPDATE teacher SET id_teacher=%s, start_date=%s WHERE id_person=%s"
            cursor.execute(sql, (teacher.id_teacher, teacher.start_date, teacher.id_person))
            Dao.connection.commit()
            return cursor.rowcount > 0

    def delete(self, teacher: Teacher) -> bool:
        """Supprime en BD l'entité Teacher correspondant à teacher

        :param teacher: Enseignant dont l'entité Teacher correspondante est à supprimer
        :return: True si la suppression a pu être réalisée
        """
        with Dao.connection.cursor() as cursor:
            sql = "DELETE FROM teacher WHERE id_person=%s"
            cursor.execute(sql, (teacher.id_person,))
            Dao.connection.commit()
            return cursor.rowcount > 0
