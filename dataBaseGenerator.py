from random import Random
import json
localRandom = Random()
class Generator:
    def __init__(self):
        with open('data.json',encoding="utf-8") as json_file:
            self.data = json.loads(json_file.read())
        self.finalData = []

    def getData(self,wantData,graduatePercent = 50, jobPercent = 90):
        if self.gender =="mixed":
            if localRandom.randint(0,1) ==0:
                wantData.insert(0,"nazwiskaMeskie")
                wantData.insert(0,"imionaMeskie")
            else:
                wantData.insert(0,"nazwiskaZenskie")
                wantData.insert(0,"imionaZenskie")                
        elif self.gender == "m":
            wantData.insert(0,"nazwiskaMeskie")
            wantData.insert(0,"imionaMeskie")
        elif self.gender == "k":
            wantData.insert(0,"nazwiskaZenskie")
            wantData.insert(0,"imionaZenskie")            
        dataToAppend = {}
        for x in wantData:
            dataToAppend[x]=self.generateData(x,graduatePercent,jobPercent)
        self.finalData.append(dataToAppend)

    def generateData(self,oneFromWantedData,graduatePercent,jobPercent):
        if oneFromWantedData== "uczelnie":
            if localRandom.randint(0,99)+1 > graduatePercent:
                return None
        elif oneFromWantedData == "zawody":
            if localRandom.randint(0,99)+1 > jobPercent:
                return None
        return self.data[oneFromWantedData][localRandom.randint(0,len(self.data[oneFromWantedData]))-1]
        
    def seed(self,seed):
         localRandom.seed(seed)

    def addToJson(self,filename = "dataToUpdate.json",name="1"):
        jsonToFile = "[\n"
        for x in self.finalData:
            jsonToFile += "\t{\n"
            for y in x:
                jsonToFile += "\t\t"
                jsonToFile += '"'+str("imiona" if y =="imionaMeskie" or y == "imionaZenskie" else "nazwiska" if y =="nazwiskaMeskie" or y=="nazwiskaZenskie" else y)+'": '
                jsonToFile += '"'+str(x[y])+'",'
                jsonToFile += "\n"
            jsonToFile = jsonToFile[:-2]
            jsonToFile += "\n"
            jsonToFile += "\t},\n"
        jsonToFile = jsonToFile[:-2]
        jsonToFile += "\n]"
        f = open(filename, "w",encoding="utf-8")
        f.write(jsonToFile)
        f.close()

    def addToMysql(self,baseName,newBase=False,newTable=False):
        return 0
    def createMysqlDatabase(self):
        import mysql.connector
        mydb = makeConnection(data)
        mycursor = mydb.cursor()
        if newBase:
            mydb = createBase(mycursor,baseName)
            mydb = makeConnection(data)
        else:
            mydb = makeConnection(data)
        mycursor = mydb.cursor()

    def addtoFileMysql(self,tablename,filename = "dataToUpdate.sql"):
        query = self.createMysqlQueryInsert(tablename)
        f = open(filename, "w",encoding="utf-8")
        f.write(query)
        f.close()

    def createMysqlQueryInsert(self,tablename):
        query = "INSERT INTO "+tablename+"("
        for x in self.finalData:
            for key,y in x.items():
                query+= "'"+str("imiona" if key =="imionaMeskie" or key == "imionaZenskie" else "nazwiska" if key =="nazwiskaMeskie" or key=="nazwiskaZenskie" else key)+"',"
            query = query[:-1]
            break
        query += ") values \n"
        for x in self.finalData:
            query += "("
            for key,y in x.items():
                query+="'"+str(y)+"'," if y != None else str(None)+","
            query = query[:-1]
            query +="),\n"
        query = query[:-2]
        return query

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

    def createBaseFile(self,baseName):
        return 0

    def addtoFileTxt(self,filename = "dataToUpdate.txt",separator=';',header = True):
        query = ''
        for x in self.finalData:
            for key,y in x.items():
                query+= str("imiona" if key =="imionaMeskie" or key == "imionaZenskie" else "nazwiska" if key =="nazwiskaMeskie" or key=="nazwiskaZenskie" else key)+separator
            break
        query += "\n"
        for x in self.finalData:
            for key,y in x.items():
                query+= str(y) + separator
            query = query[:-1]
            query +="\n"
        query = query[:-2]
        f = open(filename, "w",encoding="utf-8")
        f.write(query)
        f.close()
