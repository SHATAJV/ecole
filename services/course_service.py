from daos.course_dao import CourseDao
from daos.teacher_dao import TeacherDao
from models.course import Course
from models.teacher import Teacher

class CourseService:
    def __init__(self):
        self.teacher_dao = TeacherDao()
        self.course_dao = CourseDao()

    def add_course_with_teacher(self, course: Course, teacher: Teacher):
        # Création de l'enseignant et récupération de son ID
        teacher_id = self.teacher_dao.create(teacher)

        # Définir l'ID de l'enseignant dans le cours
        course.teacher = teacher  # Assurez-vous que l'objet teacher est bien associé au cours

        # Création du cours avec l'enseignant
        course_id = self.course_dao.create(course)

        return course_id
