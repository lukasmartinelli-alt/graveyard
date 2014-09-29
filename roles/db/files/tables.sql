CREATE TABLE domains (
    domain VARCHAR(128) NOT NULL,
    PRIMARY KEY (domain)
);
CREATE TABLE users (
    mail VARCHAR(255) NOT NULL,
    password VARCHAR(128) NOT NULL,
    domain VARCHAR(128) NOT NULL,
    PRIMARY KEY (mail),
    FOREIGN KEY (domain) REFERENCES domains(domain)
);
CREATE TABLE aliases (
    domain VARCHAR(128),
    source VARCHAR(255) NOT NULL,
    destination VARCHAR(255) NOT NULL,
    PRIMARY KEY (source, destination),
    FOREIGN KEY (domain) REFERENCES domains(domain)
);
