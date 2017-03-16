#Graph illustration
import pylab
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import math
from tkinter import *
from tkinter import messagebox
import string
import os
import socket
import ipaddress
import json
from subprocess import Popen
import subprocess


#############################################################################variables
global pos
global proc # the dictionary of Process with name of routers as key
global annotes,x,y
global data
global xdata;global ydata
global color_list
global As_dict
global lstedge
global number_nodes
global Router
global Router_Status
global IP_Port_dict
global graph
global As_numbers_dict
proc={}
As_numbers_dict={}
Router=''
Router_Status = {'A': 'OFF', 'B': 'OFF', 'C': 'OFF', 'D': 'OFF', 'E': 'OFF', 'F': 'OFF', 'G': 'OFF', 'H': 'OFF',\
                 'I': 'OFF', 'J': 'OFF'}

############################################################################Graph lables and colors
def RouterGraph(color_list=['r','r','r','r','r','r','r','r','r','r'] ):

            graph = {'A': {'B': {'IP':{}} ,'C': {'IP':{}},'D':{'IP':{}}},
                     'B': {'A': {'IP':{}}, 'C': {'IP':{}}},
                     'C': {'A': {'IP':{}},'B': {'IP':{}}},
                     'D': { 'A': {'IP':{}}, 'E': {'IP':{}}, 'J': {'IP':{}},'F': {'IP':{}}},
                     'E': {'D': {'IP':{}}, 'H': {'IP':{}},'G': {'IP':{}},'F': {'IP':{}}},
                     'F': {'E': {'IP':{}},'I': {'IP':{}},'D': {'IP':{}}},
                     'G': { 'E': {'IP':{}}},
                     'H': { 'E': {'IP':{}},'J': {'IP':{}}},
                     'I': { 'F': {'IP':{}}},
                     'J': {'D': {'IP':{}},'H': {'IP':{}}}}
            fig = plt.figure()

            ax = fig.add_subplot(111)

            ax.set_title('select the router')

            G = nx.Graph()

            labels = {'A':'Ra', 'B':'Rb','C':'Rc','D':'Rd','E':'Re','F':'Rf','G':'Rg','H':'Rh','I':'Ri','J':'Rj'}
            lstedge = []  # list of edges

            for i in graph.keys():
                for j in graph[i]:
                    if i != j:
                        lstedge.append((i, j))

            G.add_edges_from(lstedge)

            pos = {}
            pos['A'] = np.array([10, 10])
            pos['B'] = np.array([7,7])
            pos['C'] = np.array([13, 7])
            pos['D'] = np.array([4, 10])
            pos['E'] = np.array([1, 10])
            pos['F'] = np.array([-2, 13])
            pos['G'] = np.array([-2, 7])
            pos['H'] = np.array([-1, 4])
            pos['I'] = np.array([-5, 13])
            pos['J'] = np.array([4, -2])
            number_nodes = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
            nx.draw_networkx(G, pos, nodelist=['A','B','C','D','E','F','G','H','I','J'],node_size=500, node_color=color_list, with_labels=True, labels=labels,fixed=True,cmap=None)
            def oneclick(event):  # clickable canvas
                if event.inaxes is not None:
                    ax = event.inaxes
                    xdata=event.xdata; ydata=event.ydata
                    position = {}
                    length = 0

                    for Router in pos.keys():  # for each key in pos variable which return touple of node coords & calculate the distanceto nodes

                        data=pos[Router].tolist() # to convert array to list

                        xpos=data[0];ypos=data[1]
                        length = math.sqrt(pow((xdata - xpos),2 )+ pow((ydata - ypos),2))

                        if length <= 1: #if mouse clicks a nodes

                                Number_of_Niegbours=G.neighbors(Router)

                                box(Router,graph,proc)####Invoking Box Function

                                if Router_Status[Router]=='ON':
                                    color_list.pop(number_nodes[Router])
                                    color_list.insert(number_nodes[Router], 'g')

                                    Multiprocessing_Routers(Router,graph,As_numbers_dict,Router_Status)
                                    # Invoking os of routers
                                else:

                                    color_list.pop(number_nodes[Router])
                                    color_list.insert(number_nodes[Router], 'r')

                    plt.close()

                    RouterGraph(color_list)
            cid = fig.canvas.mpl_connect('button_press_event', oneclick)

            plt.show()

            if plt.close()==None: # with closing window all process will be terminate.
                for Router in Router_Status:

                    Router_Status[Router]='OFF'
                    proc[Router] = (
                    subprocess.Popen([sys.executable, os.getcwd() + '/' + Router + '.py', Router_Status[Router]],
                                     shell=False, stderr=True,
                                     stdout=subprocess.PIPE))
                    del proc[Router]
            print(proc)
################################################################################ Multiprocessing  Routers
def Multiprocessing_Routers(Router,graph,As_numbers_dict,Router_status):
         socket_name={'A':'Ra', 'B':'Rb','C':'Rc','D':'Rd','E':'Re','F':'Rf','G':'Rg','H':'Rh','I':'Ri','J':'Rj'}

         proc[Router]=(subprocess.Popen([sys.executable, os.getcwd() + '/' + Router + '.py', Router_Status[Router]], shell=False, stderr=True,
                                      stdout=subprocess.PIPE))
         print(graph[Router])
         print(proc)
         #for i in graph[Router].keys():
         print(Router)
                  #print('----------')
                  #if i not in proc: # if the process did not run before for the router i
                       #if Router_Status[i]=='ON':


                                  #proc[i]=(subprocess.Popen([sys.executable, os.getcwd() + '/' + i + '.py',Router_Status[i]], shell=False, stderr=True,
                                           #stdout=subprocess.PIPE))
                       #else:
                              #pass

###########################################################################################BOX
def box(Router,graph,proc):

     path = os.path.expanduser('~' + '/BGP_Routers/' + Router)


     if Router_Status[Router]=='OFF':

         if not os.path.exists(path):
             os.makedirs(path)
         if not os.path.isfile(path + '/' + Router + '_Info.txt'): # if there is not info file show Box
                master = Tk()
                master.title('Router'+ Router)
                Label(master, text="User name").grid(row=0)
                Label(master, text="Password").grid(row=1)
                Label(master, text='As Number').grid(row=2)
                e1 = Entry(master) # username
                e2 = Entry(master,show='*') #pass
                e3 = Entry(master) #As number
                e1.grid(row=0, column=1)
                e2.grid(row=1, column=1)
                e3.grid(row=2, column=1)
                def show_entry_fields():
                           username=e1.get()
                           password=e2.get()
                           As_number = e3.get()

                           if e1.get()=='veria' and int(e2.get())==123 :
                                    if (int(As_number) > 1) and  (int(As_number) < 64495) :

                                             plt.close()

                                             master1 = Tk()
                                             master1.title('IP Address')

                                             def check_eth():

                                                 for k in entries:

                                                        try:
                                                            eth = ipaddress.ip_address(k[1].get())
                                                        except ValueError:
                                                            messagebox.showinfo('ERROR','address/netmask is invalid for IPv4:'+ k[1].get())
                                                            return
                                                        graph[Router][k[0]]['IP'] = k[1].get()


                                                 master1.destroy()

                                             j = 1  # number of rows for getting eths
                                             entries = []  # for each eth builds a row
                                             for i in graph[Router]:
                                                    b1 = Entry(master1)
                                                    Label(master1, text='Interface serial '+i).grid(row=j, column=0)
                                                    b1.grid(row=j, column=1)
                                                    j = j + 1
                                                    entries.append((i, b1)) # entries is list of tuples which index 0 is ethof  router
                                                    # and index 1 is ip of eth

                                             Button(master1, text='Enter IP', command=check_eth).grid(row=j,
                                                                                                          column=0,
                                                                                                          sticky=W,
                                                                                                          pady=4)



                                             #Router_info.close()
                                             Router_Status[Router] = 'ON'
                                             master.destroy()
                                             mainloop()
                                             with open(path + '/' + Router + '_Info.txt', 'w') as Router_info:
                                                 Router_info.write('router BGP-4' + '\t' + Router + '\n' \
                                                                   + username + '\t' + password + '\n' \
                                                                   + As_number )

                                             with open(path + '/' + 'neigbors' + Router + '_Info.txt', 'w') as Router_neigbors:
                                                 Router_neigbors.write(json.dumps(graph[Router]))
                                             As_numbers_dict[Router]=As_number # Adding As number to router in dictionary

                                    else:

                                             messagebox.showinfo('Error', 'Invalid As number'+'\n'+'Please enter public AS number')

                           else :

                                    messagebox.showinfo('Error', 'Authentication Error')


                def Turn_off(): # Turn off button in Entry Box
                    Router_Status[Router] = 'OFF'
                    master.destroy()
                    #plt.close()

                Button(master, text='Turn Off', command=Turn_off).grid(row=5, column=0, sticky=W, pady=4)
                Button(master, text='Turn On', command= show_entry_fields).grid(row=5, column=1, sticky=W, pady=4)

                mainloop()

         else:

             Router_Status[Router] = 'ON' # here router must read info files to primary start
             with open(path + '/' + 'neigbors' + Router + '_Info.txt', 'r') as Router_neigbors:

                 graph[Router]=json.loads(Router_neigbors.read())
             with open (path + '/' + Router + '_Info.txt', 'r') as Router_info:
                 info=Router_info.readlines() # it removes /n

                 As_numbers_dict[Router]=info[2] # it reads As-number from text file


     else :

         #It means the light is off and terminate all process
         Router_Status[Router]='OFF'
         print(proc)
         proc[Router]=subprocess.Popen([sys.executable, os.getcwd() + '/' + Router + '.py', Router_Status[Router]],shell=False, stderr=True,stdout=subprocess.PIPE)
         del proc[Router]
         print(proc)
#########################################################################################################################
def main():

    IP_Port_dict={}

    RouterGraph()










if __name__ == '__main__':
    main()