# -*- coding: utf-8 -*-

"""
Classe Dao[Teacher]
"""
from daos.dao import Dao
from models.teacher import Teacher
from dataclasses import dataclass
from typing import Optional

@dataclass
class TeacherDao(Dao[Teacher]):
    def create(self, teacher: Teacher) -> int:
        with Dao.connection.cursor() as cursor:
            sql = """
                INSERT INTO teacher (first_name, last_name, age, start_date)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql, (teacher.first_name, teacher.last_name, teacher.age, teacher.start_date))
            Dao.connection.commit()
            return cursor.lastrowid

    def read(self, id_teacher: int) -> Optional[Teacher]:
        """Renvoie l'enseignant correspondant à l'entité dont l'id est id_teacher"""
        with Dao.connection.cursor() as cursor:
            # Correction de la requête SQL et des noms de colonnes
            sql = "SELECT id_teacher, start_date, id_person FROM teacher WHERE id_teacher=%s"
            cursor.execute(sql, (id_teacher,))
            result = cursor.fetchone()
            if result:
                id_teacher, start_date, id_person = result['id_teacher'], result['start_date'], result['id_person']
                # Création d'un objet Teacher avec les données récupérées
                teacher = Teacher(first_name=None, last_name=None, age=None, start_date=start_date)
                teacher.id = id_teacher
                # Vous pouvez définir d'autres attributs de Teacher si nécessaire
                return teacher
            return None

    def update(self, teacher: Teacher) -> bool:
        """Met à jour en BD l'entité Teacher correspondant à teacher"""
        with Dao.connection.cursor() as cursor:
            sql = "UPDATE teacher SET start_date=%s WHERE id_teacher=%s"
            cursor.execute(sql, (teacher.start_date, teacher.id))
            Dao.connection.commit()
            return cursor.rowcount > 0

    def delete(self, teacher: Teacher) -> bool:
        """Supprime en BD l'entité Teacher correspondant à teacher"""
        with Dao.connection.cursor() as cursor:
            sql = "DELETE FROM teacher WHERE id_teacher=%s"
            cursor.execute(sql, (teacher.id,))
            Dao.connection.commit()
            return cursor.rowcount > 0
