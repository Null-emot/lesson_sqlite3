import sqlite3

# Подключение к базе данных
conn = sqlite3.connect("university.db")
cursor = conn.cursor()

# Функция добавления студента
def add_student():
    name = input("Ім'я студента: ")
    age = int(input("Вік студента: "))
    major = input("Спеціальність: ")
    cursor.execute("INSERT INTO students (name, age, major) VALUES (?, ?, ?)", (name, age, major))
    conn.commit()
    print("Студента додано.")

# Функция добавления курса
def add_course():
    name = input("Назва курсу: ")
    instructor = input("Викладач: ")
    cursor.execute("INSERT INTO courses (course_name, instructor) VALUES (?, ?)", (name, instructor))
    conn.commit()
    print("Курс додано.")

# Функция регистрации студента на курс
def register_student_to_course():
    student_id = int(input("ID студента: "))
    course_id = int(input("ID курсу: "))
    cursor.execute("INSERT INTO student_course (student_id, course_id) VALUES (?, ?)", (student_id, course_id))
    conn.commit()
    print("Студента зареєстровано на курс.")

# Функция отображения всех студентов
def list_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    print("\nСписок студентів:")
    for student in students:
        print(f"ID: {student[0]}, Ім'я: {student[1]}, Вік: {student[2]}, Спеціальність: {student[3]}")

# Функция отображения всех курсов
def list_courses():
    cursor.execute("SELECT * FROM courses")
    courses = cursor.fetchall()
    print("\nСписок курсів:")
    for course in courses:
        print(f"ID: {course[0]}, Назва: {course[1]}, Викладач: {course[2]}")

# Функция отображения студентов на курсе
def students_in_course():
    course_id = int(input("Введіть ID курсу: "))
    cursor.execute("""
        SELECT students.id, students.name, students.age, students.major 
        FROM students
        JOIN student_course ON students.id = student_course.student_id
        WHERE student_course.course_id = ?
    """, (course_id,))
    students = cursor.fetchall()
    
    cursor.execute("SELECT course_name FROM courses WHERE id = ?", (course_id,))
    course_name = cursor.fetchone()
    
    if course_name:
        print(f"\nСтуденти на курсі '{course_name[0]}':")
        for student in students:
            print(f"ID: {student[0]}, Ім'я: {student[1]}, Вік: {student[2]}, Спеціальність: {student[3]}")
    else:
        print("Курс не знайдено.")

# Главное меню
def main_menu():
    while True:
        print("\nМеню:")
        print("1. Додати студента")
        print("2. Додати курс")
        print("3. Зареєструвати студента на курс")
        print("4. Показати всіх студентів")
        print("5. Показати всі курси")
        print("6. Показати студентів для конкретного курсу")
        print("0. Вихід")

        choice = input("Оберіть опцію: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            add_course()
        elif choice == "3":
            register_student_to_course()
        elif choice == "4":
            list_students()
        elif choice == "5":
            list_courses()
        elif choice == "6":
            students_in_course()
        elif choice == "0":
            print("Вихід...")
            break
        else:
            print("Невірна команда.")
    
    conn.close()

# Инициализация базы данных и запуск меню
if __name__ == '__main__':
    main_menu()