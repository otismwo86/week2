time=[]
realhour=[]
availableconsultants=[]
selected=[]
def createlists(consultants):
    for consultant in consultants:
        name=consultant["name"]
        if name not in globals():
            globals()[name]=[]

def checktimeconflict(hours, name):
    for time in hours:
        if time in globals()[name]:
            return False
    return True
def checklist(hours,name):
    hoursset=set(hours)
    nameset=set(name)
    timeset=nameset.intersection(hoursset)
    return timeset
def book(consultants, hour, duration, criteria):
    createlists(consultants)
    inth=int(hour)
    intd=int(duration)
    realhour.append(inth)
    while intd>1:
        inth=inth+1
        realhour.append(inth)
        intd=intd-1

    for consultant in consultants:
        if checktimeconflict(realhour, consultant["name"]):
            availableconsultants.append(consultant)

    if not availableconsultants:
        print("No Service")
        realhour.clear()
        return
    if criteria=="price":
        #min(availableconsultants, key=lambda x: x["price"]) ====>{'name': 'Jenny', 'rate': 3.8, 'price': 800}
        minprice=min(availableconsultants, key=lambda x: x["price"])['price']#800
        for consultant in availableconsultants:
            if consultant["price"]==minprice:
                selected.append(consultant)
    if criteria=="rate":
        maxrate=max(availableconsultants, key=lambda x: x["rate"])['rate']
        for consultant in availableconsultants:
            if consultant["rate"]==maxrate:
                selected.append(consultant)


        
    print(selected[0]["name"])
    for n in realhour:
        globals()[selected[0]["name"]].append(n)
    availableconsultants.clear()
    realhour.clear()
    selected.clear()
consultants=[
    {"name":"John", "rate":4.5, "price":1000},
    {"name":"Bob", "rate":3, "price":1200},
    {"name":"Jenny", "rate":3.8, "price":800}
    ]
    


        
book(consultants, 15, 1, "price") # Jenny
book(consultants, 11, 2, "price") # Jenny
book(consultants, 10, 2, "price") # John
book(consultants, 20, 2, "rate") # John
book(consultants, 11, 1, "rate") # Bob
book(consultants, 11, 2, "rate") # No Service
book(consultants, 14, 3, "price") # John