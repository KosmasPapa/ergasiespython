import datetime
import json
import urllib2

cur_date=datetime.datetime.now()


yournums=[]
for i in range(10):
    x=input("dwse arithmo apo 1-80:")
    while x<1 or x>80:
        x=input("dwse 3ana apo to 1 mexri to 80!!:")
        
    yournums.append(x)

print "oi aritmoi sou einai:",yournums
perissoteres=0
mera=0
for i in range(31):
    cur_date=cur_date - datetime.timedelta(days=1)
    date_str= cur_date.strftime("%d-%m-%Y")
    url='http://applications.opap.gr/DrawsRestServices/kino/drawDate/%s.json'%date_str
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    data = response.read()
    data=json.loads(data)
    klhrwseis= data['draws']['draw']
    
    for k in klhrwseis:
        s=0
        tmp=k["results"]
        for i in yournums:
            if i in tmp:
                 s+=1
        if s>4 and s>perissoteres:
              perissoteres=s
              mera=date_str
         
print "h mera me tis perissoteres epituxies einai:",mera     
