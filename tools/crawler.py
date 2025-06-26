'''
Created on Jun 26, 2025

@author: Alghisi Alessandro Paolo
'''

from multiprocessing import Process, Queue
from threading import Thread
import urllib.request

from bs4 import BeautifulSoup


class Crawler:
    '''
    The root of de BFS.
    '''

    def __init__(self):
        
        self.linksQ = Queue()
        
    def run(self,startLink):
        
        #Add link to Queue
        self.linksQ.put(startLink)
        #Start threads
        N = 1
        for i in range(N):
            t = Thread(target=self.crawl)
            t.daemon = True
            t.start()
        
        #Wait for workers
        
        #Join to be implemented
        
    def crawl(self):
        
        while True:
                
            #If Q not empty
            if not self.linksQ.empty():
                
                url = self.linksQ.get()
                print(url)
                
                try: 
                    #Get html page
                    resp = urllib.request.urlopen(url)
                    soup = BeautifulSoup(resp, from_encoding=resp.info().get_param('charset'))
                    
                    for link in soup.find_all('a', href=True):
                        #Fetch every url in the html
                        #Add link to Q
                        self.linksQ.put(link['href']);
                        print(link['href'])
                        
                #except urllib.error.URLError as e: ResponseData = e.read().decode("utf8", 'ignore')
                except ValueError:
                    print("Url fetch or decode error..")
