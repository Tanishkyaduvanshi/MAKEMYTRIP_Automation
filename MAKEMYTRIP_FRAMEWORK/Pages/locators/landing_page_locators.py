# Locators for login page elements
Roundtrip_locator= 'li[data-cy="roundTrip"]' 

def From_and_to_city():
    return  '//*[@class="flt_fsw_inputBox searchCity inactiveWidget "]' 

def city(type):
    return f'//input[@placeholder="{type}"]'

def suggestion():
    return '//li[@id="react-autowhatever-1-section-0-item-0"]'

def Tocity():
    return '//span[text()="To"]'
    # 

def Travell_locator():
    return '//*[text()="Travellers & Class"]'
def Adults_locator(type, number):
    return f'//*[@data-cy="{type}-{number}"]'

def Apply():
    return '//button[@data-cy="travellerApplyBtn"]'

def Searchbtn():
    return '//a[@class="primaryBtn font24 latoBold widgetSearchBtn "]'

