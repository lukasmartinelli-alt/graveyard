from pythonwhois import get_whois

def check_domain_availability(domain):
    """Returns whether the domain is already reserved or not"""
    whois = get_whois(domain, normalized=True)
#    import ipdb; ipdb.set_trace()
    return whois["contacts"]["registrant"] is None
