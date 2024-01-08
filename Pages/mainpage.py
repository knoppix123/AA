
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
    home_button = (By.CSS_SELECTOR, "//span[contains(text(),'skiplagged')]")

#==================================================================
    round_trip_button = (By.XPATH, "//span[contains(text(),'Round Trip')]")
    one_way_button = (By.XPATH, "//div[contains(text(),'One Way')]")
    departure_airport_field = (By.CSS_SELECTOR, "[class='src-input ui-autocomplete-input']")
    departure_sug_city =  (By.XPATH, "(//*[@class='autocomplete-title'])[1]")
    arrival_sug_city =  (By.XPATH, "(//*[@class='autocomplete-title'])[5]")


    arrival_airport_field = (By.CSS_SELECTOR, "[class='dst-input ui-autocomplete-input']")
    sug_miami = (By.XPATH, "(//*[contains(text(),'Miami Intl, Miami, Florida')])[1]")
    sug_paris = (By.XPATH, "//*[contains(text(),'Charles de Gaulle Intl, Paris, France')]")
    sug_honolulu = (By.XPATH, "//*[contains(text(),'Daniel K Inouye Intl, Honolulu, Hawaii')]" )
    sug_bogota = (By.XPATH, "//*[contains(text(),'El Dorado Intl, Bogota, Colombia')]")

    departure_calendar_field = (By.CSS_SELECTOR, "[placeholder='Depart']")
    back_arrow_calendar = (By.CSS_SELECTOR, "[class='ui-icon ui-icon-circle-triangle-w']")
    next_arrow_calendar = (By.CSS_SELECTOR, "[class='ui-icon ui-icon-circle-triangle-e']")
    search_button = (By.CSS_SELECTOR, "[class='blue-btn flight-search-form__search-button']")

    date_month =(By.XPATH, "(//*[@class = 'ui-datepicker-month'])[1]")
    close_button = (By.CSS_SELECTOR, "[data-dismiss='modal']")


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
    def get_sug_citya_departure(self):
        return self.driver.find_element(*Mainpage.departure_sug_city)

    def get_sug_city_arrival(self):
        return self.driver.find_element(*Mainpage.arrival_sug_city)
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
    def get_back_arrow_calendar(self):
        return self.driver.find_element(*Mainpage.back_arrow_calendar)

    def next_arrow_cal(self):
        return self.driver.find_element(*Mainpage.next_arrow_calendar)
    def next_arrow_cal2(self):
        self.driver.find_element(*Mainpage.next_arrow_calendar).click()
        self.driver.find_element(*Mainpage.next_arrow_calendar).click()

    def search_but(self):
        return self.driver.find_element(*Mainpage.search_button)

    def get_date_month(self):
        return self.driver.find_element(*Mainpage.date_month)

    def get_dynamic_date(self, date_day):
        return self.driver.find_element(By.XPATH, f"//*[@class='ui-datepicker-calendar']//*[contains(text(),'{date_day}')]")

    def get_arrival_sug_city_dynamic(self,city_name):
        return self.driver.find_element(By.XPATH, f"//*[@class='flight-search-form ui-front']//*[contains(text(),'{city_name}')]")


    def get_close_button(self):
        return self.driver.find_element(*Mainpage.close_button)
    def get_home_button(self):
        return self.driver.find_element(*Mainpage.home_button)

    def get_round_trip_button(self):
        return self.driver.find_element(*Mainpage.round_trip_button)
    def get_one_way_button(self):
        return self.driver.find_element(*Mainpage.one_way_button)












