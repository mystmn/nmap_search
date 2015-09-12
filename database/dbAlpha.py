#!/usr/bin/env python
# http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html
import sqlite3
import os

from mods import rule

class databaseImport(object):
    def __init__(self, deviceName, ip, domain, os, dbPath):

        self.dbPath = dbPath + ".db"

        self.dbConn()

        #self.verify_Table()

        return self.col_insert(deviceName, ip, domain, os)

    def dbConn(self):
        self.table_columnSettings()

        self.dbCreation()

    def dbCreation(self):

        if os.path.isfile(self.dbPath):

            # Establish Dabatabase Connection
            self.conn = sqlite3.connect(self.dbPath)
            self.c = self.conn.cursor()

        else:
            self.conn = sqlite3.connect(self.dbPath)
            self.c = self.conn.cursor()

            if self.tbl_creation():

                self.dbCommit
                print "...File Created..."
                return self.dbCreation()

            else:
                return self.dbCreation()

            print "Not able to create the database at %s" % self.dbPath

    def col_select(self):
        print ""

    def col_insert(self, deviceName, ip, domain, os):
        # A) Inserts an ID with a specific value in a second column
        signal = "Entering %s into DB" % deviceName
        try:
            self.c.execute("INSERT INTO {tn} ({cn1},{cn2},{cn3},{cn4},{cn5},{cn6}) VALUES "
                           "('{in1}','{in2}','{in3}','{in4}','{OSC1}','{OSC2}')". \
                format(
                tn=self.table_name,
                cn1=self.device_column,
                cn2=self.ip_column,
                cn3=self.domain_column,
                cn4=self.osType,
                cn5=self.dateStamp,
                cn6=self.timeStamp,

                in1=deviceName,
                in2=str(ip),
                in3=domain,
                in4=os,
                OSC1=rule.localDate,
                OSC2=rule.localtime,
            ))

            print signal + "...successful"

        except sqlite3.IntegrityError:
            print('ERROR: ID already exists in PRIMARY KEY column {}'.format(deviceName))

            print signal + "...failed"
        self.dbCommit()

    def tbl_creation(self):

        try:
            self.c.execute(
                "CREATE TABLE {tn} (id INTEGER PRIMARY KEY AUTOINCREMENT, {cn1} {var1}(30), {cn2} {var1}(15),"
                "{cn3} {var1}(30), {cn4} {var1}(75), {cn5} DATE, {cn6} DATETIME)". \
                    format(
                    tn=self.table_name,
                    cn1=self.device_column,
                    cn2=self.ip_column,
                    cn3=self.domain_column,
                    cn4=self.osType,
                    cn5=self.dateStamp,
                    cn6=self.timeStamp,
                    var1="VARCHAR"
                ))
            self.dbCommit()
            print "...table created"
            return True

        except sqlite3.IntegrityError:
            print('ERROR: Table already exists in {}'.format(self.table_name))
            self.dbCommit()
            return False

    def table_columnSettings(self):
        self.table_name = 'devices'
        self.device_column = 'deviceName'
        self.ip_column = 'ip'
        self.domain_column = 'domain'
        self.osType = 'os'
        self.dateStamp = 'dateStamp'
        self.timeStamp = 'timeStamp'

    def dbCommit(self):
        self.conn.commit()
        self.conn.close()

    '''
    def verify_Table(self):
            b = sqlite3.connect(self.dbPath + ".db")
            v = b.cursor()
            v.execute("SELECT COUNT(*) FROM {tn}". \
                format(
                    tn=self.table_name
                ))

            if v.fetchone()[0] == 1:
                v.close()
                print "yes"
                return True
            else:
                return False
                print "no"
    '''
