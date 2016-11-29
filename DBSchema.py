#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode
from collections import OrderedDict

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)
DB_NAME = 'ChildTracker'

TABLES = OrderedDict()
##TABLES['FACILITIES'] = (
##    "CREATE TABLE `FACILITIES` ("
##    "  `FACILITY_ID` int(11) NOT NULL AUTO_INCREMENT,"
##    "  `FACILITY_NAME` varchar(255) NOT NULL,"
##    "  `ACTIVE_START` date NOT NULL,"
##    "  `ACTIVE_END` date NULL,"
##    "  `ACTIVE_FLAG` enum('Y','N') NOT NULL,"
##    "  PRIMARY KEY (`FACILITY_ID`)"
##    ") ENGINE=InnoDB")

TABLES['ROOMS'] = (
    "CREATE TABLE `ROOMS` ("
    "  `ROOM_ID` int(11) NOT NULL AUTO_INCREMENT,"
    "  `ROOM_NAME` varchar(255) NOT NULL,"
    "  `ACTIVE_START` date NOT NULL,"
    "  `ACTIVE_END` date  NULL,"
    "  `ACTIVE_FLAG` enum('Y','N') NOT NULL,"
    "  PRIMARY KEY (`ROOM_ID`)"
    ") ENGINE=InnoDB")
TABLES['CAMPERS'] = (
    "CREATE TABLE `CAMPERS` ("
    "  `CAMPER_ID` int(11) NOT NULL AUTO_INCREMENT,"
    "  `CAMPER_NAME` varchar(255) NOT NULL,"
    "  `ACTIVE_START` date NOT NULL,"
    "  `ACTIVE_END` date NULL,"
    "  `ACTIVE_FLAG` enum('Y','N') NOT NULL,"
    "  `Checked_In` enum('N','Y')NOT NULL,"
    "  PRIMARY KEY (`CAMPER_ID`)"
    ") ENGINE=InnoDB")
TABLES['TAGS'] = (
    "CREATE TABLE `TAGS` ("
    "  `TAG_ID` int(11) NOT NULL AUTO_INCREMENT,"
    "  `TAG_NUMBER` varchar(255) NOT NULL,"
    "  `ACTIVE_START` date NOT NULL,"
    "  `ACTIVE_END` date NULL,"
    "  `ACTIVE_FLAG` enum('Y','N') NOT NULL,"
    "  `CAMPER_ID`int(11) NOT NULL,"
    "  PRIMARY KEY (`TAG_ID`)"
    ") ENGINE=InnoDB")
TABLES['TRANSACTIONS'] = (
    "CREATE TABLE `TRANSACTIONS` ("
    "  `TRANSACTION_ID` int(11) NOT NULL AUTO_INCREMENT,"
    "  `TAG_ID` int(11) NOT NULL,"
    "  `ROOM_ID` int(11) NOT NULL,"
    "  `T_IN` DATETIME NULL,"
    "  `T_OUT` DATETIME NULL,"
    "  PRIMARY KEY (`TRANSACTION_ID`)"
    ") ENGINE=InnoDB")
##TABLES['CAREGIVERS'] = (
##    "CREATE TABLE `CAREGIVERS` ("
##    "  `CAREGIVER_ID` int(11) NOT NULL AUTO_INCREMENT,"
##    "  `CAREGIVER_NAME` varchar(255) NOT NULL,"
##    "  `ACTIVE_START` date NOT NULL,"
##    "  `ACTIVE_END` date  NULL,"
##    "  `ACTIVE_FLAG` enum('Y','N') NOT NULL,"
##    "  PRIMARY KEY (`CAREGIVER_ID`)"
##    ") ENGINE=InnoDB")
##TABLES['USERS'] = (
##    "CREATE TABLE `USERS` ("
##    "  `USER_ID` int(11) NOT NULL AUTO_INCREMENT,"
##    "  `USER_NAME` varchar(255) NOT NULL,"
##    "  `ACTIVE_START` date NOT NULL,"
##    "  `ACTIVE_END` date  NULL,"
##    "  `ACTIVE_FLAG` enum('Y','N') NOT NULL,"
##    "  PRIMARY KEY (`USER_ID`)"
##    ") ENGINE=InnoDB")
cnx = mysql.connector.connect( user='402DB', password = '123456')

cursor = cnx.cursor()


try:
    cnx.database = DB_NAME  
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)

for name, ddl in TABLES.items():
    try:
        print("Creating table {}: ".format(name), end='')
        cursor.execute(ddl)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
cnx.close()
