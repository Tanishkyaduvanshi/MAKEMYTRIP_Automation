import sys
sys.path.append('/home/tanishkyadav/MAKEMYTRIP_FRAMEWORK')
from playwright.sync_api import sync_playwright
from Pages.locators.landing_page_locators import Roundtrip_locator
from Pages.functions import landing_page_function

from Pages.functions import select_flights_page_function


def test_main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context=browser.new_context(record_video_dir="videos/")
        page = context.new_page()


        landing_page_function.perform_login(page)
        # it make click on Round trip option
        landing_page_function.RoundTripfunction(page, Roundtrip_locator)

        # make click on 
        landing_page_function.Click_from(page)
        landing_page_function.Pune(page)
        page.wait_for_timeout(1000)
        landing_page_function.Suggestion_first(page)
        landing_page_function.ToCity(page)
        landing_page_function.Fill_city(page)
        
        landing_page_function.Travel_function(page)
        
        landing_page_function.Adult_function(page)
        
        landing_page_function.Apply_function(page)
        landing_page_function.Search_function(page)

        page.wait_for_timeout(11000)
    
        select_flights_page_function.Ads(page)
        select_flights_page_function.Checkbox_filter(page)
        
        select_flights_page_function.Flight_Range_function(page)
        select_flights_page_function.Book_NOW_function(page)

        page.wait_for_timeout(1000)
        Total_page=context.pages
        new_page=Total_page[1]
        print(len(Total_page))
        new_page.bring_to_front()


        select_flights_page_function.Secure_function(new_page)
        new_page.wait_for_timeout(1000*5)
# page.pause()
        select_flights_page_function.Number_of_adults_function(new_page)

        select_flights_page_function.Number_of_Child_function(new_page)
# page.pause()

        select_flights_page_function.Mobile_number_function(new_page)


        select_flights_page_function.State_function(new_page)
        select_flights_page_function.passangerdetail_confirmation_function(new_page)
        # price=select_flights_page_function.getprice()
        # select_flights_page_function.verifyprice(new_page,price)


        page.wait_for_timeout(3000)

if __name__=="__main__":
    test_main()