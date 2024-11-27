from selene import browser, be, have, by
import os

firstName = 'Ivan'
lastName = 'Ivanov'
userEmail = 'test@test.com'
userNumber = '1111111111'

month = 'June'
year = '2000'
day = '01'

genter = 'Female'
hobbies = 'Reading'

images = 'butterflies.png'
currentAddress = 'Russia'
subjects = 'biology'

state = "Uttar Pradesh"
city = "Merrut"


def test_type_registration_form(browser_settings):
    browser.open('/automation-practice-form')
    browser.element('#firstName').should(be.blank).type(firstName)
    browser.element('#lastName').should(be.blank).type(lastName)
    browser.element('#userEmail').should(be.blank).type(userEmail)
    browser.element('#userNumber').should(be.blank).type(userNumber)
    browser.element('#dateOfBirthInput').click()
    browser.element("[class='react-datepicker__month-select']").click().element(by.text(month)).click()
    browser.element("[class='react-datepicker__year-select']").click().element(by.text(year)).click()
    browser.element(f"[class ='react-datepicker__day react-datepicker__day--0{day}']").click()
    # browser.element('[for="gender-radio-2"]').click()
    browser.element('#genterWrapper').element(by.text(genter)).click()
    # browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('#hobbiesWrapper').element(by.text(hobbies)).click()
    browser.element("#uploadPicture").send_keys(os.path.abspath(f"../images/{images}"))
    browser.element('#currentAddress').should(be.blank).type(currentAddress)
    browser.element('#subjectsInput').should(be.blank).type(subjects)
    browser.element('#state').click().element(by.text(state)).click()
    browser.element('#city').click().element(by.text(city)).click()

    browser.element('#submit').click()

    browser.element(("[class='table-responsive']")).should(have.text(f'{firstName} {lastName}'))
    browser.element(("[class='table-responsive']")).should(have.text(userEmail))
    browser.element(("[class='table-responsive']")).should(have.text(genter))
    browser.element(("[class='table-responsive']")).should(have.text(userNumber))
    browser.element(("[class='table-responsive']")).should(have.text(f'{day} {month},{year}'))
    # browser.element(("[class='table-responsive']")).should(have.text(subjects))
    browser.element(("[class='table-responsive']")).should(have.text(hobbies))
    browser.element(("[class='table-responsive']")).should(have.text(images))
    browser.element(("[class='table-responsive']")).should(have.text(currentAddress))
    browser.element(("[class='table-responsive']")).should(have.text(f'{state} {city}'))
