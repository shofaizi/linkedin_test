from selenium import webdriver


class Base:

    url = "http://www.linkedin.com"
    driver = webdriver.Chrome('/Users/Sho/Desktop/linkedin_test/chromedriver')

    def setUp(self):

        print("Opening :", self.url)
        self.driver.get(self.url)


    def tearDown(self):

        self.driver.close()
        self.driver.quit()
