def ads():
    return '//span[@class="bgProperties  overlayCrossIcon icon20"]'

def checkbox_filter(type):
    return f'//p[text()="Popular Filters"]//ancestor::div[@class="filtersOuter"]//p[normalize-space(text())="{type}"]'

def Flight_range_locator (type,str):
    
    return f'//*[text()="{type} → {str}"]//parent::p//following-sibling::div[@class="listingCardWrap"]//input'



def Book_Now_locator(type):
    # FOR BOOKNOW AS WELL AS CONTINUE BUTTON WITH SAME LOCATOR AND DIFFRENT TEXT
    return f'//button[text()="{type}"]'

def Secure_locator():
    return '//*[text()="No,"]//ancestor::label[@class="radioboxContainer "]//input'

def addadult_btn(type):
    return f'//*[text()="{type}"]'
def number_of_adult(type,str):
    return f'//span[text()="ADULT  {type}"]//ancestor::div[@class="adultList checked"]//following-sibling::div[@class="AdultFormWrapper collapse show"]//input[@placeholder="{str}"]'

def selectGenderOfAdults(number,index):
    return f'//span[text()="ADULT {number}"]//ancestor::div[@class="adultList checked"]//following-sibling::div[@class="AdultFormWrapper collapse show"]//descendant::label[@tabindex="{index}"]'
    
def gender():
    return '//label[@tabindex="0"]'
childgender='//*[text()="CHILD (2-12 Yrs)"]//ancestor::div[@id="wrapper_CHILD"]//div[@class="selectTab "]//label[@tabindex="0"]'
def addchildbtn(type):
    return f'//button[text()="{type}"]'

def number_of_child(type, str):
    return f'//span[text()="CHILD  {type}"]//ancestor::div[@class="adultList checked"]//following-sibling::div[@class="AdultFormWrapper collapse show"]//input[@placeholder="{str}"]'
def Mobilenumber_locator(type):
    return f'//input[@placeholder="{type}"]'

Select_state_locator='//input[@id="dt_state_gst_info"]//parent::div[@class="dropdownFieldWpr__inputWpr"]'
Select_state_scrollbar = '//li[@class="dropdownListWpr__liItem activeItem" and text()="Maharashtra"]'
check_box_for_billing ='//span[@class="checkboxWpr"]'
continuebtn_page_2='//button[text()="Continue"]'


Continuebtn_after_passanger_detail='//button[@class="button buttonPrimary buttonBig fontSize14" and text()="CONFIRM"]'
Skipbtn1='//span[@class="fontSize16 linkText" and text()="Skip Seat Selection"]'
Continuebtn_after_skip_1='//button[@class="lato-black button buttonPrimary extraPadBtn fontSize16 " and text()="Continue"]'
Skipbtn2='//span[@class="fontSize16 linkText" and text()="Skip Seat Selection"]'
Proceedbtn='//button[@class="lato-black button buttonPrimary extraPadBtn fontSize16" and text()="Proceed to pay"]'

def Details_Function():
    return '//span[@class="text_capitalize" and text()="Tanishk"]'

# def Totalprice_locator():
#     return '//span[text()="Total Amount"]//following-sibling::span'

# def Total_price_at_the_end():
#     return '//span[text()="Fare"]//following-sibling::span'