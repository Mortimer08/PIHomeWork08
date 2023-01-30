def classes_list(local_classes_dict):
    print('\nКлассы в базе')
    for class_number, class_name in local_classes_dict.items():
        print(f'\t{class_number}. {class_name}')
    print(f'\t0. Выход')


def choosen_class_number() -> int:
    while True:
        class_number = input('\nВыберите номер класса для работы: ')
        if class_number.isdigit():
            return int(class_number)


def choosen_subject(class_data: dict) -> str:
    print()
    print('Предметы:\n')
    subjects = []
    for number, subject in enumerate(class_data.keys(), 1):
        print(f'\t{number}. {subject}')
        subjects.append([number, subject])
    print(f'\t0. Выход')
    while True:
        subject_number = input('\nВыберите номер предмета для работы: ')

        if subject_number.isdigit():
            if subject_number == '0':
                return 'Выход'
            elif int(subject_number) <= len(subjects):
                return subjects[int(subject_number)-1][1]


def choosen_student(subject_data: dict) -> str:
    print()
    print('Ученики:\n')
    students = []
    for number, student in enumerate(subject_data.keys(), 1):
        print(f'\t{number}. {student}')
        students.append([number, student])
    print(f'\t0. Выход')
    while True:
        student_number = input('\nВыберите номер ученика для работы: ')
        if student_number.isdigit():
            if student_number == '0':
                return 'Выход'
            elif int(student_number) <= len(students):
                return str(students[int(student_number)-1][1])


def show_choosen_student(local_student_name: str, grades):
    print(f'\n{local_student_name}: {", ".join(grades)}')


def student_newgrade():
    newgrade = 0
    while int(newgrade) < 1 or int(newgrade) > 5:
        newgrade = input('\nКакую оценку поставить? ')
        if newgrade.isdigit():
            return newgrade
