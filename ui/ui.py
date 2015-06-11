'''
Created on Jun 11, 2015

@author: nex
'''

import os

class UserInterface:

    def __init__(self,crawler):

        self.link = "" #Website link
        self.file = "" #File to save link
        self.crawler = crawler
      
    def sign(self):
        #logo
        self.logo = """  ______                 _ _    _____                    _           
 |  ____|               (_) |  / ____|                  | |          
 | |__   _ __ ___   __ _ _| | | |     _ __ __ ___      _| | ___ _ __ 
 |  __| | '_ ` _ \ / _` | | | | |    | '__/ _` \ \ /\ / / |/ _ \ '__|
 | |____| | | | | | (_| | | | | |____| | | (_| |\ V  V /| |  __/ |   
 |______|_| |_| |_|\__,_|_|_|  \_____|_|  \__,_| \_/\_/ |_|\___|_|   
                                                                     
                                                                     """                                                                                                                        
        print(self.logo)
    
    def cls(self):
        #Clear Screen
        os.system(['clear','cls'][os.name == 'nt'])

    def run(self):
        
        while True:
           
            #Clear screen 
            self.cls()
            
            #Logo
            self.sign()
            
            #Get website link + validate
            self.link = input("Please insert website url: ")
            
            #Get file to save link
            self.file = input("Please insert filename to save links : ")
            
            
            #Crawl website
            self.crawler.crawl(self.link)
            
            