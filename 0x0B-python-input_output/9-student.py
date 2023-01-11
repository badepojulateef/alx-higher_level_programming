#!/usr/bin/python3
"""Defines a class Student that defines a student."""


class Student:
    """Defines a class Student that defines a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student instance.

        Args:
            first_name (str): The firts name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a dictionary representation of the Student."""
        return self.__dict__
