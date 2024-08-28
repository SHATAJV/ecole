from datetime import date
from models.adress import Adress
from models.course import Course
from models.teacher import Teacher
from models.student import Student
from business.school import School
from services.course_service import CourseService

def init_school(school: School) -> None:
    """Initialisation d'un jeu de test pour l'école school."""
    # Création des étudiants et rattachement à leur adresse
    paul = Student('Paul', 'Dubois', 12)
    valerie = Student('Valérie', 'Dumont', 13)
    louis = Student('Louis', 'Berthot', 11)

    paul.address = Adress('12 rue des Pinsons', 'Castanet', 31320)  # Correction du nom de la classe
    valerie.address = Adress('43 avenue Jean Zay', 'Toulouse', 31200)  # Correction du nom de la classe
    louis.address = Adress('7 impasse des Coteaux', 'Cornebarrieu', 31150)  # Correction du nom de la classe

    # Ajout des étudiants à l'école
    for student in [paul, valerie, louis]:
        school.add_student(student)

    # Création des cours
    francais = Course(name="Français", start_date=date(2024, 1, 29), end_date=date(2024, 2, 16))
    histoire = Course(name="Histoire", start_date=date(2024, 2, 5), end_date=date(2024, 2, 16))
    geographie = Course(name="Géographie", start_date=date(2024, 2, 5), end_date=date(2024, 2, 16))
    mathematiques = Course(name="Mathématiques", start_date=date(2024, 2, 12), end_date=date(2024, 3, 8))
    physique = Course(name="Physique", start_date=date(2024, 2, 19), end_date=date(2024, 3, 8))
    chimie = Course(name="Chimie", start_date=date(2024, 2, 26), end_date=date(2024, 3, 15))
    anglais = Course(name="Anglais", start_date=date(2024, 2, 12), end_date=date(2024, 2, 24))
    sport = Course(name="Sport", start_date=date(2024, 3, 4), end_date=date(2024, 3, 15))

    # Ajout des cours à l'école
    for course in [francais, histoire, geographie, mathematiques, physique, chimie, anglais, sport]:
        school.add_course(course)

    # Création des enseignants
    victor = Teacher(first_name='Victor', last_name='Hugo', age=23, start_date=date(2023, 9, 4))
    jules = Teacher(first_name='Jules', last_name='Michelet', age=32, start_date=date(2023, 9, 4))
    sophie = Teacher(first_name='Sophie', last_name='Germain', age=25, start_date=date(2023, 9, 4))
    marie = Teacher(first_name='Marie', last_name='Curie', age=31, start_date=date(2023, 9, 4))
    william = Teacher(first_name='William', last_name='Shakespeare', age=34, start_date=date(2023, 9, 4))
    michel = Teacher(first_name='Michel', last_name='Platini', age=42, start_date=date(2023, 9, 4))

    # Ajout des enseignants à l'école
    for teacher in [victor, jules, sophie, marie, william, michel]:
        school.add_teacher(teacher)

    # Association des élèves aux cours qu'ils suivent
    for course in [geographie, physique, anglais]:
        paul.add_course(course)

    for course in [francais, histoire, chimie]:
        valerie.add_course(course)

    for course in [mathematiques, physique, geographie, sport]:
        louis.add_course(course)

    # Association des enseignants aux cours qu'ils enseignent
    victor.add_course(francais)
    jules.add_course(histoire)
    jules.add_course(geographie)
    sophie.add_course(mathematiques)
    marie.add_course(physique)
    marie.add_course(chimie)
    william.add_course(anglais)
    michel.add_course(sport)

def main() -> None:
    """Programme principal."""
    print("""\
--------------------------
Bienvenue dans notre école
--------------------------""")

    school = School()

    # Initialisation d'un ensemble de cours, enseignants et élèves composant l'école
    init_school(school)

    # Affichage de la liste des cours, leur enseignant et leurs élèves
    school.display_courses_list()

    # Exemple d'affichage des détails de certains cours par ID
    print(school.get_course_by_id(1))
    print(school.get_course_by_id(2))
    print(school.get_course_by_id(3))

    # Création d'un enseignant avec tous les arguments nécessaires
    teacher = Teacher(first_name="John", last_name="Doe", age=30, start_date=date(2022, 9, 1))

    # Création d'un cours avec tous les arguments nécessaires
    course = Course(name="Data Science", start_date=date(2023, 1, 1), end_date=date(2023, 6, 1))

    # Associer l'enseignant au cours
    course.set_teacher(teacher)

    # Utilisation du service pour ajouter le cours avec l'enseignant
    service = CourseService()

    try:
        course_id = service.add_course_with_teacher(course, teacher)
        print(f"New Course ID: {course_id}")
    except Exception as e:
        print(f"An error occurred while adding the course with teacher: {e}")

if __name__ == '__main__':
    main()
