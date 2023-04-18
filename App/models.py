from django.db import models as m


class Position(m.Model):
    name = m.CharField(max_length=20)
    department = m.CharField(max_length=20)

    def __str__(self):
        return self.name


class Employee(m.Model):
    fullname = m.CharField(max_length=20)
    birth_year = m.DateField()
    position = m.ForeignKey(Position, on_delete=m.CASCADE)

    def __str__(self):
        return self.fullname
