from selenium import webdriver
from time import sleep

class InstaBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://instagram.com')
        sleep(2)
        
        # Get username and password from txt file
        with open('secrets.txt', mode='r') as secrets:
            username = ''
            password = ''
            for line in secrets:
                if 'Instagram' in line:
                    line = secrets.readline()
                    username = line.split(': ')[1]

                    line = secrets.readline()
                    password = line.split(': ')[1]

                    break
        self.username = username
        self.password = password
        self.driver.find_element_by_xpath('//input[@name=\"username\"]')\
            .send_keys(username)
        self.driver.find_element_by_xpath('//input[@name=\"password\"]')\
            .send_keys(password)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(4)

        self.driver.find_element_by_xpath('//button[contains(text(), "Not Now")]')\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath('//button[contains(text(), "Not Now")]')\
            .click()
        sleep(2)
    
    def get_unfollowers(self):
        # Profile
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a')\
            .click()
        sleep(4)
        # Following
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a')\
            .click()
        following = self._get_names()

        # Followers
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a')\
            .click()
        followers = self._get_names()
        
        people = [user for user in following if user not in followers]
        for person in people:
            print(mofo)


    def _get_names(self):
        sleep(1)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        # Close Button
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/button')\
            .click()
            
        return names
        
my_bot = InstaBot()
my_bot.get_unfollowers()
