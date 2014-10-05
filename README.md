Infrastructure Overview
=======================

The idea behind the architecture of Mailgenic is to start small and
scale out as soon as the need occurs.

Developer Environment
---------------------
Vagrant is used to create virtual machines for development and testing deployment.

Start a machine with all the infrastructure
```
vagrant up
```

Now connect to the machine, source the Python virtualenv and start the web interface
```
vagrant ssh
source /var/venv/mailgenic/activate
cd /srv/www/mailgenic
python manage.py runserver 0.0.0.0:8000
```

Naming servers
--------------

We follow the guide specified in [this great article](http://mnx.io/blog/a-proper-server-naming-scheme/).

**Short summary:**

1. Pick a unique name for the server
2. Create a functional `CNAME` record and point it to the server name

**Problems**

Because all SMTP servers need a reverse PTR record to get through spam.
We will ignore this rule for one time and name our first server `smtp.mailgenic.com`.
For `imap.mailgenic.com` and `webmail.mailgenic.com` web we point a CNAME to `smtp.mailgenic.com`.

Abbreviations
-------------

**MTA**: Mail Transport Agent is responsible for sending and receiving
all mail (also called mail relay). If a MUA sends an email it will use SMTP
to connect to the **MTA** which will then delivery the mail to other **MTAs**.

**MDA**: Mail Delivery Agent is responsible for storing and receiving mail
for the user. The **MTA** will send the received messages to the **MDA** via
LMTP. The **MDA** will store the mails and make them accessible to **MUAs**
via IMAP.

**MUA**: Mail User Agent can be a webmail or any other mail client.

Connection Information
----------------------

**Incoming (IMAP)**

Server             | imap.mailgenic.com
Port               | 993
SSL/TLS Encryption | Enabled, but not STARTTLS
Username           | Your personal email
Password           | Your password

**Outgoing (SMTP)**

Server             | smtp.mailgenic.com
Port               | 465
SSL/TLS Encryption | Enabled, but not STARTTLS
Username           | Your personal email
Password           | Your password

Quick Security Considerations
-----------------------------
- Secure each server with an SSL certificate
- Only allow necessary ports
- Choose best security for the user on cost of configurability
  - Don't allow POP3
  - Only allow TLS/SSL encryption (no plaintext mail)

Initial setup
-------------
In the initial setup we have everything on one single server `smtp.mailgenic.com`.
We can  use UNIX sockets for LMTP communication between MTA and MDA.

![Initial deployment](https://www.lucidchart.com/publicSegments/view/542d665a-95bc-4a9c-bbd0-01720a005489/image.png)
