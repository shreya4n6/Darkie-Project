import os
import subprocess as subp
import requests
import json

proxies = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

def getOnionUrlData(onionUrl):
    # data = requests.get("http://altaddresswcxlld.onion",proxies=proxies).text
    data = requests.get(onionUrl,proxies=proxies).text

    print(data)

def checkServiceStatus():
    """
    Checks if the Tor service is running
    """
    print('\n' + 
          "[>] Checking for tor service ..." + '\n')
    cmd = 'systemctl is-active tor.service'
    co = subp.Popen(cmd, shell=True, stdout=subp.PIPE).communicate()[0]
    if 'inactive' in str(co):
        print('[!] Tor Service Not Running..' + '\n')
        print('[>] Tor Service is Required for this Script...')
        print('[>] Turning on Tor Service...')
        print('\n')
        cmd = 'sudo service tor start '
        os.system(cmd)

    else:
        print("[>] Tor Service is Running..." + '\n')


onionUrl1 = "http://rankspeslx4jwbalykpdrn4zsdfuqq25wiioy3ibvjlbgshfph7jtqad.onion"
onionUrl2 = "http://tape6m4x7swc7lwx2n2wtyccu4lt2qyahgwinx563gqfzeedn5nb4gid.onion/credentials-belonging-to-tokyo-olympics-ticket-buyers-posted-on-the-dark-web"
onionUrl3 = "http://hackltxlmapssd5u6wro4ms7cn3tjbtyij5iuhfgaoxjmpwcc224ibyd.onion"

checkServiceStatus()
getOnionUrlData(onionUrl1)