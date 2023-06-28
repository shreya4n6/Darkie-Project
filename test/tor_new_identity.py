#from stem import Signal
#from stem.control import Controller

#with Controller.from_port(port=9051) as controller:
  # Authenticating to our controller with the password
  # we used when we used the 'tor --hash-password' command
  #controller.authenticate(password='16:BD4F250C75B8C0DE60B956D60DF481B304A9FD38CB4B960838EF03963C')
  # Send signal to Tor controller to create new identity
  # (a new exit node IP)
  #controller.signal(Signal.NEWNYM)
from stem import Signal
from stem.control import Controller

with Controller.from_port(port=9051) as controller:
  # Authenticating to our controller with the password
  # we used when we used the 'tor --hash-password' command
  controller.authenticate(password="Forensics")
  # Send signal to Tor controller to create new identity
  # (a new exit node IP)
  controller.signal(Signal.NEWNYM)
