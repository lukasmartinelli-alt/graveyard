Infrastructure Overview
=======================

The idea behind the architecture of Mailgenic is to start small and
scale out as soon as the need occurs.

To do this we create **realms**. A **realm** contains everything needed
for sending, receiving and storing mail.
A **realm** consists of:
- 1..2 SMTP Server (MTA)
- 1..2 Proxy IMAP Server (MDA proxy)
- 2..N IMAP Server (MDA)
- 2..N Webmail Server (MUA)

The idea behind this is, that the first bottleneck is the MTA.
We can only send and receive as much mail as the MTA can chew through.
To provide redundancy we perhaps need more than one MTA.

The storage approach is that a user is associated with one specifig MDA
which stores the user data located.

Ideally one MDA contains max. 1000 users with an estimated usage of 1GB per user.
To do distribute the users across MDAs we need MDA proxies.

Initial setup
-------------

The initial setup should be very small and all fit on one single box.
We use Docker containers to keep the environment portable and easy
to distribute.

- 1 MTA
- 1 MDA Proxy
- 1 MDA
- 1 Webmail Server

This means we need following containers:

- 1 Postfix
- 1 Dovecot Proxy
- 1 Dovecot Maildir
- 1 Mailpile
- 1 Postgres

And of course a user database.

