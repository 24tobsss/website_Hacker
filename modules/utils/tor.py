# modules/utils/tor.py
from stem import Signal
from stem.control import Controller

def rotate_ip():
    with Controller.from_port(port=9051) as c:
        c.authenticate(password="hack5")
        c.signal(Signal.NEWNYM)
