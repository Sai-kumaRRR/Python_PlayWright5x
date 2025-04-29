class Dashboard:

    def __init__self(self,page):
        self.page = page


        def get_logged_in_username(self):
            self.page.wait_for_load_state("networkidle")
            return self.page.locator("[data-qa='page-heading']").text_content()