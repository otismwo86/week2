mid=[]
uniq=[]
def func(*data):
    for name in data:
        length=len(name)
        if length==2:
            
            mid.append(name[1])
        elif length==3:
            
            mid.append(name[1])
        elif length==4:
            
            mid.append(name[2])
        elif length==5:
            
            mid.append(name[2])
       
    for uni in mid:
        if mid.count(uni)==1:
            uniq.append(uni)
    
    for n in data:
        if uniq==[]:
            print("沒有")
            break
        elif uniq !=[]:
            if uniq[0] in n:
                print(n)
    
    uniq.clear()
    mid.clear()
func("彭大牆", "陳王明雅", "吳明") # print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆") # print 夏曼藍波安

