import sys
from playwright.sync_api import sync_playwright

sys.path.append('//home//tanishkyadav//MAKEMYTRIP_FRAMEWORK')
from Pages.locators import landing_page_locators
import environment_page_details
from playwright.sync_api import expect, Page

# Launch the browser
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    def perform_login(page):
        # This is url Websiteurl comes from the enivroment_page_details.py files
        page.goto(environment_page_details.Websiteurl)
        expect(page).to_have_url('https://www.makemytrip.com/')

    # to click on roundtrip
    def RoundTripfunction(page, Roundtrip_locator):
        Round_var=page.locator(Roundtrip_locator)
        Round_var.click()
        expect(Round_var).to_be_visible()
        page.screenshot(path="screenshot.png")
        # expect(Round_var).to_be_checked()
    
    
        # click for from text bar
    def Click_from(page):
        click_froM= page.locator(landing_page_locators.From_and_to_city())
        click_froM.click()
        expect(click_froM).to_be_visible()



    # This Pune is simple function that take the fromcity from the enviroment file
    def Pune(page):
        travell_from =page.locator(landing_page_locators.city('From'))
        # to fill the city dynamically
        # Assertion
        expect(travell_from).to_be_visible()
        travell_from.fill(environment_page_details.fromcity)
        # Assertion here so that text filled should not be empty
        expect(travell_from).not_to_be_empty()
        page.wait_for_timeout(1000)
    # This Suugestion function always click on first suggestion that will appear in suggestion box after typing..
    def Suggestion_first(Page):
       suggstion_var = Page.locator(landing_page_locators.suggestion())
    #   Assertion for checking the suggestion box is appeared or not 
       expect(suggstion_var).to_be_visible()
       suggstion_var.click()
    # This ToCity function used to click on To means destination 
    def ToCity(page):
        page.locator(landing_page_locators.Tocity()).click()

    # Fill_city function will fill the name of the destination from the enviromentfiles thorugh the tocity variable
    def Fill_city(page):
        fill_city_var=page.locator(landing_page_locators.city('To'))
        # Assertion is here
        expect(fill_city_var).to_be_visible()
        fill_city_var.fill(environment_page_details.tocity)
        #  Assertion is here
        expect(fill_city_var).not_to_be_empty()
        page.wait_for_timeout(1000)
        page.locator(landing_page_locators.suggestion()).click()
        # page.wait_for_timeout(1000) click for from text bar
    def Click_from(page):
        page.locator(landing_page_locators.From_and_to_city()).click()
    # To open the bar so that we can select the number of adults and child dynamically
    def Travel_function(page):
        # clicked in Travell dopdown 
        page.locator(landing_page_locators.Travell_locator()).click()
        
    # Click on adult as well as child in
    def Adult_function(page):
        # number indicate the number of adults in the travelling journey
        adult_var = page.locator(landing_page_locators.Adults_locator(environment_page_details.type,environment_page_details.number))
        adult_var.click()
        expect(adult_var).to_be_visible()

        
        # number indicate the number of child in the travelling journey
        page.locator(landing_page_locators.Adults_locator(environment_page_details.children, environment_page_details.childnumber)).click()
    # Click to apply the procedure and this is button 
    def Apply_function(page):
        apply=page.locator(landing_page_locators.Apply())
        expect(apply).to_be_visible()
        apply.click()

    # Searchbtn click function
    def Search_function(page):
        # cick on search btn so that it can search the flights and show us the result 
        page.locator(landing_page_locators.Searchbtn()).click()























































# -----------------------------------end_page_2-------------------


    # def Fill_Details(page):
    #     page.locator(landing_page_locators.filladult("First & Middle Name")).fill(environment_page_details.Name_of_adult_first)
    #     page.locator(landing_page_locators.filladult("Last Name")).fill(environment_page_details.Last_Name_of_adult_first)
    #     page.locator(landing_page_locators.filladult("First & Middle Name")).fill(environment_page_details.Name_of_adult_second)
    #     page.locator(landing_page_locators.filladult("Last Name")).fill(environment_page_details.Last_Name_of_adult_second)
        

    # def Gender_function(page):
    #     page.locator(landing_page_locators.gender()).click()
    
        # page.locator(landicheck_box_stopng_page_locators.adult_detail(environment_page_details.childpassanger)).click()

    # def form_firstname_function(page):
    #     first_name = page.locator(landing_page_locators.Addingpassanger())
    #     first_name.fill("Tanishk")