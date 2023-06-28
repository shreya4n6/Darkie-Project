from modules import statics
import uuid

def showBanner():
    """
    Show the 'Darkie' banner
    """
    banner = fr'''{statics.G}
     _____               __ _    __   _
    |  _  \      /\      ||  \   ||  //         _____
    | | | |     //\\     ||__/   || //   _o_   /_____\
    {statics.R}| | | /    //  \\    ||\\    |||     | |  //_____/
    | |/ /    //____\\   || \\   || \\   | |  \______
    {statics.C}|___/    //      \\  ||  \\  ||  \\  |_|   \_____|

    {statics.R}Developer: {statics.C}Shreya T
    {statics.R}Version: {statics.C}{statics.VERSION}
    
    '''

    print(banner)


def isOnionUrl(url):
    """
    Check whether given url is an onion url or not
    """
    if statics.ONION in url:
        return True

    return False


def getUniqueString():
    """
    Returns a unique string
    """
    return str(uuid.uuid1())