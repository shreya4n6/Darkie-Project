import os
import subprocess as subp
from modules import statics
from modules.search import session

def connectTor():
    r = session.get("http://icanhazip.com").text
    print(statics.R + '[+]' + statics.G  + ' Connected to Tor...' + statics.W)
    print(statics.R + '[+]' + statics.G  + ' Your Tor IP -> {}'.format(r) + statics.W)


def checkServiceStatus():
    """
    Checks if the Tor service is running
    """
    print('\n' + statics.C +
          "[>] Checking for tor service ..." + statics.W + '\n')
    cmd = 'systemctl is-active tor.service'
    co = subp.Popen(cmd, shell=True, stdout=subp.PIPE).communicate()[0]
    if 'inactive' in str(co):
        print(statics.R + '[!] Tor Service Not Running..' + statics.W + '\n')
        print(statics.R + '[>] Tor Service is Required for this Script...')
        print(statics.R + '[>] Turning on Tor Service...')
        print(statics.W + '\n')
        cmd = 'sudo service tor start '
        os.system(cmd)

    else:
        print(statics.C + "[>] Tor Service is Running..." + statics.W + '\n')