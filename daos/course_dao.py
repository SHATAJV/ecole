# -*- coding: utf-8 -*-

"""
Classe Dao[Course]
"""
from daos.teacher_dao import TeacherDao
from models.course import Course
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional

@dataclass
class CourseDao:
    def create(self, course: Course) -> int:
        with Dao.connection.cursor() as cursor:
            sql = """
                INSERT INTO course (name, start_date, end_date, id_teacher)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql, (course.name, course.start_date, course.end_date, course.teacher.id if course.teacher else None))
            Dao.connection.commit()
            return cursor.lastrowid

    def read(self, id_course: int) -> Optional[Course]:
        """Renvoie le cours correspondant à l'entité dont l'id est id_course (ou None s'il n'a pu être trouvé)"""
        with Dao.connection.cursor() as cursor:
            sql = "SELECT id_course, name, start_date, end_date, id_teacher FROM course WHERE id_course=%s"
            cursor.execute(sql, (id_course,))
            result = cursor.fetchone()
            if result:
                id_course, name, start_date, end_date, id_teacher = \
                    result['id_course'], result['name'], result['start_date'], \
                        result['end_date'], result['id_teacher']
                course = Course(name=name, start_date=start_date, end_date=end_date)
                course.id = id_course
                if id_teacher:
                    teacher = TeacherDao().read(id_teacher)
                    course.set_teacher(teacher)
                return course
            return None
    def update(self, course: Course) -> bool:
        with Dao.connection.cursor() as cursor:
            sql = """
                UPDATE course 
                SET name=%s, start_date=%s, end_date=%s, id_teacher=%s 
                WHERE id_course=%s
            """
            cursor.execute(sql, (course.name, course.start_date, course.end_date, course.teacher.id if course.teacher else None, course.id))
            Dao.connection.commit()
            return cursor.rowcount > 0

    def delete(self, course: Course) -> bool:
        with Dao.connection.cursor() as cursor:
            sql = "DELETE FROM course WHERE id_course=%s"
            cursor.execute(sql, (course.id,))
            Dao.connection.commit()
            return cursor.rowcount > 0
