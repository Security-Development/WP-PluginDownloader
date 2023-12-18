from utils.JsonTool import JsonTool
from utils.CrawlerTool import CrawlerTool
import concurrent.futures
import os

# use utils
JsonTool = JsonTool()
CrawlerTool = CrawlerTool()

        
def init_setting(url, id, pw):
    CrawlerTool.set_url(url)
    CrawlerTool.set_id(id)
    CrawlerTool.set_pw(pw)
    
    if not os.path.exists("./plugin-list"):
        os.makedirs("./plugin-list")

def main():
    print("[- - - - - - - - - - - - - - - - - - - - - ]")
    print("|  #WP-PluginDownloader   @sylee and @LJX  |")
    print("[- - - - - - - - - - - - - - - - - - - - - ]")

    wp_info = JsonTool.dump("WP-Info.json")
    wp_info['url'] = wp_info['url'].replace("https:"," http:")
    
    init_setting(wp_info['url'], wp_info['id'], wp_info['pw'])
    
    print("[*] url : {0}".format(wp_info['url']))
    print("[*] id : {0}".format(wp_info['id']))
    print("[*] pw : {0}".format(wp_info['pw']))
    
    # 나중에 페이지 먼저 구해오도록 할 예정
    for page in range(1, 10240):
        path = "./plugin-list/{0}".format(page)
        
        if not os.path.exists(path):
            os.makedirs(path)
            
        plugins = CrawlerTool.dump_plugin(page)
        
        if plugins == 0xdeadbeaf:
        	break
    
        with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
            results = [executor.submit(CrawlerTool.download, page, plugin) for plugin in plugins if not os.path.exists("./plugin-list/{0}/{1}".format(page, plugin))]

            for _ in concurrent.futures.as_completed(results):
                pass


if __name__ == "__main__":
    main()
