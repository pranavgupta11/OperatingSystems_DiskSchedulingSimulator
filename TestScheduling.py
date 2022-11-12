from heapq import *
import matplotlib.pyplot as plt
avgSt = []

def FCFS(hp,requests,t):
    print("  **********     First Come First Serve       *********")
    time = 0
    n = len(requests)
    pos = hp
    yCoord = []
    yCoord.append(hp)
    xCoord = [i for i in range(0, n+1)]
    for request in requests:
        time += abs(request-pos)
        pos = request
        yCoord.append(pos)
        print("        ",pos,"  Seeked")
    # calculate average seek time
    avg_seek_time = time / n
    print("Avg Seek time for  FCFS : ", avg_seek_time)
    choice=getMenu()
    if choice == 0:
        plotSeekSequence(xCoord, yCoord, "First Come First Serve", t)
    else:
        plotSeekSequenceReverse(xCoord, yCoord, "First Come First Serve", t)
    return xCoord,yCoord

def SSTF(hp,reqs, t):
    print("  **********     Shortest Seek Time First       *********")
    requests = reqs.copy()
    time = 0
    position = hp
    n = len(requests)
    heap=[]
    yCoord = []
    yCoord.append(hp)
    xCoord = [i for i in range(0, n+1)]
    while len(requests)>0:
        for r in requests:
            heappush(heap,(abs(position-r),r))
        x=heappop(heap)[1]
        time+=abs(position-x)
        position=x
        yCoord.append(x)
        print("        ",x,"  Seeked")
        requests.remove(x)
        heap=[]
    # calculate average seek time
    avg_seek_time = time/n
    print("Avg Seek time for SSTF : ", avg_seek_time)
    choice=getMenu()
    if choice == 0:
        plotSeekSequence(xCoord, yCoord, "Shortest Seek Time First", t)
    else:
        plotSeekSequenceReverse(xCoord, yCoord, "Shortest Seek Time First", t)
    return xCoord,yCoord

def SCAN(hp,reqs, t):
    print("  **********     SCAN       *********")
    requests = reqs.copy()
    pos = hp
    time = 0
    n = len(requests)
    yCoord = []
    yCoord.append(hp)
    xCoord = [i for i in range(0, n+2)]
    end=t
    start=0
    #seek from curr_pos to end which is t
    for i in range(pos,end+1):
        if i in requests:
            time+=abs(pos-i)
            pos=i
            yCoord.append(i)
            print("        ",i,"  seeked")
            requests.remove(i)

    time+=abs(pos-end)
    pos=end
    yCoord.append(pos)
    #seek back to start
    for i in range(end,start-1,-1):
        if i in requests:
            time+=abs(pos-i)
            # print(time)
            pos=i
            yCoord.append(i)
            print("        ",i,"  seeked")
            requests.remove(i)
    # calculate average seek time
    avg_seek_time = time/n
    print("Avg Seek time for SCAN Algorithm : ", avg_seek_time)
    choice=getMenu()
    if choice == 0:
        plotSeekSequence(xCoord, yCoord, "SCAN Algorithm", t)
    else:
        plotSeekSequenceReverse(xCoord, yCoord, "SCAN Algorithm", t)
    return xCoord,yCoord

def C_SCAN(hp,reqs, t):
    print("  **********     C-SCAN     *********")
    requests = reqs.copy()
    pos = hp
    time = 0
    n = len(requests)
    yCoord = []
    yCoord.append(hp)
    xCoord = [i for i in range(0, n+1+2)]
    end=t
    start=0
    #seek from curr_pos to end which is t
    for i in range(pos,end+1):
        if i in requests:
            time+=abs(pos-i)
            pos=i
            yCoord.append(i)
            print("        ",i,"  seeked")
            requests.remove(i)
    time+=abs(pos-end)
    pos=end
    yCoord.append(pos)
    yCoord.append(start)
    #seek to hp from start
    for i in range(start,hp+1):
        if i in requests:
            time+=abs(pos-i)
            pos=i
            yCoord.append(i)
            print("        ",i,"  seeked")
            requests.remove(i)
    # calculate average seek time
    avg_seek_time = time/n
    print("Avg Seek time for C-SCAN Algorithm : ", avg_seek_time)
    choice=getMenu()
    if choice == 0:
        plotSeekSequence(xCoord, yCoord, "C-SCAN Algorithm", t)
    else:
        plotSeekSequenceReverse(xCoord, yCoord, "C-SCAN Algorithm", t)
    return xCoord,yCoord

def LOOK(hp,reqs, t):
    print("  **********     LOOK       *********")
    requests = reqs.copy()
    pos = hp
    time = 0
    n = len(requests)
    yCoord = []
    yCoord.append(hp)
    xCoord = [i for i in range(0, n+1)]
    end=max(requests)
    start=min(requests)
    #seek from curr_pos to end max
    for i in range(pos,end+1):
        if i in requests:
            time+=abs(pos-i)
            pos=i
            yCoord.append(i)
            print("        ",i,"  seeked")
            requests.remove(i)

    #seek back to start
    for i in range(end,start-1,-1):
        if i in requests:
            time+=abs(pos-i)
            pos=i
            yCoord.append(i)
            print("        ",i,"  seeked")
            requests.remove(i)
    print(time)
    # calculate average seek time
    avg_seek_time = time/n
    print("Avg Seek time for LOOK Algorithm : ", avg_seek_time)
    choice=getMenu()
    if choice == 0:
        plotSeekSequence(xCoord, yCoord, "LOOK Algorithm", t)
    else:
        plotSeekSequenceReverse(xCoord, yCoord, "LOOK Algorithm", t)
    return xCoord,yCoord

def C_LOOK(hp,reqs, t):
    print("  **********     C-LOOK     *********")
    requests = reqs.copy()
    pos = hp
    time = 0
    n = len(requests)
    yCoord = []
    yCoord.append(hp)
    xCoord = [i for i in range(0, n+1)]
    end=max(requests)
    start=min(requests)
    #seek from curr_pos to max of list 
    for i in range(pos,end+1):
        if i in requests:
            time+=abs(pos-i)
            pos=i
            yCoord.append(i)
            print("        ",i,"  seeked")
            requests.remove(i)

    time+=abs(pos-start)
    pos=start
    #seek to hp from start
    for i in range(start,hp+1):
        if i in requests:
            time+=abs(pos-i)
            pos=i
            yCoord.append(i)
            print("        ",i,"  seeked")
            requests.remove(i)
    # calculate average seek time
    avg_seek_time = time/n
    print("Avg Seek time for C-LOOK Algorithm : ", avg_seek_time)
    choice=getMenu()
    if choice == 0:
        plotSeekSequence(xCoord, yCoord, "C-LOOK Algorithm", t)
    else:
        plotSeekSequenceReverse(xCoord, yCoord, "C-LOOK Algorithm", t)
    return xCoord,yCoord

def plotComparison(x, y):
    plt.bar(x, y, tick_label = x, width = 0.8, color = ['red', 'green'])
    plt.xlabel('Scheduling Algorith')
    plt.ylabel('Average Seek Time')
    plt.title('Comparative Analysis')
    plt.show() 

def plotSeekSequence(x, y, title,t):
    plt.plot(x, y, color = 'green', linestyle = 'dashed', linewidth = 3, marker = 'o', markerfacecolor = 'blue', markersize = 12)
    plt.ylim(1, t+1)
    plt.xlim(0, n+1)
    plt.xlabel('Requests')
    plt.ylabel('Tracks Visited')
    plt.title(title)
    plt.show()

def plotSeekSequenceReverse(x, y, title, t):
    plt.plot(y, x, color = 'green', linestyle = 'dashed', linewidth = 3, marker = 'o', markerfacecolor = 'blue', markersize = 12)
    plt.xlim(1, t)
    plt.ylim(0, n+1)
    plt.ylabel('Requests')
    plt.xlabel('Tracks Visited')
    plt.title(title)
    plt.show()

def CumulativePlotDesign(x1, x2, x3, x4, x5, x6 ,y1, y2, y3, y4, y5, y6):

    plt.plot(x1,y1,label = "FCFS")
    plt.plot(x2,y2,label = "SSTF")
    plt.plot(x3,y3,label = "SCAN")
    plt.plot(x4,y4,label = "C-SCAN")
    plt.plot(x5,y5,label = "LOOK")
    plt.plot(x6,y6,label = "C-LOOK")
    # naming the x axis
    plt.xlabel('Requests')
    # naming the y axis
    plt.ylabel('Track Visited')
    # giving a title to my graph
    plt.title('CUMULATIVE ANALYSIS')
    # show a legend on the plot
    plt.legend()
    # function to show the plot
    plt.show()

def CumulativePlotDesignReverse(x1, x2, x3, x4, x5, x6 ,y1, y2, y3, y4, y5, y6):
    
    plt.plot(y1,x1,label = "FCFS")
    plt.plot(y2,x2,label = "SSTF")
    plt.plot(y3,x3,label = "SCAN")
    plt.plot(y4,x4,label = "C-SCAN")
    plt.plot(y5,x5,label = "LOOK")
    plt.plot(y6,x6,label = "C-LOOK")
    # naming the x axis
    plt.xlabel('Tracks Visited')
    # naming the y axis
    plt.ylabel('Requests')
    # giving a title to my graph
    plt.title('CUMULATIVE ANALYSIS')
    # show a legend on the plot
    plt.legend()
    # function to show the plot
    plt.show()

def getMenu():
    print("""
    1. Plot Track Visited Vs Requests
    2. Plot Requests Vs Track Visited
    """)   
    choice = int(input("Enter your Choice for Graph Selection : "))
    return choice-1


#**********************     M   A   I   N   ************************

if __name__ == '__main__':
    print(""" 
    OPERATING SYSTEM AND SYSTEM PROGRAMMING LAB
                    [15B17CI472]
                        PBL
    COMPARATIVE ANALYSIS OF DISK SCHEDULING ALGORITHMS
    """)
    
    print("Provide the number of I/O requests")
    n = int(input())
    print("Provide the total number of tracks")
    t = int(input())
    print("Provide initial position of the Actuator arm (total cylinders=",t,")")
    hp = int(input())
    while hp > t:
        print("!!! INVALID !!! try again")
        hp = int(input())
    print("Provide positions to visit : max is ",t)
    requests = []
    for i in range(n):
        req = int(input())
        requests.append(req)

    print(requests)
    print("""
            Enter the corresponding number for the disk scheduling algorithm:
            1. FCFS
            2. SSTF
            3. SCAN
            4. C-SCAN
            5. LOOK
            6. C-LOOK
            7. CUMULATIVE
            8. EXIT
            """
          )

    algoInput = int(input("Enter your choice: "))
    while algoInput != 8:
        if algoInput == 1:
            FCFS(hp, requests, t)
        elif algoInput == 2:
            SSTF(hp, requests, t)
        elif algoInput == 3:
            SCAN(hp, requests, t)
        elif algoInput == 4:
            C_SCAN(hp, requests, t)
        elif algoInput == 5:
            LOOK(hp, requests, t)
        elif algoInput == 6:
            C_LOOK(hp, requests, t)
        elif algoInput == 7:
            xCoord = [i for i in range(1, n+1)]
            print("  **********     ANALYSIS       *********")
            x1,y1 = FCFS(hp, requests, t)
            x2,y2 = SSTF(hp, requests, t)
            x3,y3 = SCAN(hp, requests, t)
            x4,y4 = C_SCAN(hp, requests, t)
            x5,y5 = LOOK(hp, requests, t)
            x6,y6 = C_LOOK(hp, requests, t)
            choice = getMenu()
            if choice == 0:
                CumulativePlotDesign(x1, x2, x3, x4, x5, x6, y1, y2, y3, y4, y5, y6)
            else:
                CumulativePlotDesignReverse(x1, x2, x3, x4, x5, x6, y1, y2, y3, y4, y5, y6)
        else:
            print("You entered a wrong choice. Try again")
        algoInput = int(input("Enter your choice: "))
    
    
    
    print(""" 
    ##################      MEMBERS        ###############
    1. PRANAV GUPTA 19803021
    2. KHUSHBOO KUMARI 19803003
    3. KANISTHA 198030
    4. KANISHKA KHULLAR 19803011
    5. RITAWARI PAREEK 19803009

    ********** THANKS FOR USING THE SIMULATION ***************
    """)