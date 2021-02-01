from dataBaseGenerator import Generator

person = Generator()
person.seed(123)
person.gender = "k"
for x in range(3):
    person.getData(["uczelnie","zawody","miasta"],12)
person.addtoFileMysql("table")