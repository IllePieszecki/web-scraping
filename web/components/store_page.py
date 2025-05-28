from .web_page import WebPage

class Stores(WebPage):
    def mercari(self, element: str):
        self.scroll_to_element(self.find(element))

    def yahoo(self):
        pass

    def jyp(self):
        pass

    def flea_market(self):
        pass
