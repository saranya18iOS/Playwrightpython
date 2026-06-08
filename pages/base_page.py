class BasePage:

    def __init__(self, page):
        self.page = page
        self.frame = None

    # ---------- navigation ----------
    def navigate(self, url):
        self.page.goto(url)

    # ---------- normal actions ----------
    def click(self, locator):
        self.page.locator(locator).click()

    def fill(self, locator, value):
        self.page.locator(locator).fill(value)

    def get_text(self, locator):
        return self.page.locator(locator).text_content()

    # ---------- FRAME HANDLING ----------
    def switch_to_frame(self, frame_locator):
        self.frame = self.page.frame_locator(frame_locator)

    def frame_click(self, locator):
        self.frame.locator(locator).click()

    def frame_fill(self, locator, value):
        self.frame.locator(locator).fill(value)

    def switch_to_default(self):
        self.frame = None