import sys
import zmq
import time
import multiprocessing
from multiprocessing import *

############################################################################
global Router
global graph
global As_numbers_dict


############################################################################# B publisher

def Publisher():
    portPB = '11771'
    #if len(sys.argv) > 1:
        #portPB = sys.argv[1]
        #int(portPB)
    context = zmq.Context()
    socketPB = context.socket(zmq.PUB)
    socketPB.bind('tcp://127.0.0.1:%s' % portPB)

    while True:
        socketPB.send(('I am Publish  B'.encode('utf-8')))
        time.sleep(1)

###############################################################subscribe B on A

def Subscriber1():

    portSBA = '10771'  # connection to Router B
    #if len(sys.argv) > 1:
        #portSA = sys.argv[1]
        #int(portSA)
    context = zmq.Context()
    socketBA = context.socket(zmq.SUB)

    socketBA.connect('tcp://localhost:%s' % portSBA)
    while True:

        socketBA.setsockopt(zmq.SUBSCRIBE,''.encode('utf-8'))
        messageBA = socketBA.recv()

        print('message A to B'+str(messageBA))

        time.sleep(1)
################################################################################### subscribe B on C
def Subscriber2():
    portSC = '12771'  # connection to Router B
    context = zmq.Context()
    socketBC = context.socket(zmq.SUB)
    socketBC.connect('tcp://localhost:%s' % portSC)
    while True:
        socketBC.setsockopt(zmq.SUBSCRIBE, ''.encode('utf-8'))
        messageBC = socketBC.recv()
        print('message C to B'+str(messageBC))
        time.sleep(5)
###################################################################################
def main():
    Process(target=Publisher).start()

    # Now we can connect a client to all these servers
    Process(target=Subscriber1).start()
    Process(target=Subscriber2).start()



if __name__ == '__main__':
    main()