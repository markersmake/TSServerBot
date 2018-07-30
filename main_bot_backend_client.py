#!/usr/bin/env python3

import time
import ts3
#ZRRQgg16
#token:ICWv18cSWBROiGJef+xTmahmFJu8a9piPnclyDga
USER = "serveradmin"
PASS = "ZRRQgg16"
HOST = "192.168.2.185"
PORT = 10011
SID = 1

def random_sound(ts3conn):

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
            elseif(event[0]["msg"] == "!playsound")
            
            
    return

if __name__ == "__main__":
    with ts3.query.TS3ServerConnection(HOST, PORT) as ts3conn:
        ts3conn.exec_("login", client_login_name=USER, client_login_password=PASS)
        ts3conn.exec_("use", sid=SID)
        #hello_bot(ts3conn)
        random_sound(ts3conn)


























