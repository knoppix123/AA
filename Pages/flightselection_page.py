from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys



class Flight_selection:

    def __init__(self, driver):
        self.driver = driver

    select_cheapest_flight_departure = (By.CSS_SELECTOR, "[class='span2 trip-cost']")
    select_cheapest_flight_return = (By.XPATH, "((//*[@class='infinite-trip-list'])[2]//*[@class='span9 trip-path'])[1]")
    total_amount_of_trip = (By.CSS_SELECTOR, "[class='trip-highlight-cost-number']")



    def select_cheap_flight(self):
        return self.driver.find_element(*Flight_selection.select_cheapest_flight_departure)
    def select_cheap_return(self):
        return self.driver.find_element(*Flight_selection.select_cheapest_flight_return)
    def total_amt_of_trip(self):
        return self.driver.find_element(*Flight_selection.total_amount_of_trip)



