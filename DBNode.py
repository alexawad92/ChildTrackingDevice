#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
import datetime, calendar
import sys
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from errors import *

class DBNode():
    def __init__(self,user, password , database):
        self.cnx = mysql.connector.connect(user='402DB', password = '123456', database = 'ChildTracker')
        self.cursor = self.cnx.cursor()

    def InsertToRoom(self,RoomName, ACTIVE_START, ACTIVE_END, ACTIVE_FLAG):
        if(len(ACTIVE_START) < 1):
            ACTIVE_START = str(datetime.datetime.now().date())
        Activedate = ACTIVE_START.split('-')
        
        if (len(ACTIVE_END) >7):
            try:
                ACTIVEEND = ACTIVE_END.split('-')
                query = ("INSERT INTO ROOMS "
                               "(ROOM_NAME,ACTIVE_START,ACTIVE_END, ACTIVE_FLAG ) "
                               "VALUES (%s, %s, %s, %s)")
                self.cursor.execute(query, (RoomName, ACTIVE_START, date(int(ACTIVEEND[0]), int(ACTIVEEND[1]), int(ACTIVEEND[2])), ACTIVE_FLAG))
            except:
                print("Cursor Execution Failed 1\n")


        else:
            try:
                query = ("INSERT INTO ROOMS "
                               "(ROOM_NAME,ACTIVE_START, ACTIVE_FLAG ) "
                               "VALUES (%s, %s, %s)")
                self.cursor.execute(query, (RoomName, date(int(Activedate[0]), int(Activedate[1]), int(Activedate[2])), ACTIVE_FLAG))

            except:
                print ("Cursor Execution Failed 2\n")
        self.cnx.commit()

    def InsertToTag(self,TagNumber, ACTIVE_START, ACTIVE_END, ACTIVE_FLAG):
        if(len(ACTIVE_START) < 1):
            ACTIVE_START = str(datetime.datetime.now().date())
        Activedate = ACTIVE_START.split('-')
        
        if (len(ACTIVE_END) >7):
            try:
                ACTIVEEND = ACTIVE_END.split('-')
                query = ("INSERT INTO TAGS "
                               "(TAG_NUMBER,ACTIVE_START,ACTIVE_END, ACTIVE_FLAG,CAMPER_ID ) "
                               "VALUES (%s, %s, %s, %s)")
                self.cursor.execute(query, (TagNumber, ACTIVE_START, date(int(ACTIVEEND[0]), int(ACTIVEEND[1]), int(ACTIVEEND[2])), ACTIVE_FLAG, -1))
            except:
                print("Cursor Execution Failed 1\n")


        else:
            try:
                query = ("INSERT INTO TAGS "
                               "(TAG_NUMBER,ACTIVE_START, ACTIVE_FLAG, CAMPER_ID ) "
                               "VALUES (%s, %s, %s, %s)")
                self.cursor.execute(query, (TagNumber, date(int(Activedate[0]), int(Activedate[1]), int(Activedate[2])), ACTIVE_FLAG, -1))
            except:
                print ("Unexpected error:", sys.exc_info()[0])
                print ("Unexpected error:", sys.exc_info()[1])
                print ("Cursor Execution Failed 2\n")
        self.cnx.commit()


    # Function Present 
    # List the campers in a given room
    # Arguments (str) ROOM_NAME : The name of the desired room to see attendence
    def Present(self, ROOM_NAME):
        
        query = ("SELECT ROOM_ID FROM ROOMS WHERE ROOM_NAME = '{0}'".format(ROOM_NAME))
        self.cursor.execute(query)
        ROOM_ID = self.cursor.fetchone()

        query = ("SELECT C.CAMPER_NAME FROM TAGS I, TRANSACTIONS T, CAMPERS C WHERE T.ROOM_ID = '{0}' "
                      " and T.T_OUT IS NULL "
                      "and T.TAG_ID = I.TAG_ID "
                      "and I.CAMPER_ID = C.CAMPER_ID".format(int(ROOM_ID[0])))
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        print (result)
        if not result:
            result.append("No campers in this room") 
        return result


    # Function Present 
    # List the campers in a given room
    # Arguments ROOM_ID : The ID of the desired room to see attendence
    def Rooms(self):
        query = ("SELECT ROOM_NAME FROM ROOMS")
        self.cursor.execute(query)
        result=self.cursor.fetchall()
        return result
        


    def InsertToCamper(self,CamperName, ACTIVE_START, ACTIVE_END, ACTIVE_FLAG):
        if(len(ACTIVE_START) < 1):
            ACTIVE_START = str(datetime.datetime.now().date())
        Activedate = ACTIVE_START.split('-')
        
        if (len(ACTIVE_END) >7):
            try:
                ACTIVEEND = ACTIVE_END.split('-')
                query = ("INSERT INTO CAMPERS "
                               "(CAMPER_NAME,ACTIVE_START,ACTIVE_END, ACTIVE_FLAG) "
                               "VALUES (%s, %s, %s)")
                self.cursor.execute(query, (CamperName, ACTIVE_START, date(int(ACTIVEEND[0]), int(ACTIVEEND[1]), int(ACTIVEEND[2])), ACTIVE_FLAG))
            except:
                print("Cursor Execution Failed 1\n")


        else:
            try:
                query = ("INSERT INTO CAMPERS "
                               "(CAMPER_NAME,ACTIVE_START, ACTIVE_FLAG) "
                               "VALUES (%s, %s, %s)")
                self.cursor.execute(query, (CamperName, date(int(Activedate[0]), int(Activedate[1]), int(Activedate[2])), ACTIVE_FLAG))
            except:
                print ("Unexpected error:", sys.exc_info()[0])
                print ("Unexpected error:", sys.exc_info()[1])
                print ("Cursor Execution Failed 2\n")
        self.cnx.commit()

        
    def AssignTag(self,TagNumber, CamperName):
        ##Check if there is a tag with that tag number
            try:
                query = "SELECT COUNT(*) FROM TAGS WHERE TAG_NUMBER = '{0}'".format(TagNumber)
                        
                self.cursor.execute(query)
                result=self.cursor.fetchone()
                NumberOfUsed = int(result[0])
                if(NumberOfUsed == 0 ):
                    WELCOME_MSG = TagNumber + ''' Tag was not found in the database
                    Try again with a valid TagNumber'''
                    WELCOME_DURATION = 3000
                    top = tk.Toplevel()
                    top.title('Invalid TagNumber')
                    Message(top, text=WELCOME_MSG, padx=20, pady=20).pack()
                    top.after(WELCOME_DURATION, top.destroy)
                    return
            except:
                print ("Unexpected error:", sys.exc_info()[0])
                print ("Unexpected error:", sys.exc_info()[1])
                
                print("Cursor Execution Failed 1\n")


        ##Check if there is a camper with that Name
            try:
                query = "SELECT COUNT(*) FROM CAMPERS WHERE CAMPER_NAME = '{0}'".format(CamperName)
                        
                self.cursor.execute(query)
                result=self.cursor.fetchone()
                NumberOfCamper = int(result[0])
                if(NumberOfCamper == 0 ):
                    WELCOME_MSG = CamperName + ''' Camper was not found in the database
                    Try again with a valid CamperName'''
                    WELCOME_DURATION = 3000
                    top = tk.Toplevel()
                    top.title('Invalid CamperName')
                    Message(top, text=WELCOME_MSG, padx=20, pady=20).pack()
                    top.after(WELCOME_DURATION, top.destroy)
                    return
            except:
                print ("Unexpected error:", sys.exc_info()[0])
                print ("Unexpected error:", sys.exc_info()[1])
                
                print("Cursor Execution Failed 1\n")

                
        ##Check if that Tag is Assign to anyone  and it is active
            try:
                query = "SELECT * FROM TAGS WHERE TAG_NUMBER = '{0}'".format(TagNumber)
                        
                self.cursor.execute(query)
                result=self.cursor.fetchone()
                ActiveFlag = result[4]
                CamperId = result[5]
                if ActiveFlag != 'Y':
                    WELCOME_MSG = TagNumber + ''' was found to be an inactive Tag
                    Try again with an active Tag Number'''
                    WELCOME_DURATION = 3000
                    top = tk.Toplevel()
                    top.title('Invalid TagNumber')
                    Message(top, text=WELCOME_MSG, padx=20, pady=20).pack()
                    top.after(WELCOME_DURATION, top.destroy)
                    return
                if int(CamperId) != -1:
                    WELCOME_MSG = TagNumber + ''' is already assigned
                    Try again with an unassigned Tag Number'''
                    WELCOME_DURATION = 3000
                    top = tk.Toplevel()
                    top.title('Invalid TagNumber')
                    Message(top, text=WELCOME_MSG, padx=20, pady=20).pack()
                    top.after(WELCOME_DURATION, top.destroy)
                    return
                
                
            except:
                print ("Unexpected error:", sys.exc_info()[0])
                print ("Unexpected error:", sys.exc_info()[1])
                
                print("Cursor Execution Failed 1\n")


        ##Check if that Camper is already assigned to a tag and active
            try:
                query = "SELECT * FROM CAMPERS WHERE CAMPER_NAME = '{0}'".format(CamperName)     
                self.cursor.execute(query)
                result=self.cursor.fetchone()
                ActiveFlag = result[4]
                CamperId = int(result[0])
                if ActiveFlag != 'Y':
                    WELCOME_MSG = CamperName + ''' was found to be an inactive Camper
                    Try again with an active Camper'''
                    WELCOME_DURATION = 3000
                    top = tk.Toplevel()
                    top.title('Invalid Camper')
                    Message(top, text=WELCOME_MSG, padx=20, pady=20).pack()
                    top.after(WELCOME_DURATION, top.destroy)
                    return

                #check if kid is already assigned
                query = "SELECT COUNT(*) FROM TAGS WHERE CAMPER_ID = '{0}'".format(CamperId)
                self.cursor.execute(query)
                result=self.cursor.fetchone()
                Number = int(result[0])
                if Number != 0:
                    WELCOME_MSG = CamperName + ''' is already assigned to a Tag
                    Try again with an unassigned Camper'''
                    WELCOME_DURATION = 3000
                    top = tk.Toplevel()
                    top.title('Invalid Camper')
                    Message(top, text=WELCOME_MSG, padx=20, pady=20).pack()
                    top.after(WELCOME_DURATION, top.destroy)
                    return
                
                
            except:
                print ("Unexpected error:", sys.exc_info()[0])
                print ("Unexpected error:", sys.exc_info()[1])
                
                print("Cursor Execution Failed 1\n")

            ##if every thing goes ok
            try:
                query = "SELECT CAMPER_ID FROM CAMPERS WHERE CAMPER_NAME = '{0}'".format(CamperName)     
                self.cursor.execute(query)
                result=self.cursor.fetchone()
                CamperId = int(result[0])

                query = ("UPDATE TAGS SET CAMPER_ID = %s WHERE TAG_NUMBER =%s ")
                               
                self.cursor.execute(query, (CamperId, TagNumber))
                self.cnx.commit()
                WELCOME_MSG = CamperName + ''' Successfully assigned to Tag ''' + TagNumber + '''
                Thank You!'''
                WELCOME_DURATION = 3000
                top = tk.Toplevel()
                top.title('Assign A Tag')
                Message(top, text=WELCOME_MSG, padx=20, pady=20).pack()
                top.after(WELCOME_DURATION, top.destroy)
            except:
                print ("Unexpected error:", sys.exc_info()[0])
                print ("Unexpected error:", sys.exc_info()[1])
                
                print("Cursor Execution Failed UPDATE FAILED1\n")
##        if(len(ACTIVE_START) < 1):
##            ACTIVE_START = str(datetime.datetime.now().date())
##        Activedate = ACTIVE_START.split('-')
##        
##        if (len(ACTIVE_END) >7):
##            try:
##                ACTIVEEND = ACTIVE_END.split('-')
##                query = ("INSERT INTO CAMPERS "
##                               "(Camper_Name,ACTIVE_START,ACTIVE_END, ACTIVE_FLAG) "
##                               "VALUES (%s, %s, %s)")
##                self.cursor.execute(query, (CamperName, ACTIVE_START, date(int(ACTIVEEND[0]), int(ACTIVEEND[1]), int(ACTIVEEND[2])), ACTIVE_FLAG))
##            except:
##                print("Cursor Execution Failed 1\n")
##
##
##        else:
##            try:
##                query = ("INSERT INTO CAMPERS "
##                               "(Camper_Name,ACTIVE_START, ACTIVE_FLAG) "
##                               "VALUES (%s, %s, %s)")
##                self.cursor.execute(query, (CamperName, date(int(Activedate[0]), int(Activedate[1]), int(Activedate[2])), ACTIVE_FLAG))
##            except:
##                print ("Unexpected error:", sys.exc_info()[0])
##                print ("Unexpected error:", sys.exc_info()[1])
##                print ("Cursor Execution Failed 2\n")
##        self.cnx.commit()


    def CheckIn(self, camperName):
        try:
            query = "select CAMPER_NAME, Checked_In from CAMPERS where CAMPER_NAME = '{0}'".format(camperName)
            self.cursor.execute(query)
            x = self.cursor.fetchall()
            print(x)
            numberOfResults = self.cursor.rowcount
            if numberOfResults <= 0:
                raise NameNotFound
            elif (x[0][1] == 'N'):
                query = "update CAMPERS set Checked_In = 'Y' where CAMPER_NAME = '{0}'".format(x[0][0]) 
                self.cursor.execute(query, x[0][0])
                print("Setting checked in status for {0} to 'Y'".format(camperName))
                self.cnx.commit()

        except NameNotFound:
            print("Name not found") 
        except:
            print("CheckIn Error")


    def CheckOut(self, camperName): 
        try:
            query = "select CAMPER_NAME, Checked_In from CAMPERS where CAMPER_NAME = '{0}'".format(camperName)
            self.cursor.execute(query)
            x = self.cursor.fetchall()
            print(x)
            numberOfResults = self.cursor.rowcount
            if numberOfResults <= 0:
                raise NameNotFound
            elif (x[0][1] == 'Y'):
                query = "update CAMPERS set Checked_In = 'N' where CAMPER_NAME = '{0}'".format(x[0][0]) 
                self.cursor.execute(query, x[0][0])
                print("Setting checked in status for {0} to 'N'".format(camperName))
                self.cnx.commit()

        except NameNotFound:
            print("Name not found") 
        except:
            print("CheckIn Error")

    def UnAssignTag(self,TagNumber, CamperName):
          ##Check if there is a tag with that tag number
            try:
                query = "SELECT COUNT(*) FROM TAGS WHERE TAG_NUMBER = '{0}'".format(TagNumber)
                        
                self.cursor.execute(query)
                result=self.cursor.fetchone()
                NumberOfUsed = int(result[0])
                if(NumberOfUsed == 0 ):
                    WELCOME_MSG = TagNumber + ''' Tag was not found in the database
                    Try again with a valid TagNumber'''
                    WELCOME_DURATION = 3000
                    top = tk.Toplevel()
                    top.title('Invalid TagNumber')
                    Message(top, text=WELCOME_MSG, padx=20, pady=20).pack()
                    top.after(WELCOME_DURATION, top.destroy)
                    return
            except:
                print ("Unexpected error:", sys.exc_info()[0])
                print ("Unexpected error:", sys.exc_info()[1])
                
                print("Cursor Execution Failed 1\n")
          ##Check if there is a camper with that Name
            try:
                query = "SELECT COUNT(*) FROM CAMPERS WHERE CAMPER_NAME = '{0}'".format(CamperName)
                        
                self.cursor.execute(query)
                result=self.cursor.fetchone()
                NumberOfCamper = int(result[0])
                if(NumberOfCamper == 0 ):
                    WELCOME_MSG = CamperName + ''' Camper was not found in the database
                    Try again with a valid CamperName'''
                    WELCOME_DURATION = 3000
                    top = tk.Toplevel()
                    top.title('Invalid CamperName')
                    Message(top, text=WELCOME_MSG, padx=20, pady=20).pack()
                    top.after(WELCOME_DURATION, top.destroy)
                    return
            except:
                print ("Unexpected error:", sys.exc_info()[0])
                print ("Unexpected error:", sys.exc_info()[1])
                
                print("Cursor Execution Failed 1\n")
                
            ##Check if the camper is assigned to the right tag before unassigned them
            try:
                query = "SELECT * FROM TAGS WHERE TAG_NUMBER = '{0}'".format(TagNumber)

                self.cursor.execute(query)
                result = self.cursor.fetchone()
                Camper_ID_TAGS_TABLE = int(result[5])

                #print (Camper_ID_TAGS_TABLE)
                
                query = "SELECT * FROM CAMPERS WHERE CAMPER_NAME = '{0}'".format(CamperName)

                self.cursor.execute(query)
                result = self.cursor.fetchone()
                
                Camper_ID_CAMPERS_TABLE = int(result[0])

                #print (Camper_ID_CAMPERS_TABLE)
                

                
                if ( Camper_ID_TAGS_TABLE != Camper_ID_CAMPERS_TABLE):
                    WELCOME_MSG = CamperName + '''  was not assigned to Tag {0}
                    Try again with a valid pair of Camper and Tag '''.format(TagNumber)
                    WELCOME_DURATION = 3000
                    top = tk.Toplevel()
                    top.title('Invalid CamperName')
                    Message(top, text=WELCOME_MSG, padx=20, pady=20).pack()
                    top.after(WELCOME_DURATION, top.destroy)
                    return
                
               #otherwise we have a valid camper and tag to unassigned
                
                query   = "SELECT * FROM TAGS t, CAMPERS c WHERE t.CAMPER_ID = c.CAMPER_ID AND t.TAG_NUMBER = {0} AND c.CAMPER_NAME = '{1}'".format(TagNumber,CamperName)
                self.cursor.execute(query)
                result=self.cursor.fetchone()

                if(result == NULL ):
                    WELCOME_MSG = CamperName + '''  was not assigned to Tag {0}
                    Try again with a valid Camper Name and Tag Number'''.format(TagNumber)
                    WELCOME_DURATION = 3000
                    top = tk.Toplevel()
                    top.title('Invalid CamperName')
                    Message(top, text=WELCOME_MSG, padx=20, pady=20).pack()
                    top.after(WELCOME_DURATION, top.destroy)
                    return
                
                TAGFROMDB = int(result[1])
                CAMPERFROMDB = int(result[7])
                print(TAGFROMDB)
                print(CAMPERFROMDB)
                
                if(TAGFROMDB != TagNumber and CAMPERFROMDB != CamperName):
                    
                    WELCOME_MSG = CamperName + '''  was not assigned to Tag {0}
                    Try again with a valid Camper Name and Tag Number'''.format(TagNumber)
                    WELCOME_DURATION = 3000
                    top = tk.Toplevel()
                    top.title('Invalid CamperName')
                    Message(top, text=WELCOME_MSG, padx=20, pady=20).pack()
                    top.after(WELCOME_DURATION, top.destroy)
                    return
            except:
                print ("Unexpected error:", sys.exc_info()[0])
                print ("Unexpected error:", sys.exc_info()[1])
                
                print("Cursor Execution Failed 120\n")


            try:
                
                    query   = "SELECT * FROM TAGS t, CAMPERS c WHERE t.CAMPER_ID = c.CAMPER_ID AND t.TAG_NUMBER = {0} AND c.CAMPER_NAME = '{1}'".format(TagNumber,CamperName)
                    
                    self.cursor.execute(query)
                    
                    results = self.cursor.fetchone()
##                    print ("Done query 1")
##                    print (len(results))
##                    print (results[7])
                    TAG_ID = results[0]
                    query = ("UPDATE Tags SET Camper_Id =%s Where Tag_ID =%s ")
                               
                    self.cursor.execute(query, (-1,TAG_ID))
                    self.cnx.commit()

                    WELCOME_MSG = CamperName + " was unassigned from Tag '{0}'".format(TagNumber)
                    
                    
                    WELCOME_DURATION = 3000
                    top = tk.Toplevel()
                    top.title('Sucessfully unassinged Tag')
                    Message(top, text=WELCOME_MSG, padx=20, pady=20).pack()
                    top.after(WELCOME_DURATION, top.destroy)
                    return
            except:
                      print ("Unexpected error:", sys.exc_info()[0])
                      print ("Unexpected error:", sys.exc_info()[1])
                
                      print("Cursor Execution Failed 1000\n")
