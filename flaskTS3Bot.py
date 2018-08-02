from flask import Flask, json
import ts3
#token:98L0FO8CIumlMFIDfpe2xxH1hOTpJjpbCVGwcvtt
#UG+Od+LN
app = Flask(__name__)

HOST= '192.168.1.69'
USER= 'serveradmin'
PASS= 'UG+Od+LN'
PORT = 10011
SID  = 1

@app.route('/clientList')
def listAll():
    clients = []
    with ts3.query.TS3ServerConnection(HOST,PORT) as ts3conn:
        ts3conn.exec_("login", client_login_name=USER, client_login_password=PASS)
        ts3conn.exec_("use", sid=SID)
        clientList = ts3conn.exec_('clientlist')
        
        for x in clientList:
            clients.append(x)
        return json.dumps(clients)

if __name__ == '__main__':
    
    app.run()
