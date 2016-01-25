import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 2222))
s.listen(1)
#print "listen"
while True:
    conn, addr = s.accept()
#    print "Socket in accept", addr
    while True:
#        print "Read for data"
        data = conn.recv(1024)
        if not data: break
        if str(data).lower() == str("close"): 
            conn.close()
#            print "Connection closed"
            break
        conn.send(data)
#        print "Send", data
    
        
        
