import random
import json
#https://stackoverflow.com/questions/12368996/what-is-the-scope-of-a-random-seed-in-python
class Generator:
    def __init__(self):
        with open('data.json',encoding="utf-8") as json_file:
            self.data = json.loads(json_file.read())
        self.finalData = []

    def generateObject(self):
        return 0

    def getData(self,wantData,chanceToGraduate):
        dataToAppend = []
        for x in wantData:
            dataToAppend.append(self.generateData(x,chanceToGraduate))
        self.finalData.append(dataToAppend)
        print(dataToAppend)

    def generateData(self,oneFromWantedData,chanceToGraduate):
        if oneFromWantedData== "uczelnie":
            if random.randint(0,99)+1 > chanceToGraduate:
                return None
        return self.data[oneFromWantedData][random.randint(0,len(self.data[oneFromWantedData]))]
        
    def seed(self,seed):
        self.randomSeed = random.seed(seed)

    def addToJson(self):
        return 0

    def addToMysql(self,baseName,newBase=False):
        import mysql.connector
        mydb = makeConnection(data)
        mycursor = mydb.cursor()
        if newBase:
            mydb = createBase(mycursor,baseName)
            mydb = makeConnection(data)
        else:
            mydb = makeConnection(data)
        mycursor = mydb.cursor()

    def addtoFileMysql(self):
        return 0

    def makeConnection(self,data,baseName = 0):
        if baseName==0:
            mydb = mysql.connector.connect(
            host=data[0],
            user=data[1],
            password=data[2])
        else:
            mydb = mysql.connector.connect(
            host=data[0],
            user=data[1],
            password=data[2],
            database= baseName
            )  
        return mydb

    def createBase(self,mycursor,baseName):
        mycursor.execute("SHOW DATABASES LIKE '"+str(databaseName)+"';")
        for x in mycursor:
            if not(not x):
                print('database with this name already exist')
            else:
                mycursor.execute("CREATE DATABASE "+str(databaseName)+"")

    def addtoFileTxt(self,data,separator=';'):
        return 0
