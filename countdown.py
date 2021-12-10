#!/usr/bin/env python3

def settime(strcd):
    from datetime import datetime
    try:
        datetime_obj=datetime.strptime(strcd, '%Y-%m-%d %H:%M')
        print(datetime_obj)
        file = open('.cdd.txt','w')
        file.write(datetime_obj.strftime('%Y-%m-%d %H:%M'))
        file.close()
    except:
        print("Make sure format is YYYY-MM-DD HH:MM")
        
def gettime():
    from datetime import datetime
    try:
        file = open('.cdd.txt','r')
        time=file.read()
        datetime_obj=datetime.strptime(time, '%Y-%m-%d %H:%M')
        difference = datetime_obj - datetime.now()
        humanized = (str(difference).split(':')[:2])
        humanized = humanized[0] +' hours ' + humanized [1] + ' minutes'
        return(humanized)

    except:
        print('error')

if __name__ == '__main__':
    print(gettime())
    
        
