# Input the number of students in a/ b/ c class
students_count_a = int(input())
students_count_b = int(input())
students_count_c = int(input())
# Count the number of desks needed for each class separately
desk_a = students_count_a // 2 + students_count_a % 2
desk_b = students_count_b // 2 + students_count_b % 2
desc_c = students_count_c // 2 + students_count_c % 2
# Print the total desks needed
print(desk_a + desk_b + desc_c)
