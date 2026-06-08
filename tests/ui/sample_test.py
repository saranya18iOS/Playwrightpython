from pages.forms_page import DemoQAFormPage

def test_demoqa_click(page):
    page.goto("https://demoqa.com")
    page.get_by_text("Elements").click()


def test_demoqa_formfilling(page):
    form = DemoQAFormPage(page)

    form.navigate("https://demoqa.com/automation-practice-form")

    form.fill_form()
    assert form.verify_submission()

def test_demoqa_alerthandling(page):
    form = DemoQAFormPage(page)

    form.navigate("https://demoqa.com/alerts")

    form.handle_alert()
    form.trigger_alert()
    



