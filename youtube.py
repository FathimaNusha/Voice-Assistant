from selenium import webdriver
#search by elements
from selenium.webdriver.common.by import By

class video():
    def __init__(self):
        self.driver = webdriver.Chrome()


    def play(self,query):
        self.query= query
        self.driver.get(url="https://www.youtube.com/")
        search = self.driver.find_element(By.XPATH,'//*[@id="center"]/yt-searchbox/div[1]/form/input')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element(By.XPATH,'//*[@id="center"]/yt-searchbox/button/yt-icon/span/div')
        enter.click()
        fir_video= self.driver.find_element(By.XPATH,'//*[@id="video-title"]/yt-formatted-string')
        fir_video.click()

        input("wait unitil user close the webpage")

assist=video()
assist.play("believer")





#have to add functionality to read first paragraph of wikipedia page