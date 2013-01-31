import multiprocessing

# This process will accept connections from the meterpreter stage 1 payload
def proxy_server():
	print "Server started"
	def proxy_handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print "{} wrote:".format(self.client_address[0])
        print self.data
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())


	return

# This process will pass along the connections it gets to the meterpreter handler
def proxy_client():
	print "Client started"
	return



if __name__ == '__main__':
    jobs = []

    server = multiprocessing.Process(target=proxy_server)
    jobs.append(server)
    server.start()

    client = multiprocessing.Process(target=proxy_client)
    jobs.append(proxy_client)
    client.start()