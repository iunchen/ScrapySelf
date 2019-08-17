from bs4 import BeautifulSoup
import re

class Link():
    def __init__(self):
        self.path = ''
        self.str = ''
        self.__bstr = ''
        self.__read = ''
        print('analysis([path] or [string])')
    def analysis(self,str='',path=''):
        self.path = path
        self.str = str
        print('self.path:'+self.path,"path:"+path)
        try:
            if self.path != '':
                with open(path,'r',encoding='utf-8') as r:
                    self.__read = r.read()
                    #print(self.__read)
                    self.__bstr = BeautifulSoup(self.__read)
                    #print(self.__bstr)
            elif self.str != '':
                self.__bstr = BeautifulSoup(self.str)
        except Exception as error1:
            return error1
        
        #print(self.__bstr)
        
        divstr = self.__bstr.find(id="bgDiv")
        stylestr = divstr.get('style')
        match_element = re.compile('"(.*)"')
        linkstr = match_element.findall(stylestr)
        if linkstr != []:
            return ('https://cn.bing.com'+linkstr[0])
        else:
            return 'fail'

