class Discipline:
    def __init__(self, code, title):
        self._code = code
        self._title = title
    @property
    def code(self): return self._code
    @property
    def title(self): return self._title
    def __str__(self):
        return f'{self.code}--{self.title}'
class Department:
    def __init__(self,name):
        self._name = name
        self._course={} # (специальность, code дисциплины)= дисциплина
    def add_course(self,specialty,discipline):
        self._course[(specialty,discipline.code)]=discipline
    def read_for(self,specialty,code):
        return (specialty,code) in self._course
    def get(self,specialty,code):
        return self._course.get((specialty,code))
    def discipline_specialty(self,specialty):
        return [d for (s, _), d in self._course.items() if s == specialty]
    def all_disciplines(self):
        return list(self._course.values())
class Student:
    def __init__(self,stud_id,name,specialty):
        self._stud_id = stud_id
        self._name = name
        self._specialty = specialty
        self._semester = 1
        self._is_expelled=False
        self._description = {} #code дисциплины ={дисциплина, специальность, оценка}

    @property
    def id(self): return self._stud_id
    @property
    def name(self): return self._name
    @property
    def spec(self): return self._specialty
    @property
    def semester(self): return self._semester
    @property
    def is_expelled(self): return self._is_expelled
    def description(self):
        return {k: dict(v) for k, v in self._description.items()}
class Faculty:
    def __init__(self,name):
        self._name = name
        self._departments=[] #список кафедр
        self._students={} # айди студента:студент
    def add_student(self,stud_id,name,specialty):
        if stud_id in self._students:
            raise ValueError(f'Student with id {stud_id} already exists')
        s=Student(stud_id,name,specialty)
        self._students[stud_id]=s
    def get_student(self,stud_id):
        s=self._students.get(stud_id)
        if s is None:
            raise ValueError(f'Student with id {stud_id} does not exist')
        return s
    def expel_student(self,stud_id):
        s = self.get_student(stud_id)
        if s.is_expelled:
            raise ValueError(f'Student with id {stud_id} already expelled')
        s._is_expelled=True
        s.description.clear()
    def reading_department(self,specialty,code):
       for d in self._departments:
           if d.read_for(specialty,code):
               return d
       return None
    def add_to_discipline(self,stud_id,code):
        s=self.get_student(stud_id)
        if s.is_expelled:
            raise ValueError(f'Student with id {stud_id} expelled')
        dept = self.reading_department(s.spec, code)
        if dept is None:
            raise ValueError(f'Discipline {dept} is not being taught for {s.spec}')
        if code in s.description:
            raise ValueError(f'{s.name} already written at {code}')
        s.description[code] = {"discipline": dept.get(s.specialty, code),
                           "department": dept.name, "grade": None}
    def remove_from_discipline(self,stud_id,code):
        s=self.get_student(stud_id)
        if code not in s.description:
            raise ValueError(f'{s.name} not written at {code}')
        del s.description[code]
    def set_grade(self,stud_id,code,grade):
        s=self.get_student(stud_id)
        if code not in s.description:
            raise ValueError(f'{s.name} not written at {code}')
        if type(grade) != int or not 0<grade<=10:
            raise ValueError(f'{grade} cannot be writen as grade')
        if s.description[code]["grade"] is not None:
            raise ValueError(f'Grade is already written')
        s.description[code]["grade"]=grade
    def next_semester(self,stud_id):
        s=self.get_student(stud_id)
        if s.is_expelled:
            raise ValueError(f'Student with id {stud_id}  expelled')
        if not s.description:
            raise ValueError(f'Student with id {stud_id} has no disciplines')
        pending = [data["discipline"] for code, data in s._description.items() if data["grade"] is None]
        if pending:
            raise ValueError(f'No grade in:{pending}')
        failed = [data["discipline"] for code, data in s._description.items() if data["grade"] <= 4]
        if failed:
            raise ValueError(f'Grade that <=4 in:{failed}')
        s._semester += 1
        s._description.clear()

    def report_student(self, stud_id, filename=None):
        s = self.get_student(stud_id)
        if filename is None:
            filename = f"student_{stud_id}.txt"
        lines = [
            f"ФИО:{s.name}",
            f"ID:{s.id}",
            f"Специальность:{s.spec}",
            f"Семестр:{s.semester}",
            f"Статус:{'отчислен' if s.is_expelled else 'активен'}",
        ]
        if not s.description():
            lines.append("Нет записей о дисциплинах.")
        else:
            for code, data in s.description().items():
                grade = data["grade"] if data["grade"] is not None else "—"
                lines.append(f"{data['discipline']} | Кафедра: {data['department']} | Оценка: {grade}")
        grades = [data["grade"] for data in s.description().values() if data["grade"] is not None]
        if grades:
            avg = sum(grades) / len(grades)
            lines.append(f"Средний балл: {avg:.2f}")
        else:
            lines.append("Средний балл: —")
        with open(filename, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        return filename


