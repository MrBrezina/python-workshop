#!/usr/bin/env python
# encoding: utf-8
"""
Print list of students.
"""

students = ["María", "Noel", "Norbert", "Fermín", "Becca", "Juan", "Thalia", "Najla", "Borna", "Ueli", "Vincenzo", "Anna", "Zeynep", "Sergio", "Sebastian", "John"]
guests = ["Anna", "Zeynep"]

print
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
print
