#!/usr/bin/env python
# http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html
import sqlite3
import os
import sys

sys.path.append('mods/os_commands')
from mods import osCommands as OSC


class databaseImport(object):
    def __init__(self, deviceName, ip, domain, os, dbPath):
        #        self.testDatabase()
        # raise SystemExit(0)
        self.dbPath = dbPath + ".db"

        if self.establish_db_connection():
            self.deviceInsert(deviceName, ip, domain, os)
        else:
            print "BAM!!!"

    def table_columnSettings(self):
        self.table_name = 'devices'
        self.device_column = 'deviceName'
        self.ip_column = 'ip'
        self.domain_column = 'domain'
        self.osType = 'os'
        self.dateStamp = 'dateStamp'
        self.timeStamp = 'timeStamp'

    def establish_db_connection(self):
        self.table_columnSettings()

        self.conn = sqlite3.connect(self.dbPath)
        self.c = self.conn.cursor()

        if not self.verifyTable():
            self.createTable()
            return self.establish_db_connection()
#        else:
        return True

    def verifyTable(self):
            self.conn.cursor()
            self.c.execute("SELECT COUNT(*) FROM main_162_37_59_db.'{tn}'". \
                format(
                    tn=self.table_name
                ))

            if self.c.fetchone()[0] == 1:
                self.c.close()
                print "yes"
                return True
            else:
                return False
                print "no"

    def dbCommit(self):
        self.conn.commit()
        self.conn.close()

    def deviceInsert(self, deviceName, ip, domain, os):
        # A) Inserts an ID with a specific value in a second column

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
                OSC1=OSC.localDate,
                OSC2=OSC.localtime,
            ))
            print (deviceName, ip)

        except sqlite3.IntegrityError:
            print('ERROR: ID already exists in PRIMARY KEY column {}'.format(deviceName))

    def createTable(self):

        try:
            self.c.execute("CREATE TABLE {tn} (id INTEGER PRIMARY KEY AUTOINCREMENT, {cn1} {var1}(30), {cn2} {var1}(15),"
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

        except sqlite3.IntegrityError:
            print('ERROR: Table already exists in {}'.format(self.table_name))
