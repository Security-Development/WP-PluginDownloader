from utils.JsonTool import JsonTool
from utils.CrawlerTool import CrawlerTool
import concurrent.futures

# use utils
JsonTool = JsonTool()
CrawlerTool = CrawlerTool()

def init_setting(url, id, pw):
    CrawlerTool.set_url(url)
    CrawlerTool.set_id(id)
    CrawlerTool.set_pw(pw)

def main():
    print("[- - - - - - - - - - - - - - - - - - - - - ]")
    print("|  #WP-PluginDownloader   @sylee and @LJX  |")
    print("[- - - - - - - - - - - - - - - - - - - - - ]")

    wp_info = JsonTool.dump("WP-Info.json")
    init_setting(wp_info['url'], wp_info['id'], wp_info['pw'])

    plugins = CrawlerTool.dump_all_plugin()
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        results = [executor.submit(CrawlerTool.download, plugin) for plugin in plugins]

        for _ in concurrent.futures.as_completed(results):
            pass

if __name__ == "__main__":
    main()