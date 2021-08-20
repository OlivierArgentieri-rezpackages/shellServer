import socket
import sys
import logging
import _thread
HOST = 'localhost'
PORT = 2017
print(sys.version)
# set log level here :
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    # Get -p parameter value
    if ('-p' in sys.argv and sys.argv.index('-p') != len(sys.argv)):
        PORT = int(sys.argv[sys.argv.index('-p')+1])

    # Start code server socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    logging.info('socket created')


    try:
        s.bind((HOST, PORT))
    except socket.error as msg:
        logging.error(f'Bind Failed {msg}')
        sys.exit()

    logging.info('Socket Bind Complete')

    s.listen(10)
    logging.info(f'Listening on {HOST}:{PORT} ...')
    # threaded
    def thread_listener(conn):
        while True:
            # receive Data
            data = conn.recv(1024)
            if not data:
                break
            try:
                exec(data, globals())
            except Exception as e:
                print(e) # just print  because error on send python code, not execution
        conn.close()
        
        

    while True:
        conn, addr = s.accept()
        _thread.start_new_thread(thread_listener, (conn,))

    s.close()