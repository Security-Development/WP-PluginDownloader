from utils.LogHandler import LogHandler
import requests
from bs4 import BeautifulSoup

# use utils
LogHandler = LogHandler()

class CrawlerTool:
    def __init__(self):
        self.url = None
        self.id = None
        self.pw = None

    def set_url(self, url):
        self.url = url
    
    def set_id(self, id):
        self.id = id

    def set_pw(self, pw):
        self.pw = pw

    def get_url(self):
        return self.url
    
    def get_id(self):
        return self.id

    def get_pw(self):
        return self.pw

    def init_check(self):
        return not (None in [self.url, self.id, self.pw])

    def login_data(self):
        return {
            "log": self.get_id(),
            "pwd": self.get_pw(),
            "wp-submit": "Log In",
            "redirect_to": "{0}/wp-admin/".format(self.get_url()),
            "testcookie": "1"
        }
    
    def dump_all_plugin(self):
        LogHandler.call_msg("All plugin name parsing...")
        
        plugins = []

        # 나중에 병렬 처리 할 예정
        if not self.init_check():
            LogHandler.error_msg("Make sure you have entered or entered the information correctly in WP-Info")
        
        with requests.Session() as session:
            res = session.post("{0}/wp-login.php".format(self.get_url()), data=self.login_data())
            
            if "wp-admin" in res.url:
                print("login 성공")
            else:
                print("login 실패")

        req = requests.get("{0}/wp-admin/plugin-install.php?tab=popular&paged={1}".format(self.get_url(), 0))
        soup = BeautifulSoup(req.text, "html.parser")

        max_page = soup.find(class_="total-pages").text
        element = soup.find_all(class_="plugin-card")

        LogHandler.info_msg("Full Page - {0}".format(max_page))
        LogHandler.info_msg("Current Page - {0}".format(max_page))
        LogHandler.info_msg("Number of plugins in the current page - {0}".format(len(element)))
        
        for div in element:
            plugins.append(div.get('class')[1][12:])
        
        LogHandler.info_msg("Finished analyzing. Let's start installing {0} plugin.".format(len(plugins)))

        return plugins
    
    def download(self, plugin):
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36",
            "Connection": "close"
        }

        req = requests.get("https://downloads.wordpress.org/plugin/"+plugin+".zip")
        print("[*] {0} The plugin has been downloaded.".format(plugin))


