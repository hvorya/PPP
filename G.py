import sys
import zmq
import time
import multiprocessing
from multiprocessing import *

############################################################################
global Router
global graph
global As_numbers_dict


############################################################################# G publisher

def Publisher():
    portPG = '16771'
    context = zmq.Context()
    socketPG = context.socket(zmq.PUB)
    socketPG.bind('tcp://127.0.0.1:%s' % portPG)
    while True:
        socketPG.send(('I am Publish  G'.encode('utf-8')))
        time.sleep(1)

###############################################################subscribe G on E

def Subscriber1():

    portSGE = '14771'  # listen  to Router E
    context = zmq.Context()
    socketGE = context.socket(zmq.SUB)
    socketGE.connect('tcp://localhost:%s' % portSGE)
    while True:
        socketGE.setsockopt(zmq.SUBSCRIBE,''.encode('utf-8'))
        messageGE = socketGE.recv()

        print('message E to G'+str(messageGE))

        time.sleep(1)

################################################################################### Main()
def main():
    Process(target=Publisher).start()

    # Now we can connect a client to all these servers
    Process(target=Subscriber1).start()



if __name__ == '__main__':
    main()