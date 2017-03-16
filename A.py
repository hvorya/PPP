import sys
import zmq
import time
import multiprocessing
from multiprocessing import*
############################################################################
global Router
global graph
global As_numbers_dict

############################################################################# Publish A

def Publisher():
        portPA='10771'
        #if len(sys.argv) > 1 :
           # portPA=sys.argv[1]
            #int(portPA)
        context = zmq.Context()
        socketPA = context.socket(zmq.PUB)
        socketPA.bind('tcp://127.0.0.1 '+':'+ portPA)

        while True:

            socketPA.send(('I am publish A'.encode('utf-8')))
            time.sleep(1)

#####################################################################################A subscribe on B

def Subscriber1():

        portSB='11771' # connection to Router B
        #if len(sys.argv) > 1:
            #portSB=sys.argv[1]
            #int(portSB)
        context = zmq.Context()
        socketAB = context.socket(zmq.SUB)
        socketAB.connect('tcp://localhost:%s' % portSB)
        while True:
            socketAB.setsockopt(zmq.SUBSCRIBE, ''.encode('utf-8'))
            messageAB = socketAB.recv()
            print('message B to A'+str(messageAB))
            time.sleep(5)

#########################################################################################A subscribe on C
def Subscriber2():

        portSC='12771' #listen  to Router C
        context = zmq.Context()
        socketAC = context.socket(zmq.SUB)
        socketAC.connect('tcp://localhost:%s' % portSC)
        while True:
            socketAC.setsockopt(zmq.SUBSCRIBE, ''.encode('utf-8'))
            messageAC = socketAC.recv()
            print('message C to A'+str(messageAC))
            time.sleep(5)
###########################################################################A subscribe on D
def Subscriber3():

        portSAD='13771' #listen  to Router D
        context = zmq.Context()
        socketAD = context.socket(zmq.SUB)
        socketAD.connect('tcp://localhost:%s' % portSAD)
        while True:
            socketAD.setsockopt(zmq.SUBSCRIBE, ''.encode('utf-8'))
            messageAD = socketAD.recv()
            print('message D to A'+str(messageAD))
            time.sleep(5)


############################################################################Main()
def main():

     Process(target=Publisher).start()
          # Now we can connect a client to all these servers
     Process(target=Subscriber1).start()
     Process(target=Subscriber2).start()
     Process(target=Subscriber3).start()

     #if sys.argv[1]=='OFF':
        #Process(target=Publisher).terminate()
       # Process(target=Subscriber1).terminate()
        #Process(target=Subscriber2).terminate()
        #Process(target=Subscriber3).terminate()




if __name__ == '__main__':
         main()