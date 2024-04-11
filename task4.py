n=0

def get_number(index):
    if index%3==0:
        n=(index//3)*7
        print(n)
    elif index%3==1:
        n=(index//3)*7+4
        print(n)
    elif index%3==2:
        n=(index//3)*7+8
        print(n)
get_number(1) # print 4
get_number(5) # print 15
get_number(10) # print 25
get_number(30) # print 70