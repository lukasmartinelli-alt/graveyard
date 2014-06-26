Remote Procedure Call
=====================
Es gibt zwei Designdimensionen:

**lokaler Aufruf:** Kommunikation mit nächsttieferer lokaler Schicht

** remote Aufruf:** Kommunikation mit derselben Schicht auf entferntem Rechner

Blocking vs Non-Blocking
------------------------
Blockiert ein Programm (beispielsweise der `accept()` Call beim Java Socket API) so
muss dies unbedingt dokumentiert werden.

Bringt ausserdem viele Fehlermöglichkeiten mit sich. Bei blockierenden Methoden
deshalb immer ein Timeout setzen.

======================   ====================   =====================
                         Synchrones Protokoll   Asynchrones Protokoll
======================   ====================   =====================
Blocking API Call        Ja                     Situationsbedingt
Non-blocking API Call    Selten                 Ja
======================   ====================   =====================

Synchronous Remote Procedure Call
---------------------------------

.. images:: images/synchronous-rpc.png

Asynchronous Remote Procedure Call
----------------------------------

.. images:: images/asynchronous-rpc.png

