from selenium.webdriver.common.by import By
import time
from selenium import webdriver
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from test_setup.webdriver_setup import se
from Pages.mainpage import Mainpage
from Pages.flightselection_page import Flight_selection


@pytest.fixture
def mainpage_instance(se):
    MP = Mainpage(se)
    FP = Flight_selection(se)
    return MP, FP



def test_accept_logo(mainpage_instance):
    MP, FP =mainpage_instance
    logo = MP.logo()
    logo.click()
    time.sleep(3)
    title = MP.driver.title
    assert title == "Skiplagged: The smart way to find cheap flights."

def test_accept_flight(mainpage_instance):
    MP, FP =mainpage_instance
    logo = MP.flights()
    logo.click()
    time.sleep(3)
    title = MP.driver.title
    assert title == "Skiplagged: The smart way to find cheap flights."


def test_accept_stays(mainpage_instance):
    MP, FP =mainpage_instance
    login = MP.stays()
    login.click()
    time.sleep(3)
    title = MP.driver.title
    assert title == "Find & Book Top Stays | Up To 60% off | Skiplagged"

def test_accept_cars(mainpage_instance):
    MP, FP =mainpage_instance
    login = MP.cars()
    login.click()
    time.sleep(3)
    title = MP.driver.title
    assert title == "Skiplagged - Car Rentals"

def test_accept_rewards(mainpage_instance):
    MP, FP =mainpage_instance
    login = MP.rewards()
    login.click()
    time.sleep(3)
    title = MP.driver.title
    assert title == "Earn Up To $25 per Booking | Rewards | Skiplagged"

def test_accept_rewards(mainpage_instance):
    MP, FP =mainpage_instance
    login = MP.rewards()
    login.click()
    time.sleep(3)
    title = MP.driver.title
    assert title == "Earn Up To $25 per Booking | Rewards | Skiplagged"

def test_accept_deals(mainpage_instance):
    MP, FP =mainpage_instance
    login = MP.deals()
    login.click()
    time.sleep(3)
    title = MP.driver.title
    assert title == "Newsletter Sign Up | Skiplagged"

def test_accept_logn(mainpage_instance):
    MP, FP =mainpage_instance
    login = MP.login()
    login.click()
    time.sleep(3)

def test_login_positive(mainpage_instance):
    MP, FP =mainpage_instance
    login = MP.login()
    login.click()
    MP.email().send_keys("knoppix123@gmail.com")
    MP.password().send_keys("a171205$wd")
    time.sleep(3)
    MP.signin().click()
    time.sleep(3)

def test_login_negative_email(mainpage_instance):
    MP, FP =mainpage_instance
    login = MP.login()
    login.click()
    MP.email().send_keys("knoppixil.com")
    MP.password().send_keys("a171205$wd")
    time.sleep(3)
    MP.signin().click()
    time.sleep(3)

def test_login_negative_password(mainpage_instance):
    MP, FP =mainpage_instance
    login = MP.login()
    login.click()
    MP.email().send_keys("knoppix123@gmail.com")
    MP.password().send_keys("a1712")
    time.sleep(3)
    MP.signin().click()
    time.sleep(3)

def test_flight_book_MIA(mainpage_instance):
    MP, FP =mainpage_instance
    wait = WebDriverWait(MP.driver, 10)
    MP.departure_airport().clear()
    MP.departure_airport().send_keys("ATL")
    time.sleep(1)
    MP.sug_atl().click()
    MP.arrival_airport().clear()
    MP.arrival_airport().send_keys("MIA")
    wait.until(EC.element_to_be_clickable(MP.sug_mia())).click()
    time.sleep(1)
    MP.departure_calendar().click()
    time.sleep(1)
    MP.next_arrow_cal().click()
    MP.next_arrow_cal().click()
    MP.next_arrow_cal().click()
    MP.date_25_jan().click()
    MP.next_arrow_cal().click()
    MP.next_arrow_cal().click()
    wait.until(EC.element_to_be_clickable(MP.date_04_feb())).click()
    time.sleep(1)
    wait.until(EC.element_to_be_clickable(MP.search_but())).click()
    time.sleep(4)
    MP.driver.switch_to.window(MP.driver.window_handles[1])
    title = MP.driver.title
    assert title == "ATL to MIA - Cheap flights from ATL to MIA - Skiplagged"
    wait.until(EC.element_to_be_clickable(FP.select_cheap_flight())).click()
    time.sleep(2)
    FP.select_cheap_return().click()
    time.sleep(2)
    amount = FP.total_amt_of_trip().text
    print(amount)
    if int(amount.replace("$", "")) < 100:
        print("good deal")

def test_flight_book_paris(mainpage_instance):
    MP, FP =mainpage_instance
    MP.departure_airport().clear()
    MP.departure_airport().send_keys("ATL")
    time.sleep(1)
    MP.sug_atl().click()
    MP.arrival_airport().clear()
    MP.arrival_airport().send_keys("CDG")
    time.sleep(1)
    MP.sug_cdg_paris().click()
    time.sleep(1)
    MP.departure_calendar().click()
    time.sleep(1)
    MP.next_arrow_cal().click()
    MP.next_arrow_cal().click()
    MP.next_arrow_cal().click()
    MP.date_25_jan().click()
    MP.next_arrow_cal().click()
    MP.next_arrow_cal().click()
    MP.date_04_feb().click()
    time.sleep(1)
    MP.search_but().click()
    time.sleep(5)
    MP.driver.switch_to.window(MP.driver.window_handles[1])
    title = MP.driver.title
    assert title == "ATL to CDG - Cheap flights from ATL to CDG - Skiplagged"
    FP.select_cheap_flight().click()
    # time.sleep(4)
    FP.select_cheap_return().click()
    time.sleep(2)
    amount = FP.total_amt_of_trip().text
    print(amount)
    if int(amount.replace("$", "")) < 400:
        print("good deal")

def test_flight_book_honolulu(mainpage_instance):
    MP, FP =mainpage_instance
    MP.departure_airport().clear()
    MP.departure_airport().send_keys("ATL")
    time.sleep(1)
    MP.sug_atl().click()
    MP.arrival_airport().clear()
    MP.arrival_airport().send_keys("HNL")
    time.sleep(1)
    MP.sug_hnl_honolulu().click()
    time.sleep(1)
    MP.departure_calendar().click()
    time.sleep(1)
    MP.next_arrow_cal().click()
    MP.next_arrow_cal().click()
    MP.next_arrow_cal().click()
    MP.date_25_jan().click()
    MP.next_arrow_cal().click()
    MP.next_arrow_cal().click()
    MP.date_04_feb().click()
    time.sleep(1)
    MP.search_but().click()
    time.sleep(5)
    MP.driver.switch_to.window(MP.driver.window_handles[1])
    title = MP.driver.title
    assert title == "ATL to HNL - Cheap flights from ATL to HNL - Skiplagged"
    FP.select_cheap_flight().click()
    time.sleep(4)
    FP.select_cheap_return().click()
    time.sleep(2)
    amount = FP.total_amt_of_trip().text
    print(amount)
    if int(amount.replace("$", "")) < 400:
        print("good deal")

def test_flight_book_bogota(mainpage_instance):
    MP, FP =mainpage_instance
    MP.departure_airport().clear()
    MP.departure_airport().send_keys("ATL")
    time.sleep(1)
    MP.sug_atl().click()
    MP.arrival_airport().clear()
    MP.arrival_airport().send_keys("BOG")
    time.sleep(1)
    MP.sug_bog_bogota().click()
    time.sleep(1)
    MP.departure_calendar().click()
    time.sleep(1)
    MP.next_arrow_cal().click()
    MP.next_arrow_cal().click()
    MP.date_21_dec().click()
    MP.next_arrow_cal().click()
    MP.next_arrow_cal().click()
    MP.date_02_jan().click()
    time.sleep(1)
    MP.search_but().click()
    time.sleep(5)
    MP.driver.switch_to.window(MP.driver.window_handles[1])
    title = MP.driver.title
    assert title == "ATL to BOG - Cheap flights from ATL to BOG - Skiplagged"
    FP.select_cheap_flight().click()
    time.sleep(4)
    FP.select_cheap_return().click()
    time.sleep(2)
    amount = FP.total_amt_of_trip().text
    print(amount)
    if int(amount.replace("$", "").replace(",","")) < 400:
        print("good deal")
















#





