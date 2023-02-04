from datetime import datetime
f = open("a_b_schedule.txt")
data = []
for line in f.readlines():
    a = [x.strip() for x in line.split(' ')]
    data.append({
        'date': a[0],
        'dow':  a[1],
        'a_b':  a[2]
    })
    
data.sort(key = lambda date: datetime.strptime(date['date'], "%m/%d/%Y"))
for x in data:
    endtime = "5:30" if x['dow'] != "Friday" else "2:20" if x['a_b'][0] ==  'B' else "3:55"
    ans = "" + x['date'] + " " + x['dow'] + " " + x['a_b']
    if(x['a_b'][0] != 'B'):
        print(ans, "LASA", "8:15 a.m. -", endtime, 'p.m.')
    else:
        print(ans, "LBJ", "9:00 a.m. -", endtime, 'p.m.')
f.close()