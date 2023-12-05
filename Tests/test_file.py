from selenium.webdriver.common.by import By
import time
from selenium import webdriver
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

from test_setup.webdriver_setup import se
from Pages.mainpage import Mainpage
from Pages.flightselection_page import Flight_selection
from Scripts import emailsend


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
def test_flights_paris(mainpage_instance):
    MP, FP = mainpage_instance

    number = 0
    while number != 10:
        MP, FP = mainpage_instance
        departure_city_list = ["MCO", "TPA", "ATL", "MIA", "JFK", "BNA", "CLT"]
        departure_day_list = ["21", "22", "23", "24", "25"]
        departure_city = random.choice(departure_city_list)
        arrival_city = "CDG"
        date_month_dep = "January"
        date_month_arrival = "February"
        date_day_dep = random.choice(departure_day_list)
        date_day_arrival = "2"

        MP.departure_airport().clear()
        MP.departure_airport().send_keys(departure_city)
        time.sleep(1)
        MP.sug_citya().click()
        MP.arrival_airport().clear()
        MP.arrival_airport().send_keys(arrival_city)
        time.sleep(1)
        MP.sug_cdg_paris().click()
        time.sleep(1)
        MP.departure_calendar().click()
        time.sleep(1)
        month = "a"
        ccc = 0
        while date_month_dep != month:
            month = MP.get_date_month().text
            MP.next_arrow_cal().click()
            ccc = ccc +1
            if ccc > 10:
                aaa = 0
                while aaa < 10:
                    MP.get_back_arrow_calendar().click()
                    aaa = aaa + 1
                    ccc = 0
        MP.get_dynamic_date(date_day_dep).click()
        month = "a"
        ccc = 0
        while date_month_arrival != month:
            month = MP.get_date_month().text
            MP.next_arrow_cal().click()
            ccc = ccc + 1
            if ccc > 10:
                aaa = 0
                while aaa < 10:
                    MP.get_back_arrow_calendar().click()
                    aaa = aaa + 1
                    ccc = 0
        MP.get_dynamic_date(date_day_arrival).click()
        time.sleep(3)
        MP.search_but().click()
        time.sleep(9)
        MP.driver.switch_to.window(MP.driver.window_handles[1])
        title = MP.driver.title
        assert title == f"{departure_city} to {arrival_city} - Cheap flights from {departure_city} to {arrival_city} - Skiplagged"
        FP.select_cheap_flight().click()
        time.sleep(6)
        FP.select_cheap_return().click()
        time.sleep(6)
        amount = FP.total_amt_of_trip().text
        print(f"{departure_city} + {amount}")
        emailsend.send_result(departure_city,arrival_city,amount, 300)
        MP.get_close_button().click()
        time.sleep(1)
        MP.logo().click()
        time.sleep(3)
        number = number + 1

def test_flights_from_ATL_to_South_America(mainpage_instance):
    MP, FP = mainpage_instance

    number = 0
    while number != 1:
        MP, FP = mainpage_instance
        departure_city_list = ["ATL"]
        departure_day_list = ["21", "22", "23", "24", "25"]
        arrival_city_list = {"BOG": "Bogota",  "MDE": "Medelin",  "CTG": "Cartagen", "PTY":"Panama", "UIO": "Quito" , "CLO": "Cali"}
        # citys = arrival_city_list['MDE']
        random_key = random.choice(list(arrival_city_list.keys()))
        # print(random_key)
        # Get the corresponding value for the random key
        # random_value = arrival_city_list[random_key]

        # print(random_value)

        departure_city = random.choice(departure_city_list)
        arrival_city = random_key
        date_month_dep = "January"
        date_day_dep = random.choice(departure_day_list)

        MP.get_round_trip_button().click()
        MP.get_one_way_button().click()
        MP.departure_airport().clear()
        MP.departure_airport().send_keys(departure_city)
        time.sleep(1)
        MP.get_sug_citya_departure().click()
        MP.arrival_airport().clear()
        MP.arrival_airport().send_keys(arrival_city)
        time.sleep(1)
        MP.get_sug_city_arrival().click()
        time.sleep(1)
        MP.departure_calendar().click()
        time.sleep(1)
        month = "a"
        ccc = 0
        while date_month_dep != month:
            month = MP.get_date_month().text
            MP.next_arrow_cal().click()
            ccc = ccc + 1
            if ccc > 10:
                aaa = 0
                while aaa < 10:
                    MP.get_back_arrow_calendar().click()
                    aaa = aaa + 1
                    ccc = 0
        MP.get_dynamic_date(date_day_dep).click()

        time.sleep(3)
        MP.search_but().click()
        time.sleep(9)
        MP.driver.switch_to.window(MP.driver.window_handles[1])
        title = MP.driver.title
        assert title == f"{departure_city} to {arrival_city} - Cheap flights from {departure_city} to {arrival_city} - Skiplagged"
        FP.select_cheap_flight().click()
        time.sleep(6)

        amount = FP.total_amt_of_trip().text
        print(f" price from {departure_city} to {arrival_city}  {amount}")
        emailsend.send_result(departure_city, arrival_city, amount, 300)
        MP.get_close_button().click()
        time.sleep(1)
        MP.logo().click()
        time.sleep(3)
        number = number + 1

def test_flights_from_ATL_to_Europe(mainpage_instance):
    MP, FP = mainpage_instance
    number = 0
    while number != 1:
        MP, FP = mainpage_instance
        departure_city_list = ["ATL"]
        departure_day_list = ["21", "22", "23", "24", "25"]
        arrival_city_list = {"CDG": "Paris",  "MAD": "Madrid",  "AMS": "Amsterdam", "BRU":"Brussels", "NCE": "Nice" , "LGW": "London"}
        # citys = arrival_city_list['MDE']
        random_key = random.choice(list(arrival_city_list.keys()))
        # print(random_key)
        # Get the corresponding value for the random key
        # random_value = arrival_city_list[random_key]

        # print(random_value)

        departure_city = random.choice(departure_city_list)
        arrival_city = random_key
        date_month_dep = "January"
        date_day_dep = random.choice(departure_day_list)

        MP.get_round_trip_button().click()
        MP.get_one_way_button().click()
        MP.departure_airport().clear()
        MP.departure_airport().send_keys(departure_city)
        time.sleep(1)
        MP.get_sug_citya_departure().click()
        MP.arrival_airport().clear()
        MP.arrival_airport().send_keys(arrival_city)
        time.sleep(1)
        MP.get_sug_city_arrival().click()
        time.sleep(1)
        MP.departure_calendar().click()
        time.sleep(1)
        month = "a"
        ccc = 0
        while date_month_dep != month:
            month = MP.get_date_month().text
            MP.next_arrow_cal().click()
            ccc = ccc + 1
            if ccc > 10:
                aaa = 0
                while aaa < 10:
                    MP.get_back_arrow_calendar().click()
                    aaa = aaa + 1
                    ccc = 0
        MP.get_dynamic_date(date_day_dep).click()

        time.sleep(3)
        MP.search_but().click()
        time.sleep(9)
        MP.driver.switch_to.window(MP.driver.window_handles[1])
        title = MP.driver.title
        assert title == f"{departure_city} to {arrival_city} - Cheap flights from {departure_city} to {arrival_city} - Skiplagged"
        FP.select_cheap_flight().click()
        time.sleep(6)

        amount = FP.total_amt_of_trip().text
        print(f" price from {departure_city} to {arrival_city}  {amount}")
        emailsend.send_result(departure_city, arrival_city, amount, 300)
        MP.get_close_button().click()
        time.sleep(1)
        MP.logo().click()
        time.sleep(3)
        number = number + 1

def test_flights_from_ATL_to_Europe_roundtrip(mainpage_instance):
    MP, FP = mainpage_instance
    number = 0
    while number != 10:
        MP, FP = mainpage_instance
        departure_city_list = ["ATL"]
        departure_day_list = ["21", "22", "23", "24", "25"]
        arrival_city_list = {"CDG": "Paris",  "MAD": "Madrid",  "AMS": "Amsterdam", "BRU":"Brussels", "NCE": "Nice" , "LGW": "London"}
        arrival_day_list = ["3","4"]
        # citys = arrival_city_list['MDE']
        arrival_city = random.choice(list(arrival_city_list.keys()))

        departure_city = random.choice(departure_city_list)
        # arrival_city = random_key
        date_month_dep = "January"
        date_month_arr = "February"

        date_day_dep = random.choice(departure_day_list)
        date_day_arr = random.choice(arrival_day_list)


        MP.departure_airport().clear()
        MP.departure_airport().send_keys(departure_city)
        time.sleep(1)
        MP.get_sug_citya_departure().click()
        MP.arrival_airport().clear()
        MP.arrival_airport().send_keys(arrival_city)
        time.sleep(1)
        MP.get_sug_city_arrival().click()
        time.sleep(1)
        MP.departure_calendar().click()
        time.sleep(1)
        month = "a"
        ccc = 0
        while date_month_dep != month:
            month = MP.get_date_month().text
            MP.next_arrow_cal().click()
            ccc = ccc + 1
            if ccc > 10:
                aaa = 0
                while aaa < 12:
                    MP.get_back_arrow_calendar().click()
                    aaa = aaa + 1
                    ccc = 0
        MP.get_dynamic_date(date_day_dep).click()
        month = "a"
        ccc = 0
        while date_month_arr != month:
            month = MP.get_date_month().text
            MP.next_arrow_cal().click()
            ccc = ccc + 1
            if ccc > 10:
                aaa = 0
                while aaa < 10:
                    MP.get_back_arrow_calendar().click()
                    aaa = aaa + 1
                    ccc = 0

        MP.get_dynamic_date(date_day_arr).click()

        time.sleep(3)
        MP.search_but().click()
        time.sleep(9)
        MP.driver.switch_to.window(MP.driver.window_handles[1])
        title = MP.driver.title
        # assert title == f"{departure_city} to {arrival_city} - Cheap flights from {departure_city} to {arrival_city} - Skiplagged"
        FP.select_cheap_flight().click()
        time.sleep(8)
        FP.select_cheap_return().click()
        time.sleep(6)

        amount = FP.total_amt_of_trip().text
        print(f" price from {departure_city} to {arrival_city}  {amount}")
        emailsend.send_result(departure_city, arrival_city, amount, 300)
        MP.get_close_button().click()
        time.sleep(1)
        MP.logo().click()
        time.sleep(3)
        number = number + 1


def test_flights_from_Baltimor_to_Europe_roundtrip(mainpage_instance):
    MP, FP = mainpage_instance
    number = 0
    while number != 4:
        MP, FP = mainpage_instance
        departure_city_list = ["BWI"]
        departure_day_list = ["24", "25", "26"]
        arrival_city_list = {"CDG": "Paris",  "MAD": "Madrid",  "AMS": "Amsterdam", "BRU":"Brussels", "NCE": "Nice" , "LGW": "London"}
        arrival_day_list = ["3","4"]
        # citys = arrival_city_list['MDE']
        arrival_city = random.choice(list(arrival_city_list.keys()))
        print(arrival_city)

        departure_city = random.choice(departure_city_list)
        # arrival_city = random_key
        date_month_dep = "January"
        date_month_arr = "February"

        date_day_dep = random.choice(departure_day_list)
        date_day_arr = random.choice(arrival_day_list)


        MP.departure_airport().clear()
        MP.departure_airport().send_keys(departure_city)
        time.sleep(1)
        MP.get_sug_citya_departure().click()
        MP.arrival_airport().clear()
        MP.arrival_airport().send_keys(arrival_city)
        time.sleep(1)
        MP.get_arrival_sug_city_dynamic(arrival_city).click()
        time.sleep(1)
        MP.departure_calendar().click()
        time.sleep(1)
        month = "a"
        ccc = 0
        while date_month_dep != month:
            month = MP.get_date_month().text
            MP.next_arrow_cal().click()
            ccc = ccc + 1
            if ccc > 10:
                aaa = 0
                while aaa < 12:
                    MP.get_back_arrow_calendar().click()
                    aaa = aaa + 1
                    ccc = 0
        MP.get_dynamic_date(date_day_dep).click()
        month = "a"
        ccc = 0
        while date_month_arr != month:
            month = MP.get_date_month().text
            MP.next_arrow_cal().click()
            ccc = ccc + 1
            if ccc > 10:
                aaa = 0
                while aaa < 10:
                    MP.get_back_arrow_calendar().click()
                    aaa = aaa + 1
                    ccc = 0

        MP.get_dynamic_date(date_day_arr).click()

        time.sleep(3)
        MP.search_but().click()
        time.sleep(9)
        MP.driver.switch_to.window(MP.driver.window_handles[1])
        title = MP.driver.title
        # assert title == f"{departure_city} to {arrival_city} - Cheap flights from {departure_city} to {arrival_city} - Skiplagged"
        FP.select_cheap_flight().click()
        time.sleep(8)
        FP.select_cheap_return().click()
        time.sleep(6)

        amount = FP.total_amt_of_trip().text
        print(f" price from {departure_city} to {arrival_city}  {amount} on {date_day_dep} return {date_day_arr}")
        emailsend.send_result(departure_city, arrival_city, amount, 400)
        MP.get_close_button().click()
        time.sleep(1)
        MP.logo().click()
        time.sleep(3)
        number = number + 1
