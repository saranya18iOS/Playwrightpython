from pages.base_page import BasePage
from test_data.ui.form_data import DemoQAFormData as data


class DemoQAFormPage(BasePage):

    FIRST_NAME = "#firstName"
    LAST_NAME = "#lastName"
    EMAIL = "#userEmail"
    GENDER_MALE = "label[for='gender-radio-1']"
    MOBILE = "#userNumber"
    DOB = "#dateOfBirthInput"
    YEAR = ".react-datepicker__year-select"
    MONTH = ".react-datepicker__month-select"
    DAY = ".react-datepicker__day--015:not(.react-datepicker__day--outside-month)"
    SUBJECT = "#subjectsInput"
    HOBBY_SPORTS = "label[for='hobbies-checkbox-1']"
    ADDRESS = "#currentAddress"
    STATE = "#state"
    CITY = "#city"
    SUBMIT = "#submit"
    SUCCESS_MSG = "#example-modal-sizes-title-lg"
    ALERT_BUTTON = "#alertButton"

    def fill_form(self):

        self.fill(self.FIRST_NAME, data.FIRST_NAME)
        self.fill(self.LAST_NAME, data.LAST_NAME)
        self.fill(self.EMAIL, data.EMAIL)

        self.click(self.GENDER_MALE)

        self.fill(self.MOBILE, data.MOBILE)

        self.click(self.DOB)
        self.page.locator(self.YEAR).select_option(data.YEAR)
        self.page.locator(self.MONTH).select_option(data.MONTH)
        self.click(self.DAY)

        self.fill(self.SUBJECT, data.SUBJECT)
        self.page.keyboard.press("Enter")

        self.click(self.HOBBY_SPORTS)

        self.fill(self.ADDRESS, data.ADDRESS)

        self.click(self.STATE)
        self.page.get_by_text(data.STATE).click()

        self.click(self.CITY)
        self.page.get_by_text(data.CITY).click()

        self.page.locator(self.SUBMIT).scroll_into_view_if_needed()
        self.page.locator(self.SUBMIT).click(force=True)

    def verify_submission(self):
        return self.get_text(self.SUCCESS_MSG) == data.SUCCESS_MSG
    
    def handle_alert(self, action="accept", text=None):

        def handler(dialog):
            print(dialog.message())

            if action == "accept":
                dialog.accept(text) if text else dialog.accept()
            elif action == "dismiss":
                dialog.dismiss()

        self.page.once("dialog", handler)

    def trigger_alert(self):

        self.page.once("dialog", lambda dialog: dialog.accept())
        self.click(self.ALERT_BUTTON)     