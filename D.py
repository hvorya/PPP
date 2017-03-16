import sys
import zmq
import time
import multiprocessing
from multiprocessing import*
############################################################################
global Router
global graph
global As_numbers_dict

############################################################################# Publish D

def Publisher():
        portPD='13771'
        context = zmq.Context()
        socketPD = context.socket(zmq.PUB)
        socketPD.bind('tcp://127.0.0.1 '+':'+ portPD)

        while True:

            socketPD.send(('I am publish D'.encode('utf-8')))
            time.sleep(1)

############################################################################### D subscribe on A
def Subscriber1():
        portSDA='10771' # listen  to Router A
        context = zmq.Context()
        socketDA = context.socket(zmq.SUB)
        socketDA.connect('tcp://localhost:%s' % portSDA)

        while True:
            socketDA.setsockopt(zmq.SUBSCRIBE, ''.encode('utf-8'))
            messageDA = socketDA.recv()
            print('message A to D' + str(messageDA))
            time.sleep(5)
###############################################################################D subscribe on E
def Subscriber2():

        portSDE='14771' # listen  to Router E
        context = zmq.Context()
        socketDE = context.socket(zmq.SUB)
        socketDE.connect('tcp://localhost:%s' % portSDE)
        while True:
            socketDE.setsockopt(zmq.SUBSCRIBE, ''.encode('utf-8'))
            messageDE = socketDE.recv()
            print('message E to D' + str(messageDE))
            time.sleep(5)

############################################################################### D subscribe on F
def Subscriber3():
        portSDF='15771' # listen  to Router F
        context = zmq.Context()
        socketDF = context.socket(zmq.SUB)
        socketDF.connect('tcp://localhost:%s' % portSDF)
        while True:
            socketDF.setsockopt(zmq.SUBSCRIBE, ''.encode('utf-8'))
            messageDF = socketDF.recv()
            print('message A to D' + str(messageDF))
            time.sleep(5)

############################################################################### D subscribe to J
def Subscriber4():

        portSDJ='19771' # listen to  Router J

        context = zmq.Context()
        socketDJ = context.socket(zmq.SUB)
        socketDJ.connect('tcp://localhost:%s' % portSDJ)
        while True:
            socketDJ.setsockopt(zmq.SUBSCRIBE, ''.encode('utf-8'))
            messageDJ = socketDJ.recv()
            print('message J to D' + str(messageDJ))
            time.sleep(5)

################################################################################Main()

def main():
    Process(target=Publisher).start()

    # Now we can connect a client to all these servers
    Process(target=Subscriber1).start()
    Process(target=Subscriber2).start()
    Process(target=Subscriber3).start()
    Process(target=Subscriber4).start()




if __name__ == '__main__':
         main()