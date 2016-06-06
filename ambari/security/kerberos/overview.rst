Kerberos Overview
=================

Strongly authenticating and establishing a user’s identity is the basis for secure access in |rbd-stack|.
Users need to be able to reliably “identify” themselves and then have that identity propagated throughout the |rbd-stack| cluster.
Once this is done, those users can access resources (such as files or directories) or interact with the cluster (like running Flink jobs).
Besides users, |rbd-stack| cluster resources themselves (such as Hosts and Services) need to authenticate with each other to avoid potential malicious systems or daemon’s “posing as” trusted components of the cluster to gain access to data.

|rbd-stack| uses Kerberos as the basis for strong authentication and identity propagation for both user and services.
Kerberos is a third party authentication mechanism, in which users and services rely on a third party - the Kerberos server - to authenticate each to the other.
The Kerberos server itself is known as the **Key Distribution Center**, or **KDC**.
At a high level, it has three parts:

* A database of the users and services (known as **principals**) that it knows about and their respective Kerberos passwords
* An **Authentication Server** (**AS**) which performs the initial authentication and issues a **Ticket Granting Ticket** (**TGT**)
* A **Ticket Granting Server** (**TGS**) that issues subsequent service tickets based on the initial **TGT**

A **user principal** requests authentication from the AS.
The AS returns a TGT that is encrypted using the user principal's Kerberos password, which is known only to the user principal and the AS.
The user principal decrypts the TGT locally using its Kerberos password, and from that point forward, until the ticket expires, the user principal can use the TGT to get service tickets from the TGS.
Service tickets are what allow a principal to access various services.

Because cluster resources (hosts or services) cannot provide a password each time to decrypt the TGT, they use a special file, called a **keytab**, which contains the resource principal's authentication credentials.
The set of hosts, users, and services over which the Kerberos server has control is called a **realm**.

**Terminology**

+---------------------------------+--------------------------------------------------------------------------------------------------------+
| Term                            | Description                                                                                            |
+=================================+========================================================================================================+
| Key Distribution Center, or KDC | The trusted source for authentication in a Kerberos-enabled environment.                               |
+---------------------------------+--------------------------------------------------------------------------------------------------------+
| Kerberos KDC Server             | The machine, or server, that serves as the Key Distribution Center (KDC).                              |
+---------------------------------+--------------------------------------------------------------------------------------------------------+
| Kerberos Client                 | Any machine in the cluster that authenticates against the KDC.                                         |
+---------------------------------+--------------------------------------------------------------------------------------------------------+
| Principal                       | The unique name of a user or service that authenticates against the KDC.                               |
+---------------------------------+--------------------------------------------------------------------------------------------------------+
| Keytab                          | A file that includes one or more principals and their keys.                                            |
+---------------------------------+--------------------------------------------------------------------------------------------------------+
| Realm                           | The Kerberos network that includes a KDC and a number of Clients.                                      |
+---------------------------------+--------------------------------------------------------------------------------------------------------+
| KDC Admin Account               | An administrative account used by Ambari to create principals and generate keytabs in the KDC.         |
+---------------------------------+--------------------------------------------------------------------------------------------------------+