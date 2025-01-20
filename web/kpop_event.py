from components.env import Config
from components.driver_browser import Browser
from components.web_page import WebPage

urls = [
    'https://www.thebdm.co.kr/shop/shopbrand.html?xcode=003&type=N',
    'https://everlineshop.com/us/goods/event_sale_list.php?type=ing',
    'https://www.ktown4u.com/event?keyword=video+call',
    'https://www.ktown4u.com/event?keyword=sign',
    'https://en.sound-wave.co.kr/category/fan-event/406/',
    'https://hello82.com/en-int/collections/signed-albums?filter.v.availability=1&filter.v.price.gte=&filter.v.price.lte=&sort_by=created-descending',
    'https://kpopstoreinusa.com/search?options%5Bprefix%5D=last&options%5Bunavailable_products%5D=last&page=3&q=signed&type=product',
    'https://globalbunjang.com/search?q=signed%20mamamoo&soldout=exclude',
    'https://globalbunjang.com/search?q=signed%20twice&soldout=exclude',
    'https://www.allthatsales.com/signed-kpop-albums',
    'https://hallyusuperstore.com/search?q=signed&options%5Bprefix%5D=last&filter.v.availability=1',
    'https://www.makestar.co/projects/list/pre_order?status=&orderBy=10&viewMode=LIST',
    'https://store.frommyarti.com/en/product',
    'https://wonderwall.kr/en/search?q=video%20call',
    'https://www.musickorea.asia/Board/list/board_name/eventnotice',
    'http://ticket.yes24.com/Pages/English/Perf/FnPerfList.aspx?Genre=15456',
    'https://jumpupent.com/product/list.html?cate_no=48',
    'https://beatroad.co.kr/product/list.html?cate_no=150',
    'https://www.dmcmusic.co.kr/board/board.html?code=sincere123_board3',
    'https://dearmymuse.kr/category/fansign-etc/253/',
    'https://dailyduck.com/event',
    'https://www.applemusic.co.kr/board/board.html?code=applemusic_board2',
    'https://www.withmuu.com/us/goods/event_sale_list.php?type=ing'
]


class KpopEvents(WebPage, Browser, Config):
    def __init__(self):
        # Inicializa la clase base
        self.initialize_browser()
        self.load_environment_variables()
        WebPage.__init__(self, self.driver)

    def view_urls(self, urls):
        for url in urls:
            print(url)


events = KpopEvents()
events.view_urls(urls)
