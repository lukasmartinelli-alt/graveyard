Infrastructure Overview
=======================

The idea behind the architecture of Mailgenic is to start small and
scale out as soon as the need occurs.

Naming servers
--------------

We follow the guide specified in [this great article](http://mnx.io/blog/a-proper-server-naming-scheme/).

**Short summary:**

1. Pick a unique name for the server
2. Create a functional `CNAME` record and point it to the server name

**Example:**

In the initial phase we only have one server `norman.mailgenic.com`.
This server will forever keep this hostname and is secured with an SSL certificate.
Because the MTA and MDA are installed on this server,
we point `imap.mailgenic.com` and `smtp.mailgenic.com` to `norman.mailgenic.com`.
This will allow us to simply point `imap.mailgenic.com` to a dedicated server or a
load balancer in the future.

Because the MX record must not be pointed to a CNAME we directly create an A
record to the same IP.

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
In the initial setup we have everything on one single server `norman.mailgenic.com`.
We can  use UNIX sockets for LMTP communication between MTA and MDA.

<div style="width: 480px; height: 360px; margin: 10px; position: relative;"><iframe allowfullscreen frameborder="0" style="width:480px; height:360px" src="https://www.lucidchart.com/documents/embeddedchart/4b4350dd-48c4-4406-8c68-52f3a612de18"></iframe><a href="https://www.lucidchart.com/pages/examples/mind_mapping_software" style="margin: 0; padding: 0; border: none; display: inline-block; position: absolute; bottom: 5px; left: 5px;"><img alt="mind mapping software"title="Lucidchart online diagrams"style="width: 100px; height: 30px; margin: 0; padding: 0; border-image: none; border: none; display: block"src="https://www.lucidchart.com/img/diagrams-lucidchart.png"/></a></div>
