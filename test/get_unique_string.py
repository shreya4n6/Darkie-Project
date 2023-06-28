import uuid

def getUniqueString():
    """
    Returns a unique string
    """
    return str(uuid.uuid1())

us = getUniqueString()
print(us)