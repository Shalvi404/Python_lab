class Discipline:
    def __init__(self, code, title, description):
        self._code = code
        self._title = title
        self.description = description
    @property
    def code(self): return self.code
    @property
    def title(self): return self.title
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
    def active(self): return self._is_expelled
    def description(self,specialty):
        return {k: dict(v) for k, v in self._description.items()}


