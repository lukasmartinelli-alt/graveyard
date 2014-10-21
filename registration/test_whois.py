from .whois import check_domain_availability
import pytest

@pytest.mark.integration
def test_check_domain_works_for_ch():
    free_domains = ["frischiwürscht.ch", "frischesfleisch.ch"]
    reserved_domains = ["manuelroth.ch", "lukasmartinelli.ch", "mailgenic.ch"]

    for domain in free_domains:
        assert check_domain_availability(domain)

    for domain in reserved_domains:
        assert not check_domain_availability(domain)

@pytest.mark.integration
def test_check_domain_works_for_com():
    free_domains = ["mailgenic.com", "lukasmartinelli.com"]
    reserved_domains = ["fastmail.com", "google.com", "mailgenic.com"]

    for domain in free_domains:
        assert check_domain_availability(domain)

    for domain in reserved_domains:
        assert not check_domain_availability(domain)
