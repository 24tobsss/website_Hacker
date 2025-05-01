from stem import Signal
from stem.control import Controller
import requests

def rotate_tor_ip():
    try:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate(password="hack5")
            controller.signal(Signal.NEWNYM)
            print("[✓] Tor-IP rotiert!")
    except Exception as e:
        print(f"[!] Tor-Fehler: {e}")

def make_anonymous_request(url):
    session = requests.session()
    session.proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }
    return session.get(url)
