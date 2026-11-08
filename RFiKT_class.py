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
    @property
    def name(self):return self._name
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
    def __str__(self):
        return f'{self._stud_id}:{self.name}'
class Faculty:
    def __init__(self,name):
        self._name = name
        self._departments=[] #список кафедр
        self._students={} # айди студента:студент

    def add_department(self, department):
        self._departments.append(department)
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
        s._description.clear()
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
            raise ValueError(f'Discipline {code} is not being taught for {s.spec}')
        if code in s._description:
            raise ValueError(f'{s.name} already written at {code}')
        s._description[code] = {"discipline": dept.get(s.spec, code),
                           "department": dept.name, "grade": None}
    def remove_from_discipline(self,stud_id,code):
        s=self.get_student(stud_id)
        if code not in s._description:
            raise ValueError(f'{s.name} not written at {code}')
        del s._description[code]
    def set_grade(self,stud_id,code,grade):
        s=self.get_student(stud_id)
        if code not in s._description:
            raise ValueError(f'{s.name} not written at {code}')
        if type(grade) != int or not 0<grade<=10:
            raise ValueError(f'{grade} cannot be writen as grade')
        if s._description[code]["grade"] is not None:
            raise ValueError(f'Grade is already written')
        s._description[code]["grade"]=grade
    def next_semester(self,stud_id):
        s=self.get_student(stud_id)
        if s.is_expelled:
            raise ValueError(f'Student with id {stud_id}  expelled')
        if not s._description:
            raise ValueError(f'Student with id {stud_id} has no disciplines')
        pending = [str(data["discipline"]) for code, data in s._description.items() if data["grade"] is None]
        if pending:
            raise ValueError(f'No grade in:{','.join(pending)}')
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
            f"Статус:{'отчислен' if s.is_expelled else 'не отчислен'}",
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

    def report_discipline(self, code, filename=None):
        found_discipline = None
        dept_name = None
        for dept in self._departments:
            for d in dept.all_disciplines():
                if d.code == code:
                    found_discipline = d
                    dept_name = dept.name
                    break
            if found_discipline:
                break
        if not found_discipline:
            raise ValueError(f"Дисциплина с кодом {code} нету.")
        if filename is None:
            filename = f"discipline_{code}.txt"
        students_data = []
        for s in self._students.values():
            desc = s.description()
            if code in desc and desc[code]["grade"] is not None:
                students_data.append((s.name, desc[code]["grade"]))
        lines = [
            f"Дисциплина: {found_discipline.title}",
            f"Код:        {found_discipline.code}",
            f"Кафедра:    {dept_name}",
        ]
        if not students_data:
            lines.append("Нет студентов, изучающих дисциплину.")
        else:
            total_grades = sum(grade for _, grade in students_data)
            avg = total_grades / len(students_data)
            lines.append(f"Средний балл: {avg:.2f}")
            lines.append(f"Количество студентов: {len(students_data)}")
            for name, grade in students_data:
                lines.append(f"{name:<30} | {grade}")
        with open(filename, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        return filename
def start():
    f = Faculty("РФиКТ")
    pi = Department("Прикладная информатика")
    kb = Department("Кибербезопасность")
    rf = Department("Радиофизика")
    ai = Department("Интеллектуальные системы")
    prog = Discipline("PI01", "Программирование с++")
    al = Discipline("PI02", "Алгоритмы")
    mathan = Discipline("KB01", "Матанализ")
    kiber = Discipline("KB02", "Кибербезопастность")
    phys = Discipline("RF01", "Механика")
    java = Discipline("RF02", "Программирование java")
    isbel = Discipline("AI01", "История Беларуси")
    eng = Discipline("AI02", "Английский язык")
    pi.add_course("прикладная информатика", prog)
    pi.add_course("прикладная информатика", al)
    kb.add_course("кибербезопасность", mathan)
    kb.add_course("кибербезопасность", kiber)
    ai.add_course("интеллектуальные системы", isbel)
    ai.add_course("интеллектуальные системы", eng)
    rf.add_course("радиофизика", phys)
    rf.add_course("радиофизика", java)
    pi.add_course("радиофизика",eng)
    for d in (pi,kb, rf, ai):
        f.add_department(d)
    f.add_student("S001", "Шивилько Алексей", "прикладная информатика")
    f.add_student("S002", "Синоженский Дмитрий", "кибербезопасность")
    f.add_student("S003", "Субачус Никита", "интеллектуальные системы")
    f.add_student("S004", "Пацыкалик Илья", "радиофизика")
    return f
def menu():
    print("""
 1. Список студентов
 2. Зачислить студента
 3. Отчислить студента
 4. Дисциплины специальности студента
 5. Записать на дисциплину
 6. Убрать с дисциплины
 7. Выставить оценку
 8. Перевести в следующий семестр
 9. Инфо о студенте
10. Ведомость по студенту
11. Ведомость по дисциплине
 0. Выход""")
def write(p): return input(p).strip()
def main():
    f = start()
    while True:
        menu()
        choice = write("Выберите действие: ")
        try:
            if choice == "0":
                break
            elif choice == "1":
                print("Список студентов:")
                for s in f._students.values():
                    print(s)
            elif choice == "2":
                stud_id = write("ID студента: ")
                name = write("ФИО: ")
                spec = write("Специальность: ")
                f.add_student(stud_id, name, spec)
                print(f"Студент {name} зачислен.")
            elif choice == "3":
                stud_id = write("ID студента: ")
                f.expel_student(stud_id)
                print(f"Студент {stud_id} отчислен.")
            elif choice == "4":
                stud_id = write("ID студента: ")
                s = f.get_student(stud_id)
                print(f"\nДисциплины для «{s.spec}»:")
                found = False
                for dept in f._departments:
                    for d in dept.discipline_specialty(s.spec):
                        print(f"  {d} (читает кафедра: {dept._name})")
                        found = True
                if not found:
                    print("нет доступных дисциплин")
            elif choice == "5":
                stud_id = write("ID студента: ")
                code = write("Код дисциплины: ")
                f.add_to_discipline(stud_id, code)
                print(f"Студент {stud_id} записан на {code}.")
            elif choice == "6":
                stud_id = write("ID студента: ")
                code = write("Код дисциплины: ")
                f.remove_from_discipline(stud_id, code)
                print(f"Студент {stud_id} удалeн с дисциплины {code}.")
            elif choice == "7":
                stud_id = write("ID студента: ")
                code = write("Код дисциплины: ")
                raw_grade = write("Оценка (1-10): ")
                try:
                    grade = int(raw_grade)
                except ValueError:
                    raise ValueError(f"Введите целое число.")
                f.set_grade(stud_id, code, grade)
                print(f"Оценка {grade} выставлена.")
            elif choice == "8":
                stud_id = write("ID студента: ")
                f.next_semester(stud_id)
                print(f"Студент переведён на следующий семестр.")
            elif choice == "9":
                stud_id = write("ID студента: ")
                s = f.get_student(stud_id)
                print(f"Инфо о студенте")
                print(f"ID: {s.id} | ФИО: {s.name} | Спец: {s.spec}")
                print(f"Семестр: {s.semester} | Статус: {'отчислен' if s.is_expelled else 'активен'}")
                print("Дисциплины:")
                if not s.description():
                    print("нет дисциплин")
                for code, data in s.description().items():
                    g = data["grade"] if data["grade"] is not None else "—"
                    print(f"  {data['discipline']} | Кафедра: {data['department']} | Оценка: {g}")
            elif choice == "10":
                stud_id = write("ID студента: ")
                filename = f.report_student(stud_id)
                print(f"Ведомость успешно сохранена в файл: {filename}")
            elif choice == "11":
                code = write("Код дисциплины: ")
                filename = f.report_discipline(code)
                print(f"Ведомость по дисциплине сохранена в файл: {filename}")
            else:
                print("Попробуйте снова.")
        except ValueError as e:
           print(f"\nОШИБКА: {e}\n")
if __name__ == "__main__":
    main()