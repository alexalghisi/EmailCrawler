'''
Created on Jun 11, 2015

@author: nex
'''

from tools.crawler import Crawler
from ui.ui import UserInterface


if __name__ == '__main__':
    
    crawler = Crawler()
    UI = UserInterface(crawler)
    UI.run()