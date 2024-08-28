from daos.course_dao import CourseDao
from daos.teacher_dao import TeacherDao
from models.course import Course
from models.teacher import Teacher

class CourseService:
    def __init__(self):
        self.teacher_dao = TeacherDao()
        self.course_dao = CourseDao()

    def add_course_with_teacher(self, course: Course, teacher: Teacher) -> int:
        # Assurez-vous que l'enseignant a un ID valide
        if teacher.id is None:
            try:
                # Enregistrez d'abord l'enseignant
                teacher_id = self.teacher_dao.create(teacher)
                teacher.id = teacher_id
            except Exception as e:
                print(f"An error occurred while saving the teacher: {e}")
                return -1  # Indique un échec

        # Associe l'enseignant au cours
        course.set_teacher(teacher)

        # Crée le cours dans la base de données
        try:
            course_id = self.course_dao.create(course)
            return course_id
        except Exception as e:
            print(f"An error occurred while adding the course with teacher: {e}")
            return -1  # Indique un échec
