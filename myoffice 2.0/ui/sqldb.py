#!/usr/bin/python
#coding: utf-8
import types,locale
import MySQLdb
createdb="create database if not exists pythondb"
#createtable=["create table if not exists usertab(id int, name varchar(100),passwd varchar(100),PRIMARY KEY(id))",]

class Moudels(object):
    def __init__(self):
        self.localcharset = locale.getdefaultlocale()[1]              
        self.conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='rootss',port=3306)    
        createdb="create database if not exists pythondb"
        self.execute(createdb, autocommit=True)
        self.conn.select_db('pythondb') 
        self.version = '' 
        self.init()
        
    def init(self):
        pass        

    def close(self):
        self.conn.close()
        self.conn = None
        
    def execute(self, sql, autocommit=True):
        cur = self.conn.cursor()
        cur.execute(sql)       
        if autocommit:
            self.conn.commit()       
        cur.close()
            

    def execute_param(self, sql, param, autocommit=True):
        cur = self.conn.cursor()
        cur.execute(sql, param)        
        if autocommit:
            self.conn.commit()
        cur.close()

    def commit(self):
        self.conn.commit()
        
    def rollback(self):
        self.conn.rollback()

    def query(self, sql, iszip=True):
        if type(sql) == types.UnicodeType:
            sql = sql.encode(self.charset, 'ignore') 
        cur = self.conn.cursor()
        cur.execute(sql)
        res = cur.fetchall()
        cur.close()
        return res 

    def query_one(self, sql):
        if type(sql) == types.UnicodeType:
            sql = sql.encode(self.charset, 'ignore')
 
        cur = self.conn.cursor()
        cur.execute(sql)
        one = cur.fetchone()
        cur.close()
        
        if one:
            return one[0]
        return None

    def last_insert_id(self):
        sql = "select last_insert_rowid()"
        cur = self.conn.cursor()
        cur.execute(sql)
        one = cur.fetchone()
        cur.close()
        return one[0]

class userdb(Moudels):
    __Tab='usertable'
    id=0
    name='name'
    passwd='passwd'
    usertable="create table if not exists usertable \
    (id int not null auto_increment primary key,%s varchar(100),%s varchar(100))" %(name,passwd)
    def __init__(self,name='name',passwd='passwd'):
        id=None
        self.name=name
        self.passwd=passwd
        Moudels.__init__(self)       
        self.execute(userdb.usertable)
        
    def Insert(self):
        insertsql="insert into usertable (name,passwd) values ('%s','%s')" %(self.name,self.passwd)        
        print insertsql
        self.execute(insertsql)
    def Delete(self):
        deletesql="delete from usertable where name='%s' and passwd='%s'" %(self.name,self.passwd)
        print deletesql
        self.execute(deletesql)
    def Update(self):
        #UPDATE pythondb.usertable SET passwd = 'kf' WHERE usertable.id=1 LIMIT 1 
        updatesql="Update usertable set name='%s',passwd='%s' where id=%d" %(self.name,self.passwd,self.id)
        print updatesql
        self.execute(updatesql)
    def Query(self,name=None,passwd=None): 
        if name is None  and passwd is None:
            return
        if name:
            if passwd:
                querysql="select * from %s WHERE name LIKE '%s' AND passwd LIKE '%s'" %(userdb.__Tab,name,passwd)
            else:
                querysql="select * from %s WHERE name LIKE '%s'" %(userdb.__Tab,name)
        else:
            querysql="select * from %s WHERE passwd LIKE '%s'" %(userdb.__Tab,passwd)
        print querysql
        return self.query(querysql)
        
        
#f=userdb('name','passwd')      
        
        
