from selenium import webdriver
from selenium.webdriver.common.by import By

class music():
    def __init__(self):
        self.driver = webdriver.Chrome()


    def play(self,query):
        self.query= query
        self.driver.get(url="https://www.youtube.com/results?search_query=" + query)
        video= self.driver.find_element(By.XPATH,'//*[@id="title-wrapper"]/h3')
        video.click()

        input("wait unitil user close the webpage")





#have to add functionality to read first paragraph of wikipedia page