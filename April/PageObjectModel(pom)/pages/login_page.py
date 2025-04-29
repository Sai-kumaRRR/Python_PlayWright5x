# Page Locators
# Page Actions

class Login:

    def __init__(self,page):
        self.page = page

        # Page Locators

@property
def username_field(self):
    return self.page.wait_for_selector("#login-username", timeout=5000)

@property
def username_button(self):
    return self.page.wait_for_selector("#login-password")


@property
def submit_button(self):
    return self.page.wait_for_selector("#js-login-btn")


# Page Actions



def submit_login_form(self,user):
    self.username_field.fill(user["username"])
    self.password_field.fill(user["password"])
    self.submit_button.click()


def navigate(self):
    self.page.goto("https://app.vwo.com")

