from concurrent.futures import as_completed
from requests_futures.sessions import FuturesSession
from threading import Thread
url = 'https://WEBURL/Request'
check = False
maxThreads = 50



def getRequests():
    with FuturesSession() as webSession:
        #Update to Post/Get as necessary
        futures = [webSession.post(url)  for _ in range(500)]
        while True:
            try:
                for future in as_completed(futures):
                    response = future.result()
                    #print(str(response) + "\n")
                    if str(response) == "<Response [200]>":
                        print("up")
                        getRequests()
            except:
                pass


def main():
    global maxThreads
    threadCounter = 0
    threadsCreated = {}  
    
    while threadCounter <= maxThreads:
        key = threadCounter
        value = Thread(target=getRequests)
        
        threadsCreated[str(key)] = key
        threadsCreated[str(key)] = Thread(target=getRequests)
        threadCounter += 1
        
    for key,value in threadsCreated.items():
        key = value.start()
        
    for key,value in threadsCreated.items():
        key = value.join()
    
        
        
main()



