subject1=int(input("Enter marks for Subject 1: "))
subject2=int(input("Enter marks for Subject 2: "))
subject3=int(input("Enter marks for Subject 3: "))
subject4=int(input("Enter marks for Subject 4: "))
subject5=int(input("Enter marks for Subject 5: "))

total_subjects = [subject1, subject2, subject3, subject4, subject5]
print("Marks for each subject:", total_subjects)
total_marks = sum(total_subjects)
print("Total marks obtained:", total_marks)


print("Average marks obtained:", total_marks / len(total_subjects))
print("Maximum marks obtained in a subject:", max(total_subjects))
print("Minimum marks obtained in a subject:", min(total_subjects))
print("Marks in ascending order:", sorted(total_subjects))