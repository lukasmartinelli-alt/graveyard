***********************
Grundlagen und Remoting
***********************

Definitionen
============

Programm
--------
* Hat einen Anfang und ein Ende
* Akzeptiert Input und produziert Output
* Läuft deterministisch
* Ist clock-driven

System
------
Besteht aus Programmen und Subsystemen

* Hört evtl. nie auf
* Azeptiert immer Input
* Oft dynamisch konfiguriert
* Kann sich nichtdeterministisch verhalten
* Ist event-driven

Distributed System
------------------
A distributed system is a collection of independent computers that
appears to its users as a single coherent system.

Design Herausforderungen
========================

Transparency
------------

============   ===========
Transparency   Description
============   ===========
Access         Hide differences in data representation and how a resource is accessed
Location       Hide where the resource is located
Migration      Hide that the resource may move to another location
Relocation     Hide that the resource may be moved to another location while in use
Replication    Hide that resources is replicated
Concurrency    Hide that resource may be shared
Failure        Hide failure and recovery
============   ===========

================
Architekturstile
================



Middleware
----------

    Middleware ist infrastrukturelle Software zur Kommunikation zwischen
    Software-Komponenten und Anwendungen auf verschiedenen Computern

Die Middleware erfüllt folgende Funktionen:

* Dient als Verteilungsplatform die viele Protokolle unterstützt
* Bietet höheres Abstraktionsniveau
* Verbirgt Komplexität darunter

Gründe für eine Einführung:

* Interoperabilität
* Vereinfachung

Communication-oriented middleware
---------------------------------
Stellt ein von der Applikation unabhängiges Protokoll zur Verfügung.

* Low-level protocols and API (infrastructure)
* Sockets

Anwendungsorientierte Middleware
--------------------------------
Benutzt ein spezifisches Protokoll

* High-level protocols and API (programming models)
* CORBA IDL, RMI interfaces
* WSDL/SOAP Webservices

Dimensionen
-----------
Verteilte Software Systeme besitzen drei unabhängige Merkmale:

* Nebenläufigkeit
* Verteilung
* Persistenz

Client/Server Architecture Style
================================

Distributed Objects
-------------------
Jedes Objekt ist unabhängig vom Ort und antwortet auf einen Method Call.

N-Layers
--------
Jedes Layer kennt nur das tieferliegende Layer. Ein Request geht durch alle Layers
hindurch (Request flow) und wieder zurück (Response flow).

Client-Server
-------------
Der Client sendet einen Request auf den Server und bekommt die Antwort.

2-Tier Architecture
-------------------
Die Applikationsschichten lassen sich beliebig auf den Server oder Client auslagern.
Sowohl Persistenz und die eigentliche Business Logik wird vom Server bereitgestelllt, der Client ist lediglich ein Thin Client.
Das lässt sich in der Praxis nicht immer so leicht trennen, deshalb gibt es verschiedenste
Variationen.

3-Tier Architecture
-------------------
Tier 1  : Clients mit Browser
Tier 2: Web Server und Presentation Logic (z.B. HTML Templates)
Application Server und Business Logic
Tier 3: Database

Event Driven Architecture
-------------------------
Reagiert auf Ereignisse.

Peer-to-Peer Systeme
--------------------

Abstraktionsebenen
------------------

Datenaustausch
^^^^^^^^^^^^^^
* Sockets (UDP/TCP über IP)
* File Transfer
* Shared Database

Nachrichtenaustauch
^^^^^^^^^^^^^^^^^^^
* Message-Oriented Middleware
* HTTP GET, POST

Remote Procedure Call (RPC)
^^^^^^^^^^^^^^^^^^^^^^^^^^
* DCE RPC
* Java RMI, CORBA
* Web Services, RESTful HTTP


CORBA
-----

Object Orientation + Remoting = CORBA
CORBA ermöglicht es, mit verteilten Objekten zu programmieren.
CORBA benutzt ein eigenes TCP/IP Protokoll und giltet als veraltet, trotzdem wird
es vor allem in Banken in Legacy Systemen immer noch verwendet.

Prinzip
^^^^^^^

Ein Objekt sendet eine Message an ein anderes Objekt (lokal oder über das Netzwerk)
welches darauf antwortet. Diese Abstraktion erlaubt es theoretisch Komponenten über
Platformen und Sprachen hinweg wiederzuverwenden.

Services
^^^^^^^^
CORBA bringt von Haus aus Lösungen mit für typische Probleme in verteilten Systemen.

Fowler’s First Law of Distributed Object Design
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    Don’t distribute your objects!


Eight Fallacies of Distributed Systems
--------------------------------------

* The network is reliable
* Latency is zero
* Bandwidth is infinite
* The network is secure
* Topology doesn't change
* There is one administrator
* Transport cost is zero
* The network is homogeneous



Sockets
=======

Socket Programmierung ist im Grunde Low-Level Messaging.

Mechanismus
^^^^^^^^^^^
Es werden lediglich Byteströme auf Programmierebene ausgetauscht.
Ein Socket ist eine eindeutige Verbindung zwischen eine Client (IP + Port) und einem
Server (IP + Port).

Client kennt Hostname und Port für Connect mit Server:
1. stellt Connect her
2. erhält Socket Objekt
3. kommuniziert mit Methoden des Socket Objekts

Server kennt eigenen Port und ist im Listen Modus:
1. Listen: Wartet bis Client über den Connect Port verbindet
2. akzeptiert Request
3. erzeugt für jeden Request einen neuen Socket (neuer Port)
   um auf den Request zu antworten
4. Ursprünglicher Connect Sockets ist bereit für weitere Requests

Nachteile
^^^^^^^^^
* Byteströme müssen erstellt und geparst werden
* Messaging Format muss selbst spezifiziert und implementiert werden
* Viele fehlende Features die heute Middleware übernimmt (z.B. Synchronization)

Berkeley Sockets
^^^^^^^^^^^^^^^^
Funktioniert platformübergreifend für alle Sprachen gleich.

=========  ================
Primitive  Meaning
=========  ================
SOCKET     Create new communication end point
BIND       Attach a local address to a socket
LISTEN     Announce willingness to accept connections
ACCEPT     Block caller until connection request arrives
CONNECT    Actively attempt to establish connection
SEND       Send data over connection
RECEIVE    Receive data over connection
CLOSE      Release the connection

Java
^^^^
Socket benutzt standardmässing einen TCP/IP Socket.
Beispiel für einen Server, welcher die aktuelle Zeit liefert::

    public class TimeServer {
        public static void main(String args[]) throws Exception {
            int port = 2342;
            ServerSocket server = new ServerSocket(port);
            while(true) {
                Socket client = server.accept();
                try(PrintWriter out = new PrintWriter(client.getOutputStream(), true)) {
                    Date date = new Date();
                    out.println(date);
                }
            }
        }
    }

Beispiel für den Client der die Zeit vom Server holt::

    public class TimeClient {
        public static void main(String args[]) throws IOException {
            String host = "localhost";
            int port = 2342;

            Socket server = new Socket(host, port);
            try(BufferedReader in = new BufferedReader(new InputStreamReader(server.getInputStream))) {
                String date = in.readLine();
            }

    }

Best practice: Default-Konstruktor verwenden, Connect und Bind explizit machen::
    ServerSocket server = new ServerSocket(1234);
    Socket serverSocket = server.accept();

Unterschied Socket und ServerSocket:

Der ServerSocket macht im Konstruktor hinter den Kulissen einen BIND auf den Port
und ruft dann LISTEN auf.
Die eigentliche Socket Funktionalität ist in der Klasse Socket.

Weitere Java Klassen:

* DatagramSocket für UDP
* MulticastSocket für Multicasts mit UDP

Things that can go wrong:

* Attempt to connect to port that nobody is listening on
* Attempt to bind to port that is already in use (other program listening)
* Protocol mismatches (Format stimmt nicht überein, Buffer überläuft)

Message Exchange Pattern (MEP)
==============================


Remote Procedure Call (RPC)
===========================
Zwei Designdimensionen:

* lokaler Aufruf: Kommunikation mit nächsttieferer lokaler Schicht
* remote Aufruf: Kommunikation mit derselben Schicht auf entferntem Rechner

Blocking vs Non-Blocking
========================


Messaging
=========

Mit dem Message-Queuing Model enkoppelt man den Empfänger von der Zeitdimension.
Er kann selbst wählen, wie er die Nachricht empfangen will.

Der Sender kann auch eine lokale Queue verwenden um beispielsweise momentane
Übertragungsprobleme auszugleichen oder inkommende Nachrichten zu puffern.

API Primitives
--------------

=========  ================
Primitive  Meaning
=========  ================
PUT        Append message to specified queue
GET        Block until specified queue is nonempty and remove first message
POLL       Check a specified queue for messages and remove first message. Never block
NOTIFY     Install a handler to be called when a message is put into a specified queue

Java Messaging Service (JMS)
----------------------------
JMS eine Message Oriented Middleware (MOM) API um Nachrichten auszutauschen.
Externe JMS Provider (z.B. ein Messaging Server wie ApacheMQ) implementieren lediglich das
JMS Interface.

Terminology
^^^^^^^^^^^

JMS Client

JMS Producer/Publisher

JMS Consumer/Subscriber

JMS Message

JMS Queue

JMS Topic

Point-to-Point Channel
^^^^^^^^^^^^^^^^^^^^^^
Messages werden zu einem spezifischen Consumer gerouted, der eine Queue für die
Messages verwaltet. Jede Message geht an eine spezifische Queue.

Publish-Subscribe Channel
^^^^^^^^^^^^^^^^^^^^^^^^^
Messages werden an ein spezielles Topic gesendet. Subscriber können alle Messages
zu einem Topic abonnieren. Der Publisher muss die Consumer nicht kennen.

Quality of Service (QoS) Settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

=========          ================
Attribute          Description
=========          ================
Transport Type     Transport Protokoll für die Übertragung
FIFO delivery      Messages werden in der Reihenfolge zugestellt, in der sie gesendet wurden
Message length     Maximale Länge einer Nachricht
Setup retry count  Maximale Anzahl Versuche um die Remote Queue zu erreichen
Delivery retries   Maximale Anzahl Versuche um eine Nachricht in die Queue zu speichern

Definition MCA:
Multi Channel Architecture

Message Delivery Policy (QoS)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

NON_PERSISTENT

PERSISTENT

Produkte
^^^^^^^^

MS MQ
    Bestandteil von Windows (kann über Windows Features aktiviert werden)
IBM WebSphere MQ
    Diverse Messaging Patterns in mehreren Produkten
RabbitMQ
    ...
ZeroMQ
    ...

Non-Functional Requirements (NFR)
---------------------------------


Enterprise Integration Messaging
--------------------------------

EIP Patterns
------------

Summary
-------

Queue-basiertes Messaging gestattet die flexible und lose Kopplung
unterschiedlichster Systeme:

* Auf unterschiedlichen Plattformen
* In unterschiedlichen Programmiersprachen
* Mit völlig unterschiedlichen Message-Formaten (Text, Byte, Objekt).

Messaging wird heute vielfach als einfacherer Ansatz für die Integration
unterschiedlicher Systeme eingesetzt mit den Merkmalen:

* Einfachheit
* Lose Kopplung
* Erweiterbarkeit
* Skalierbarkeit
* Fehlertoleranz

Die APIs sind einfach zu benutzen, es müssen aber viele
Designentscheidungen getroffen werden:

* Message intent (command vs. data)
* Returning a response (request-reply)
* Huge amounts of data (sequencing)
* Slow messages (message expiration)
* QoS (guaranteed delivery, transactionality, idempotency)

RMI & Web Services
==================

Recurring Design Issues in Remoting:
* Wire protocol
* Naming/addressing of endpoints
* Message Exchange Pattern (MEP) on application level
* Request-Reply, One-Way, Long Polling, ...
* Data formatting (requests, replies) a.k.a. parameter syntax
* QoS policies:

Um diese Probleme in den Griff zu kriegen, wird ein Vertrag/Interface benötigt,
der diese Aspekte definiert.

Remote Method Invocation RMI
============================

Wird eine Methode auf einem Objekt aufgerufen, wird ein synchroner Aufruf vom Client
an den Server gemacht.
Der Anwendungsentwickler auf der Client-Seite bleibt der Remote Aufruf verborgen
(Proxy Pattern).

RMI-Registry
------------

Remote Objekte können auch referenziert werden, dies muss speziell
über einen Namensdienst (RMI-Registry) gehandhabt werden. Diese RMI-Registry
wird von der RMI-Referenzschicht zur Verfügung gestellt.
RMI stellt ebenfalls einen Mechanismus bereit um ein Remote Object,
dass als Parameter an ein anderes Remote Object übergeben wurde, dynamisch nachzuladen.

RMI-Compiler
------------
All die Stubs und Skeletons von Hand anzulegen wäre eine zu grosse Handarbeit.
Deshalb wird RMI-IDL (als Interface Sprache) benutzt. Mithilfe des RMI-Compiler
kann man dann vom RMI-IDL automatisch Proxies und Stubs erzeugen.

In neuen Java Versionen kann dies auch dynamisch zur Laufzeit mithilfe von Introspection
passieren.

Stub
----
Ein Stub ist ein Stellvertreterobjekt (Remote Proxy), das Clientaufruf an
Server weiterreicht.

Die Stub-Klasse baut Socket-Verbindung zu Server auf (CONNECT).
Sie schickt Namen der Methode und Parameter und holt das Ergebnis ab.

Skeleton
--------
Ein Skeleton nimmt Aufrufe des Stubs entgegen und leitet sie an
Serverobjekt weiter.

Erzeugt Socket auf demselben Port wie Stub (BIND/LISTEN/ACCEPT), wartet auf den
Methoden-aufruf vom client und delegiert diesen an das Objekt. Der Rückgabewert wird
dann über die Socketverbindung an Client zurück gesendet.

Beispiel
--------

Server und Client
^^^^^^^^^^^^^^^^^
Es muss ein Interface für die Remote-Methoden erstellt werden, dass sowohl
dem Client, als auch dem Server bekannt ist::

    import java.rmi.Remote;
    import java.rmi.RemoteException;
    public interface Hello extends Remote {
        String sayHello() throws RemoteException;
    }

Server
^^^^^^
Der Server implementiert nun dieses Interface::

    import java.rmi.RemoteException;
    import java.rmi.server.UnicastRemoteObject;
    public class HelloImpl extends UnicastRemoteObject implements Hello
    {
        public HelloImpl() throws RemoteException {
            super();
        }
        public String sayHello() throws RemoteException {
            return "Hello World!";
        }
    }

Nun muss ein Remote Object der Implementierung erzeugt und bei der RMI-Registry
angemeldet::

    import java.rmi.Naming;
    public class HelloServer {
        public static void main(String args[]) {
            try {
                HelloImpl obj = new HelloImpl();
                Naming.rebind("rmi://[hn]/remoteHello", obj);
            } catch (Exception e) { ... }
        }
    }

Client
^^^^^^

Zuerst muss das Remote Object von der RMI-Registry abgeholt werden.
Danach können wir auf dem Interface alle definierten Methoden aufrufen::

    import java.rmi.*;
    public class RmiClient {
        public static void main(String[] args) {
            try {
                Hello obj =(Hello)Naming.lookup("rmi://[hn]/remoteHello");
                String message = obj.sayHello();
                System.out.println(message);
            } catch (Exception e) { ... }
        }
    }

Deployment
----------
Die RMI-Registry wurde sowohl vom Client, als auch vom Server verwendet.
Um diese bereitzustellen, wird ein Infrastruktur Server benötigt.

Wer started die RMI-Registry?
Die RMI-Registry muss separat auf dem Infrastruktur Server gestartet und verwaltet
werden.



