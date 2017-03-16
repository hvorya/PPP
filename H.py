import sys
import zmq
import time
import multiprocessing
from multiprocessing import *

############################################################################
global Router
global graph
global As_numbers_dict


#############################################################################Publisher H

def Publisher():
    portPH = '17771'
    context = zmq.Context()
    socketPH = context.socket(zmq.PUB)
    socketPH.bind('tcp://127.0.0.1:%s' % portPH)

    while True:
        socketPH.send(('I am Publish H '.encode('utf-8')))
        time.sleep(1)
################################################################################### H subscribe on E
def Subscriber1():
    portSHE = '14771'  # listen to Router E

    context = zmq.Context()
    socketHE = context.socket(zmq.SUB)
    socketHE.connect('tcp://localhost:%s' % portSHE)
    while True:

        socketHE.setsockopt(zmq.SUBSCRIBE, ''.encode('utf-8'))
        messageHE = socketHE.recv()
        print('message E to H '+str(messageHE))
        time.sleep(4)

    ################################################################################### H subscribe on J
def Subscriber2():
        portSHJ = '10771'  # listen  to Router J

        context = zmq.Context()
        socketHJ = context.socket(zmq.SUB)
        socketHJ.connect('tcp://localhost:%s' % portSHJ)

        while True:
            socketHJ.setsockopt(zmq.SUBSCRIBE, ''.encode('utf-8'))
            messageHJ = socketHJ.recv()
            print('message J to H ' + str(messageHJ))
            time.sleep(4)
#################################################################################################
def main():
    Process(target=Publisher).start()

    # Now we can connect a client to all these servers
    Process(target=Subscriber1).start()

    Process(target=Subscriber2).start()


if __name__ == '__main__':
    main()