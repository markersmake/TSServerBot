#!/usr/bin/env python3

import time, ts3, random
#ZRRQgg16
#token:ICWv18cSWBROiGJef+xTmahmFJu8a9piPnclyDga
USER = "serveradmin"
PASS = "ZRRQgg16"
HOST = "192.168.2.185"
PORT = 10011
SID  = 1

def controller(ts3conn):

    '''
    [SUM] The purpose of this function is to server as the controller for the bot where each function listens for to command to execute it
    [DEC]
    [input] ts3conn (connection properties)
    [output] text or banning of a client
    '''
    rollName = []
    isRollName = False
    ts3conn.exec_("servernotifyregister", event="textserver")
    
    while True:
        ts3conn.send_keepalive()
        try:
            #send keepalive message every 9 minutes to not timeout
            event = ts3conn.wait_for_event(timeout=550)
        except ts3.query.TS3TimeoutError:
            pass
        
        else:
            if(event[0]["msg"] == "!pokeme"):
                #play a random sound from soundbits folder
                msg = "hello"
                ts3conn.exec_("clientpoke", clid=event[0]["invokerid"], msg=msg)
            #elseif(event[0]["msg"] == "!playsound")
            
            #!roulette
            if(event[0]["msg"] == "!roulette"):
                start = time.time()
                msg = "You're the fuck"
                #Is user already on the list?
                for name in rollName:
                    if(event[0]["invokername"] == name):
                         ts3conn.exec_("gm", msg="Hey asshole, you've already rolled. Just wait")
                         
                if(isRollName == False):
                    rollName.append(event[0]["invokername"])
                    ts3conn.exec_("gm", msg="You've been added to the list")
                    
            elif(event[0]["msg"] == "!roll"):
                    ts3conn.exec_("gm", msg="There once were a brave few\n")
                    time.sleep(2)
                    ts3conn.exec_("gm", msg="who thought that they knew\n")
                    time.sleep(2)
                    ts3conn.exec_("gm", msg="But one could not stand\n")
                    time.sleep(2)
                    ts3conn.exec_("gm", msg="As he was the one to get banned\n")
                    if(len(rollName) >= 2):
                        index = random.randint(0, len(rollName))
                        rolledName = rollName[index]
                        uid   = ts3conn.exec_("clientfind", pattern=rolledName)
                        uid   = uid[1]
                        uid   = uid['clid']
                        ts3conn.exec_("banclient", clid=uid, time=20)
                        rollname = []
                    else:
                        continue
            elif(event[0]["msg"] == "!video")
            
            #!sound
            #!video
    return

if __name__ == "__main__":
    with ts3.query.TS3ServerConnection(HOST, PORT) as ts3conn:
        ts3conn.exec_("login", client_login_name=USER, client_login_password=PASS)
        ts3conn.exec_("use", sid=SID)
        #hello_bot(ts3conn)
        controller(ts3conn)


























