students = ["Maria", "Noel", "Norbert", "Fermin", "Becca", "Juan", "Thalia", "Najla", "Borna", "Ueli", "Vincenzo", "Anna", "Zeynep", "Sergio", "Sebastian", "John"]
guests = ["Anna", "Zeynep"]

print "*" * 66
print
print "There should be %d students in the room." % len(students)
print
print "Namely (in alphabetical order):"

for student in sorted(students):
    if student in guests:
        print "  ", student, "(guest)"
    else:
        print "  ", student

print
print "*" * 66
