from dataBaseGenerator import Generator

person = Generator()
person.seed(123)
for x in range(3):
    person.getData(["imionaMeskie","nazwiskaMeskie","uczelnie","zawody","miasta"],12)