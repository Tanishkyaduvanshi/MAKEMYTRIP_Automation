import sys
from playwright.sync_api import sync_playwright

sys.path.append('//home//tanishkyadav//MAKEMYTRIP_FRAMEWORK')
from Pages.locators import select_flights_page_locators
import environment_page_details
from playwright.sync_api import expect, Page

# Launch the browser
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    def Ads(page):
        page.locator(select_flights_page_locators.ads()).click()

    def Checkbox_filter(page):
        checkbox_var = page.locator(select_flights_page_locators.checkbox_filter(environment_page_details.flight_name))
        expect(checkbox_var).not_to_be_checked()
        checkbox_var.check()
        expect(checkbox_var).to_be_checked()
        check_box_stop = page.locator(select_flights_page_locators.checkbox_filter(environment_page_details.stop))
        # Assertion so that the checkbox is not already checked
        expect(check_box_stop).not_to_be_checked()
        check_box_stop.check()
        # Assertion for checking the check box is check to not 
        expect(check_box_stop).to_be_checked()

    def Flight_Range_function(page):
        
        page.locator(select_flights_page_locators.Flight_range_locator(environment_page_details.fromcity,environment_page_details.tocity)).nth(2).click()
        page.locator(select_flights_page_locators.Flight_range_locator(environment_page_details.tocity,environment_page_details.fromcity)).nth(1).click()

        
    def Book_NOW_function(page):
        page.locator(select_flights_page_locators.Book_Now_locator("Book Now")).click()
        page.locator(select_flights_page_locators.Book_Now_locator("CONTINUE")).click()
        page.locator(select_flights_page_locators.Book_Now_locator("BOOK NOW")).click()

    def Secure_function(page):
        page.locator(select_flights_page_locators.Secure_locator()).click()
    def Number_of_adults_function(page):
        for i in range(0,environment_page_details.adult_number):
             page.locator(select_flights_page_locators.addadult_btn(environment_page_details.adultpassanger)).click()
             page.locator(select_flights_page_locators.number_of_adult(i+1,"First & Middle Name")).fill(environment_page_details.adultslist[i]["FirstName"])
             page.locator(select_flights_page_locators.number_of_adult(i+1,"Last Name")).fill(environment_page_details.adultslist[i]["LastName"])
             
             page.locator(select_flights_page_locators.gender()).click()
            #  page.locator(select_flights_page_locators.selectGenderOfAdults(i+1,environment_page_details.adultslist[i]["Gender"])).click()
             
            #  page.locator(select_flights_page_locators.CountrY(environment_page_details.adultslist["CountryCode"])).click()
            #  page.locator(select_flights_page_locators.CountrY(environment_page_details.adultslist["CountryCode"])).click()
            #  page.locator(select_flights_page_locators.CountrY(environment_page_details.adultslist[i]["CountryCode"])).click()
            #  page.keyboard.press("Enter")
    def Number_of_Child_function(page):
        for i in range(0,environment_page_details.child_number):
            page.locator(select_flights_page_locators.addadult_btn(environment_page_details.childpassanger)).click()
            page.locator(select_flights_page_locators.number_of_child(i+1,"First & Middle Name")).fill(environment_page_details.childlist[i]["FirstChild_Name"])
            page.locator(select_flights_page_locators.number_of_child(i+1,"Last Name")).fill(environment_page_details.childlist[i]["Child_Surname"])
            page.locator(select_flights_page_locators.childgender).click()
            


    def Mobile_number_function(page):
        page.locator(select_flights_page_locators.Mobilenumber_locator("Mobile No")).fill(environment_page_details.Mobile_number)
        page.locator(select_flights_page_locators.Mobilenumber_locator("Email")).fill(environment_page_details.Email)

    def State_function(page):
        page.locator(select_flights_page_locators.Select_state_locator).click()
        page.locator(select_flights_page_locators.Select_state_scrollbar).click()
        page.locator(select_flights_page_locators.check_box_for_billing).click()

        page.locator(select_flights_page_locators.continuebtn_page_2).click()

        page.locator(select_flights_page_locators.Continuebtn_after_passanger_detail).click()

        page.locator(select_flights_page_locators.Skipbtn1).click()

        page.locator(select_flights_page_locators.Continuebtn_after_skip_1).click()

        page.locator(select_flights_page_locators.Skipbtn2).click()

        page.locator(select_flights_page_locators.Continuebtn_after_skip_1).click()


        page.locator(select_flights_page_locators.Continuebtn_after_skip_1).click()
        page.locator(select_flights_page_locators.Continuebtn_after_skip_1).click()
        # page.locator(select_flights_page_locators.Continuebtn_after_skip_1).click()

        page.locator(select_flights_page_locators.Proceedbtn).click()
    def getprice(page):
        return page.locator(select_flights_page_locators.price).inner_text()






    def passangerdetail_confirmation_function(page):
        Travelerdetail = page.locator(select_flights_page_locators.Details_Function())
        # Assertion for the passanger detail
        expect(Travelerdetail).to_contain_text(environment_page_details.adultslist["FirstName"])


    # def Totalprice_function(page):
    #     price1=page.locator(select_flights_page_locators.Totalprice_locator)
    #     price2=page.locator(select_flights_page_locators.Total_price_at_the_end)
    #     price2.to_contain_text(price1)

    # def verifyPrice(page,price):
    #     assert (page.locator(select_flights_page_locators).inner_text() in price)

    