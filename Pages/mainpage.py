
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys



class Mainpage:

    def __init__(self, driver):
        self.driver = driver

    #mainmanubuttons===============

    # book_button = (By.XPATH, "//span[contains(text(),'BOOK')]")
    logo_button = (By.CSS_SELECTOR, "[class='logo']")
    flights_button = (By.XPATH, "//*[contains(text(),'Flights')]")
    stays_button = (By.XPATH, "//*[contains(text(),'Stays')]")
    cars_button = (By.XPATH, "//a[contains(text(),'Cars')]")
    rewards_button = (By.XPATH, "//a[contains(text(),'Rewards')]")
    deals_button = (By.XPATH, "//a[contains(text(),'Deals')]")
    login_button = (By.XPATH, "//a[contains(text(),'Login')]")
    email_field = (By.CSS_SELECTOR, "[placeholder='Email Address']")
    password_field = (By.CSS_SELECTOR, "[placeholder='Password']")
    sign_in_button = (By.CSS_SELECTOR, "[class='blue-btn']")

#==================================================================
    departure_airport_field = (By.CSS_SELECTOR, "[class='src-input ui-autocomplete-input']")
    sug_atlanta =  (By.XPATH, "(//*[@class='autocomplete-title'])[1]")
    arrival_airport_field = (By.CSS_SELECTOR, "[class='dst-input ui-autocomplete-input']")
    sug_miami = (By.XPATH, "(//*[contains(text(),'Miami Intl, Miami, Florida')])[1]")
    sug_paris = (By.XPATH, "//*[contains(text(),'Charles de Gaulle Intl, Paris, France')]")
    sug_honolulu = (By.XPATH, "//*[contains(text(),'Daniel K Inouye Intl, Honolulu, Hawaii')]" )
    sug_bogota = (By.XPATH, "//*[contains(text(),'El Dorado Intl, Bogota, Colombia')]")

    departure_calendar_field = (By.CSS_SELECTOR, "[placeholder='Depart']")
    next_arrow_calendar = (By.CSS_SELECTOR, "[class='ui-icon ui-icon-circle-triangle-e']")
    date_25_january = (By.XPATH, "//*[@class='ui-datepicker-calendar']//*[contains(text(),'25')]")
    date_04_february = (By.XPATH, "//*[@class='ui-datepicker-calendar']//*[contains(text(),'4')]")
    date_21_december = (By.XPATH, "//a[contains(text(),'21')]")
    date_02_january = (By.XPATH, "//a[contains(text(),'2')]")
    search_button = (By.CSS_SELECTOR, "[class='blue-btn flight-search-form__search-button']")
    asdasds = "dadfs "


    def logo(self):
        return self.driver.find_element(*Mainpage.logo_button)
    def flights(self):
        return self.driver.find_element(*Mainpage.flights_button)
    def stays(self):
        return self.driver.find_element(*Mainpage.stays_button)
    def cars(self):
        return  self.driver.find_element(*Mainpage.cars_button)
    def rewards(self):
        return self.driver.find_element(*Mainpage.rewards_button)
    def deals(self):
        return self.driver.find_element(*Mainpage.deals_button)
    def login(self):
        return self.driver.find_element(*Mainpage.login_button)
    def email(self):
        return self.driver.find_element(*Mainpage.email_field)
    def password(self):
        return self.driver.find_element(*Mainpage.password_field)
    def signin(self):
        return self.driver.find_element(*Mainpage.sign_in_button)

#===================================================================
    def departure_airport(self):
        return self.driver.find_element(*Mainpage.departure_airport_field)
    def sug_atl(self):
        return self.driver.find_element(*Mainpage.sug_atlanta)
    def arrival_airport(self):
        return self.driver.find_element(*Mainpage.arrival_airport_field)
    def sug_mia(self):
        return self.driver.find_element(*Mainpage.sug_miami)
    def sug_cdg_paris(self):
        return self.driver.find_element(*Mainpage.sug_paris)
    def sug_hnl_honolulu(self):
        return self.driver.find_element(*Mainpage.sug_honolulu)
    def sug_bog_bogota(self):
        return self.driver.find_element(*Mainpage.sug_bogota)
#============================================================================
    def departure_calendar(self):
        return self.driver.find_element(*Mainpage.departure_calendar_field)
    def next_arrow_cal(self):
        return self.driver.find_element(*Mainpage.next_arrow_calendar)
    def date_25_jan(self):
        return self.driver.find_element(*Mainpage.date_25_january)
    def date_04_feb(self):
        return self.driver.find_element(*Mainpage.date_04_february)
    def date_21_dec(self):
        return self.driver.find_element(*Mainpage.date_21_december)
    def date_02_jan(self):
        return self.driver.find_element(*Mainpage.date_02_january)
    def search_but(self):
        return self.driver.find_element(*Mainpage.search_button)











