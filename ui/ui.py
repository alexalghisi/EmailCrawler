'''
Created on Jun 11, 2015

@author: nex
'''

class UserInterface:

    def __init__(self,crawler):

        self.link = "" #Website link
        self.crawler = crawler
        
    def run(self):
        
        while True:
            
            self.link = input("Please insert website url: ") #Get website link + validate
            
            