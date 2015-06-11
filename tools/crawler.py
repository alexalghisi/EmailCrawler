'''
Created on Jun 11, 2015

@author: nex
'''

from urllib.request import urlopen

class Crawler:
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
   
    def crawl(self,link):
        
        html = urlopen(link)
        print(html)