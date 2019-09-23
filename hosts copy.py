import urllib.request

def main():
    WARUI_INTERNET_URL = "https://warui.intaa.net/adhosts/hosts_lb.txt"
    hosts = fetch_hosts(WARUI_INTERNET_URL)
    hosts += fetch_hosts("https://adaway.org/hosts.txt")
    hosts += fetch_hosts("http://winhelp2002.mvps.org/hosts.txt")
    hosts += fetch_hosts("https://pgl.yoyo.org/adservers/serverlist.php?hostformat=hosts&showintro=1&minetype=plaintext")
    hosts += fetch_hosts("https://mao2009.github.io/maos_adblock_hosts/hosts.txt")

    hosts = set(hosts)

    with open("test.txt", "w",encoding="utf-8") as fp:
        fp.write("#mao's adblock hosts")
        fp.write("127.0.0.1  locahost")
        fp.write("::1  localhost")
        for line in hosts:
            fp.write(line)
    
def fetch_hosts(hosts_url):
    print(hosts_url)
    hosts = []
    try:
        with urllib.request.urlopen(hosts_url) as res:
            for line in res.readlines():
                host =str(line,"utf-8")
                host = host.replace("0.0.0.0", "127.0.0.1")
                if host.startswith("#") or "localhost" in host:
                    continue
                hosts += [host]
    except urllib.error.HTTPError:
        print("ダウンロードできませんでした")
        return []
    return hosts

if __name__ == "__main__":
    main()