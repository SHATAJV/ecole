from dataclasses import dataclass, field
from typing import List
from models.course import Course
from datetime import date

@dataclass
class Teacher:
    first_name: str
    last_name: str
    age: int
    start_date: date
    id: int = field(default=None)
    courses_teached: List[Course] = field(default_factory=list)

    def add_course(self, course: Course) -> None:
        """Ajoute un cours à la liste des cours enseignés par cet enseignant."""
        if course not in self.courses_teached:
            self.courses_teached.append(course)
            course.set_teacher(self)

    def __str__(self) -> str:
        """Renvoie une chaîne de caractères représentant l'enseignant."""
        return (f"Teacher(first_name={self.first_name}, "
                f"last_name={self.last_name}, "
                f"age={self.age}, "
                f"start_date={self.start_date}, "
                f"id={self.id})")

