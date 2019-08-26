import requests

#download url content,input one number to name image
class DownloadPhoto():
    def __inti__(self):
        self.__url = ''

    def get(self,target_url):
        self.__url = target_url
        img = requests.get(self.__url)
        m = input("Input photo series number:")
        with open('./bingbackimage'+str(m)+'.jpeg','wb') as f:
            f.write(img.content)
