from pathlib import Path
import os
uni_path = Path('PIHomeWork08', 'lists')
classes_names = {}
class_data = {}


def reab_db(current_class_name: str):
    global class_data
    current_file_name = current_class_name+'.txt'
    path = Path(uni_path, current_file_name)
    with open(path, 'r', encoding='UTF-8') as file:
        file_data = file.read()
        class_summary_data = list(
            filter(lambda x: (x != ''), file_data.replace('\n', '').split('#')))

        for subject in class_summary_data:
            subject_summary_data = subject.split(':')
            subject_name = subject_summary_data[0]
            subject_data = list(
                filter(lambda x: (x != ''), subject_summary_data[1].split(')')))

            class_data[subject_name] = {}

            for student in subject_data:
                student_summary_data = student.split('(')

                student_name = student_summary_data[0]
                student_grades = student_summary_data[1].split(',')
                class_data[subject_name][student_name] = student_grades


def get_students_grades(local_subject, local_student):
    local_grades = class_data[local_subject][local_student]
    return local_grades


def add_grade(local_subject: str, local_student: str, local_grade: str):
    class_data[local_subject][local_student].append(local_grade)


def write_db(current_class_name: str):
    global class_data
    current_file_name = current_class_name+'.txt'
    # current_file_name = '1.txt'
    path = Path(uni_path, current_file_name)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write('#\n')
        for subject, students in class_data.items():
            file.write(f'{subject}:\n')
            for student, grades in students.items():
                file.write(f'{student}({",".join(grades)})\n')
            file.write('#\n')


def get_classes_names(current_path: str):
    files_list = os.listdir(current_path)
    global classes_names
    for file_number, file_name in enumerate(files_list,1):
        classes_names[file_number] = file_name.split('.')[0]
