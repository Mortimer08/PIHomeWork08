import view
import model


def start():
    model.get_classes_names(model.uni_path)
    while True:
        view.classes_list(model.classes_names)

        choosen_class_number = view.choosen_class_number()
        if choosen_class_number in model.classes_names.keys():
            model.reab_db(model.classes_names[choosen_class_number])
            choosen_subject = view.choosen_subject(model.class_data)
            if choosen_subject != 'Выход':
                choosen_student = view.choosen_student(model.class_data[choosen_subject])
                if choosen_student != 'Выход':
                    student_grades = model.get_students_grades(
                        choosen_subject, choosen_student)
                    view.show_choosen_student(choosen_student, student_grades)
                    student_newgrade = view.student_newgrade()
                    model.add_grade(choosen_subject, choosen_student, student_newgrade)
                    student_grades = model.get_students_grades(
                        choosen_subject, choosen_student)
                    view.show_choosen_student(choosen_student, student_grades)
                    model.write_db(model.classes_names[choosen_class_number])
        elif choosen_class_number == 0:
            exit()

