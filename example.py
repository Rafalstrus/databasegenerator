from dataBaseGenerator import Generator

person = Generator()
person.seed(123)
for x in 200:
    person.getData(["imie","nazwisko","uczelnia","zawod","miasto"])