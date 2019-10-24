from selenium import webdriver
import time, unittest

def Links(link):
    browser=webdriver.Chrome()
    browser.get(link)

    input1=browser.find_element_by_css_selector('.first_block input[placeholder="Input your first name"]')
    input1.send_keys("Ivan")
    input2=browser.find_element_by_css_selector('.first_block input[placeholder="Input your last name"]')
    input2.send_keys("Petrov")
    input3=browser.find_element_by_css_selector('.first_block input[placeholder="Input your email"]')
    input3.send_keys("121@mail.ru")
  
    button=browser.find_element_by_tag_name("button")    
    button.click()
       
    return browser.find_element_by_tag_name("h1").text

class TestPage(unittest.TestCase):
    def test_page1(self):
        self.assertEqual(Links("http://suninjuly.github.io/registration1.html"),"Congratulations! You have successfully registered!","Тест не пройден")
    
    def test_page2(self):
        self.assertEqual(Links("http://suninjuly.github.io/registration2.html"),"Congratulations! You have successfully registered!","Тест не пройден")
   
            
if __name__=="__main__":
    unittest.main()

