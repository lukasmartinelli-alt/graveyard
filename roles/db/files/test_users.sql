INSERT INTO domains (domain)
VALUES ('lukasmartinelli.ch'), ('mailgenic.com');

-- Password is "test"
INSERT INTO users (mail, domain, password)
VALUES ('me@lukasmartinelli.ch', 'lukasmartinelli.ch', '$6$t8yoaEQ1chO2MLoV$.yq6VeDhVWp5cUZk3sif.eQq9/suh504zlHnbb0B5ic/4c6QCwyqqQovyP4Ipe1oBpRgGA09m1bGfrwjgOEsL0'),
('admin@mailgenic.com', 'mailgenic.com', '$6$t8yoaEQ1chO2MLoV$.yq6VeDhVWp5cUZk3sif.eQq9/suh504zlHnbb0B5ic/4c6QCwyqqQovyP4Ipe1oBpRgGA09m1bGfrwjgOEsL0');
