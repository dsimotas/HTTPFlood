from concurrent.futures import as_completed
from requests_futures.sessions import FuturesSession
from threading import Thread
url = 'https://API/RequestURL'
        

def getRequests():   
    with FuturesSession() as webSession:
        
        while True:    
            futures = [webSession.get(url)  for _ in range(50)]
            for future in as_completed(futures):
                response = future.result()
                if str(response) == "<Response [429]>":
                    print("rate limited")
        
    

t1,t2,t3,t4,t5 = Thread(target=getRequests),Thread(target=getRequests),Thread(target=getRequests),Thread(target=getRequests),Thread(target=getRequests)


t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()


