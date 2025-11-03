% --- Facts: student_course(Student, Course) ---
student_course(john, math).
student_course(john, english).
student_course(mary, math).
student_course(mary, biology).
student_course(lisa, english).
student_course(tom, biology).

% --- Rules ---
courses_of_student(Student, Course) :- student_course(Student, Course).
students_in_course(Course, Student) :- student_course(Student, Course).
