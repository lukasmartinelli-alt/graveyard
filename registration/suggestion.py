from .whois import check_domain_availability


def suggest_domains(initial_domain):
    domain, tld = initial_domain
    tlds = ["li", "ch", "com", "de"]

    for tld in tlds:
        full_domain = domain + "." + tld
        yield {"domain": domain,
               "tld": tld,
               "available": check_domain_availability(full_domain)}

    yield {"domain": domain[:-2],
           "tld": domain[-2:],
           "available": check_domain_availability(domain[:-2] + "." + domain[-2:])}
