from pythonwhois import get_whois
import requests

MASHAPE_KEY = "jOXU2vI0pRmshlgTGynBOs1jMX8lp1M9cYCjsnMASwXg2rg3jA"
MASHAPE_URL = "https://nametoolkit-name-toolkit.p.mashape.com/beta/whois/"

def check_domain_availability(domain):
    """
    Returns whether the domain available or not.
    The nametoolkit is used together with a local library to check
    concurrently whether the domain is available or not.
    """

    def check_local():
        """
        Use pythonwhois to check whether a domain has a registrant
        in the whois directory.
        """
        try:
            whois = get_whois(domain, normalized=True)
            return whois["contacts"]["registrant"] is None
        except ConnectionRefusedError:
            return False

    def check_extern():
        """
        Use the nametoolkit via Mashape to check if the domain is available
        """
        headers = {"X-Mashape-Key": MASHAPE_KEY}
        response = requests.get(MASHAPE_URL + domain, headers=headers)

        if response.status_code != requests.codes.ok:
            return False
        return response.json()["available"]

    return check_local() or check_extern()


