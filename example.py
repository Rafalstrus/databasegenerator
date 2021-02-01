from dataBaseGenerator import Generator
person = Generator()
person.seed(123)
person.gender = "mixed"
for x in range(10):
    person.getData(["uczelnie","zawody","miasta"],50)
person.addtoFileMysql("table")
person.addToJson(name=3)
person.addtoFileTxt()
