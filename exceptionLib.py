import settings
import shutil
import os
exceptionList={}
database=None

def loadException():
    #exceptionList={}
    file = open(settings.exceptionFile, 'r')
    for line in file:
        (exc, key)=line.split(' => ')
        key=key.strip()
        if key not in exceptionList.keys():
            exceptionList[key]=[]
            exceptionList[key].append(exc)
        else:
            if exc not in exceptionList[key]:
                exceptionList[key].append(exc)

def saveException():
    filename=settings.exceptionFile + '.wip'
    file = open(filename, 'w+')
    x=0
    dictList=exceptionList
    for k in sorted(exceptionList.keys()):
        v=exceptionList[k]
        for i in v:
            if x==0:
                file.write(i+" => "+k)
                x=1
            else:
                file.write("\n"+i+" => "+k)

def publishException():
    saveException()
    src=settings.exceptionFile + '.wip'
    dest=settings.exceptionFile
    try:
        copyres=shutil.copy2(src, dest)
    except Exception as error:
        return {"ok":"ko", "msg":"error in publishing", "error":error}
    os.remove(src)
    return {"ok":"ok", "msg":"Published"}


def addExcepion(base:str, lista:list):
    base=base.strip()
    v=[]
    # if base in exceptionList.keys():
    #     v=exceptionList[base]

    for i in lista:
        if i not in v:
            s=i.strip()
            if len(s)>0:
                v.append(s)
    exceptionList[base]=sorted(v)
    return {"base":base, "list":exceptionList[base]}

def removeException(base:str):
    if base in exceptionList.keys():
        del exceptionList[base]
        saveException()
    return {"msg":"remove", "base":base}

def isPublished():
    src=settings.exceptionFile + '.wip'
    if os.path.exists(src):
        return False
    return True

def search(pattern, searchString):
    try:
        cur = database.connection.cursor()
        query=settings.MYSQL_QUERY.replace('{#pattern#}',pattern).replace('{#searchString#}', searchString)
        print(query)
        cur.execute(query)
        
        res=cur.fetchall()
        returnValue=[]
        for i in res:
            val=str(i[0])
            if val!='None':
                val=val.strip()
                returnValue.append(val)
        return returnValue
    except Exception as error:
        return {"ok":"ko", "msg":str(error)}
    # select distinct REGEXP_SUBSTR(s_title,'[[:space:]]1.+9[[:space:]]') from oc_t_item_description where s_title like '%1,9%' limit 100;

def reload():
    exceptionList={}
    src=settings.exceptionFile + '.wip'
    if os.path.exists(src):
        os.unlink(src)

    loadException()