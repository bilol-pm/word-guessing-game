# class Student:
#     def __init__(self,name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
#
#     def display_info(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#         print(f"Grade: {self.grade}")
#         print("-" * 20)
#
# class StudentManager:
#     def __init__(self):
#         self.students = []
#
#     def add_student(self):
#         name = input("Enter student name: ")
#         age = int(input("Enter student age: "))
#         grade = int(input("Enter student grade: "))
#         student = Student(name, age, grade)
#         self.students.append(student)
#         print("\nStudent added successfully!\n")
#
#     def show_students(self):
#         if not self.students:
#             print("No students found!")
#             return
#
#         print("\nStudents:")
#         for student in self.students:
#             student.display_info()
#
#     def search_student(self):
#         if not self.students:
#             print("No students found!")
#             return
#         user_search = input("Enter student name: ")
#         print("\nResults:")
#         for student in self.students:
#             if student.name.upper() == user_search.upper():
#                 print(f"Student name: {student.name}, student age: {student.age}, student grade: {student.grade}")
#
#     def delete_student(self):
#         if not self.students:
#             print("No students found!")
#             return
#
#         delete_choice = input("Enter student name: ")
#         for student in self.students:
#             if student.name.upper() == delete_choice.upper():
#                 self.students.remove(student)
#                 print("Student removed successfully!")
#
#
#
#
#
# manager = StudentManager()
# print('--------Welcome to the student manager.-------')
# while(True):
#     print("1. Add student")
#     print("2. Show student")
#     print("3. Search student")
#     print("4. Delete student")
#     print("5. Update student")
#     print("6. Exit")
#
#     choice = int(input('Enter your choice: '))
#     if choice == 1:
#         manager.add_student()
#     elif choice == 2:
#         manager.show_students()
#     elif choice == 3:
#         manager.search_student()
#     elif choice == 4:
#         manager.delete_student()
#         manager.show_students()
#
#
#         print("")

# user_input = input("Please enter a word: ")
#
# # for i in user_input:
# #     print(i)
# #
# # reversed_str = user_input[::-1]
# # print(reversed_str)
# #
# # for i in reversed_str:
# #     if user_input == reversed_str:
# #         print("Palindrome")
# #         break
# #     else:
# #         print("Not Palindrome")
# #     break
#
# is_palindrome = True
# length = len(user_input)
#
# for i in range(length // 2):
#     if user_input[i] != user_input[length - 1 - i]:
#         is_palindrome = False
#         break
#
# if is_palindrome:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

import random

word_hints = {
    "samalyot": "Temir qush",
    "olma": "Ilm mevasi",
    "kompyuter": "Sirlar sandig'i",
    "telefon": "Cho'ntak olami",
    "mashina": "Temir tulpor",
    "kitob": "Jim ustoz",
    "quyosh": "Koinot olovi",
    "soat": "Vaqt o'g'risi",
    "qalam": "Qora yulduz",
    "dengiz": "Moviy olam",
    "oy": "Tungi chiroq",
    "suv": "Hayot manbai",
}

while True:
    secret_word, hint = random.choice(list(word_hints.items()))

    print("===SO'Z TOPISH O'YINI===")
    print(f"🕵️‍♂️ Podskazka: {hint}")
    print(f"So'z uzunligi: {len(secret_word)} ta harfdan iborat.\n")

    full_guess = input(
        "Butun so'zni topishga harakat qiling (yoki o'tkazib yuborish uchun Enter bosing): ").lower().strip()

    if full_guess == secret_word:
        print(f"🏆 Qoyil! Shu qisqa ishoradan topganingiz uchun haqiqiy dahosiz! Yashirin so'z: '{secret_word}'")
    else:
        if full_guess:
            print("❌ Afsuski, bu emas edi. Endi harfma-harf davom etamiz!\n")
        else:
            print("Xo'sh, unda harfma-harf topishga o'tamiz!\n")

        guessed_letters = []
        attempts = 7

        while attempts > 0:
            display_word = ""
            for letter in secret_word:
                if letter in guessed_letters:
                    display_word += letter + " "
                else:
                    display_word += "_ "

            print(f"So'z --  {display_word.strip()}")
            print(f"Qolgan urunishlar soni {attempts}")

            if "_" not in display_word:
                print(f"\n🎉 Tabriklayman! Siz so'zni to'liq topdingiz: {secret_word}")
                break

            user_guess = input("Birorta harf kiriting: ").lower().strip()

            if len(user_guess) != 1:
                print("Iltimos, faqat bitta harf kiriring!")
                continue

            if user_guess in guessed_letters:
                print("Siz bu harfni allaqachon kiritgansiz!")
                continue

            guessed_letters.append(user_guess)

            if user_guess in secret_word:
                print("✅ To'g'ri! Bunday harf bor.\n")
            else:
                attempts -= 1
                print("❌ Afsuski, bunday harf yo'q.\n")
        else:
            print(f"😢 O'yin tugadi! Urinishlaringiz tugadi. Yashirin so'z '{secret_word}' edi.")
    play_again = input("\nYana o'ynashni xohlaysizmi? (ha/yo'q): ").lower().strip()
    if play_again != "ha" and play_again != "h":
        print("O'yin uchun rahmat! Xayr! 👋")
        break
















