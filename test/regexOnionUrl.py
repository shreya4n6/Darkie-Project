import re

s = '''hfajlhfjkdsflkdsja.onion
https://hfajlhfjkdsflkdsja.onion
http://www.hfajlhfjkdsflkdsja.onion
https://www.google.com
http://wbl3q5i7mbwdsbqo2outtnehadswp6zr7gpme5wn555xbyhatzmn2wqd.onion/big-dick-fuck-sissy/rise-sex.php
http://hiddenpuubpeeyiq3zmjshclbgvitpepde2wyyhkscgbb42zdzsfljyd.onion/game-store/msi-ge75-raider-645-17.3%22-gaming-laptop/reviews/page-4
http://rankspeslx4jwbalykpdrn4zsdfuqq25wiioy3ibvjlbgshfph7jtqad.onions
https://stackoverflow.com'''


for m in re.finditer(r'(?:https?://)?(?:www)?(\S*?\.onion)\b', s, re.M | re.IGNORECASE):
    print(m.group(0))