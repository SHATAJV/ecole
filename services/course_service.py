from daos.course_dao import CourseDao
from daos.teacher_dao import TeacherDao
from models.course import Course
from models.teacher import Teacher

class CourseService:
    def __init__(self):
        self.teacher_dao = TeacherDao()
        self.course_dao = CourseDao()

    def add_course_with_teacher(self, course: Course, teacher: Teacher) -> int:
        course.set_teacher(teacher)
        course_id = CourseDao().create(course)
        return course_id
