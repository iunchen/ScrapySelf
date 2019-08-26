from bs4 import BeautifulSoup
import re
#when init ok print use method
print('DivLink():\n  self.analysis(str,path)')
print('HrefLink():\n  self.analysis(str,path)')

#get next photo link
class DivLink():
    def __init__(self):
        self.path = ''
        self.str = ''
        self.__bstr = ''
        self.__read = ''
        #print('analysis([path] or [string])')

    def analysis(self,str='',path=''):
        self.path = path
        self.str = str
        #print('self.path:'+self.path,"path:"+self.path)
        try:
            if self.path != '':
                self.__read = ReadFile(self.path)
                self.__bstr = BeautifulSoup(self.__read)
                '''
                with open(path,'r',encoding='utf-8') as r:
                    self.__read = r.read()
                    #print(self.__read)
                    self.__bstr = BeautifulSoup(self.__read)
                    #print(self.__bstr)
                '''
            elif self.str != '':
                self.__bstr = BeautifulSoup(self.str)
        except Exception as error1:
            return error1
        #print(self.__bstr)
        #find backgroundPhoto in bing.com web sources
        divstr = self.__bstr.find(id="bgDiv")
        stylestr = divstr.get('style')
        match_element = re.compile('"(.*)"')
        linkstr = match_element.findall(stylestr)
        if linkstr != []:
            return ('https://cn.bing.com'+linkstr[0])
        else:
            return 'fail'

#get first photo link
class HrefLink():
    def __init__(self):
        self.__str = ''
        self.__path = ''

    def analysis(self,str='',path=''):
        self.__str = str
        self.__path = path
        #respon = requests.get(bing_url)
        if self.__path != '':
            after_rf = ReadFile(self.__path)
            after_bs = BeautifulSoup(after_rf)
        elif self.__str != '':
            after_bs = BeautifulSoup(self.__str)
        
        link_str = after_bs.find('link')
        if link_str != '':
            print(link_str)
            links = link_str.get('href')
            return 'https://cn.bing.com'+links
        else:
            return 'fail'
 
def ReadFile(vPath):
    with open(vPath,'r',encoding='utf-8') as r:
        vRead = r.read()
        return vRead


#PostScript:
#Beaucasue the first backgroudPhoto with history photo is not same location in bing.com sources
#So,i used twice method to get difference photo links: FirstPhoto is HrefLink() NextPhoto is DivLink()
#In same time,hope everone attention to first click 'previous' button need twice in bing.com homepage
#If have any suggestion can contact me :cenun@outlook.com
