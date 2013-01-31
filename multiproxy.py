#!/usr/bin/env python

import multiprocessing
import SocketServer

import signal
import sys


def signal_handler(signal, frame):
    print '\nterminating jobs...'
    global jobs

    for job in jobs:
        job.terminate()
        job.join()
    

    print "all jobs stopped. quitting."
    sys.exit(0)



class ProxyHandler(SocketServer.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(2).strip()
        print "{} wrote:".format(self.client_address[0])
        print self.data
        # just send back the same data, but upper-cased
        #self.request.sendall(self.data.upper())




# This process will accept connections from the meterpreter stage 1 payload
def proxy_server():
    print "Server started"
    HOST = "10.20.20.5"
    PORT = 4444
    server = SocketServer.TCPServer((HOST, PORT), ProxyHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C

    server.serve_forever()


    return

# This process will pass along the connections it gets to the meterpreter handler
def proxy_client():
    print "Client started"
    return



if __name__ == '__main__':

    jobs = []

    signal.signal(signal.SIGINT, signal_handler)

    p_server = multiprocessing.Process(target=proxy_server)
    jobs.append(p_server)
    p_server.start()

    p_client = multiprocessing.Process(target=proxy_client)
    jobs.append(p_client)
    p_client.start()