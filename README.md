Infrastructure Overview
=======================

The idea behind the architecture of Mailgenic is to start small and
scale out as soon as the need occurs.

Every user is associated with one specific MDA which stores the user data.

One MDA contains max 1000 users with an estimated usage of 1GB per user.
To do distribute the users across MDAs we need MDA proxies.

Initial setup
-------------

- 1 MTA
- 1 MDA
- 1 UserDB

