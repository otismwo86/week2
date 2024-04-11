all_station=["Songshan","Nanjing Sanmin","Taipei Arena","Nanjing Fuxing","Songjiang Nanjing","Zhongshan",
         "Beimen","Ximen","Xiaonanmen","Chiang Kai-Shek Memorial Hall","Guting","Taipower Building","Gongguan","Wanlong","Jingmei",
         "Dapinglin","Qizhang","Xiaobitan","Xindian City Hall","Xindian"]

station=["Songshan","Nanjing Sanmin","Taipei Arena","Nanjing Fuxing","Songjiang Nanjing","Zhongshan",
         "Beimen","Ximen","Xiaonanmen","Chiang Kai-Shek Memorial Hall","Guting","Taipower Building","Gongguan","Wanlong","Jingmei",
         "Dapinglin","Qizhang","Xindian City Hall","Xindian"]
friendloc=[]
locdict=[]
namedict=[]
def closevalue(list,k): #最接近的值
    closeelement=None
    x=float('inf')
    for n in list:
        c=abs(n-k)
        if c<x:
            x=c
            closeelement=n
    return closeelement
def find_closest_value(list,k): #與最近值的距離的最小值
    minuse=[]
    for n in list:
        c=abs(n-k)
        minuse.append(c)
    return min(minuse)
def find_and_print(messages, current_station):
    for data, location in messages.items():
        for n in all_station:
            if n in location:
                locdict.append(n)
                namedict.append(data)
                sta_dict=dict(zip(locdict,namedict))  #{'Xiaobitan': 'Leslie', 'Ximen': 'Bob', 'Jingmei': 'Mary', 'Taipei Arena': 'Copper', 'Xindian': 'Vivian'}
    if "Xiaobitan" in sta_dict:
        for data, location in messages.items():
            for n in station:
                if n in location:
                    order=station.index(n)
                    friendloc.append(order)
                    friendloc.sort()
                    x=station.index(current_station)
        loc=station[closevalue(friendloc,x)]
        lcc=find_closest_value(friendloc,x)
        if int(x)>16:
            if int(lcc)>int(x)-15:
                print(sta_dict["Xiaobitan"])
            else:
                print(sta_dict[loc])
        else:
            if int(lcc)>17-int(x):
                print(sta_dict["Xiaobitan"])
            else:
                print(sta_dict[loc])

    else:
        for data, location in messages.items():
            for n in station:
                if n in location:
                    order=station.index(n)
                    friendloc.append(order)
                    friendloc.sort()
                    x=station.index(current_station)
        loc=station[closevalue(friendloc,x)]
        lcc=find_closest_value(friendloc,x)
        print(sta_dict[loc])
        print(lcc)
        print(station.index(loc))            
messages={
"Leslie":"I'm at home near Xiaobitan station.",
"Bob":"I'm at Ximen MRT station.",
"Mary":"I have a drink near Jingmei MRT station.",
"Copper":"I just saw a concert at Taipei Arena.",
"Vivian":"I'm at Xindian station waiting for you."
}
find_and_print(messages, "Wanlong") # print Mary
find_and_print(messages, "Songshan") # print Copper
find_and_print(messages, "Qizhang") # print Leslie
find_and_print(messages, "Ximen") # print Bob
find_and_print(messages, "Xindian City Hall") # print Vivian