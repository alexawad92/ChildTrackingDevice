#Alex Awad
#Team 1
#10-20-2016
#!/usr/bin/env python3
 
import time
import RPi.GPIO as GPIO
import datetime
import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
import sys




def InsertToTrans(Roomid,TagID):
    
    cnx = mysql.connector.connect(host = "10.131.174.133" , user= "402DB", password = "123456", database = 'ChildTracker')
    cursor = cnx.cursor(buffered=True)
    try:
        query = "Select * from TRANSACTIONS where TAG_ID = %s and ROOM_ID = %s"
        cursor.execute(query,(TagID, Roomid))
        Result=cursor.fetchall()
        UpdateId = 0;
        if(len(Result) >0 ):
            for R in Result:
                if(R[3] != None and R[4] == None):
                    UpdateId = int(R[0])
                    break
        
        
        if(UpdateId == 0):
            print ("Entering Room")
            #insert new recode and set R_OUT to null
            QUERY = ("INSERT INTO TRANSACTIONS "
            "(TAG_ID,ROOM_ID,T_IN) "
            "VALUES (%s, %s, %s)")
            cursor.execute(QUERY, (TagID, Roomid, datetime.now()))
            cnx.commit()

        if(UpdateId != 0 ):
            print('Leaving Room')
            QUERY = ("UPDATE TRANSACTIONS SET T_OUT = %s Where TRANSACTION_ID =%s ")
            cursor.execute(QUERY, (datetime.now(), UpdateId))
            cnx.commit()
    except:
        print("Cursor Execution Failed 1\n")
        print ("Unexpected error:", sys.exc_info()[0])
        print ("Unexpected error:", sys.exc_info()[1])
        print ("Cursor Execution Failed 2\n")
def main():

    try:
        GPIO.setmode(GPIO.BCM)  ##BCM
        GPIO.setup(4,GPIO.IN) #4
        GPIO.setup(3,GPIO.IN) # 3
        GPIO.setup(17, GPIO.OUT) # 27
        GPIO.output(17,True)## Switch on pin 7
        GPIO.output(17,False)## Switch off pin 7
            
        while True:
            GPIO.setmode(GPIO.BCM)  ##BCM
            GPIO.setup(4,GPIO.IN) #4
            GPIO.setup(3,GPIO.IN) # 3
            if int(GPIO.input(3) == 1) and int(GPIO.input(4)) ==0:
                print('Alex')
                print('Time: ', datetime.now() , 'RoomID :', '1' , 'TagID: ', '1')
                InsertToTrans(1, 1)
                print('resetting')
                time.sleep(1)
                GPIO.output(17,True)## Switch on pin 7
                time.sleep(2)## Wait
                GPIO.output(17,False)## Switch off pin 7
                continue
            elif int(GPIO.input(3)) ==0 and int(GPIO.input(4))==1:
                print('Cooper')
                print('Time: ', datetime.now() , 'RoomID :', '1' , 'TagID: ', '2')
                InsertToTrans(1, 1)
                print('resetting')
                time.sleep(1)
                GPIO.output(17,True)## Switch on pin 7
                time.sleep(2)## Wait
                GPIO.output(17,False)## Switch off pin 7
            else:
                time.sleep(1)
                x = 0
            time.sleep(0.5)
    except KeyboardInterrupt:
        print ("KeyboardInterrupt : Exitting")
    except:
        print ("EException: Exitting")
    finally:
            GPIO.cleanup()



if __name__=="__main__":
    main()
