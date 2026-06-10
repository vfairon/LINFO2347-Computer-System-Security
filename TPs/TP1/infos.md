When you send SYN packets, you are doing a standard TCP port scan.When you send SYN packets, you are doing a standard TCP port scan. The target responds with:

SYN-ACK (SA) — port is open, a service is listening
RST — port is closed
No response / ICMP error — port is filtered by a firewall

When you send ACK packets instead, the behavior changes completely. An ACK packet does not initiate a connection — it is normally only sent mid-connection. So the target has no connection state to match it against, and responds with:

RST — regardless of whether the port is open or closed, because the ACK is unexpected

At first glance this seems useless, but ACK scanning is actually a classic firewall detection technique. A stateless firewall filtering inbound SYN packets (to block connection attempts) may still let ACK packets through, since ACK looks like a reply to an outbound connection. So:

If you get no response — a stateful firewall is dropping the packet (it knows there is no matching connection)
If you get RST — the packet reached the host, meaning either there is no firewall or it is stateless

So ACK scanning does not tell you whether a port is open, but it tells you whether a firewall is present and whether it is stateful or stateless.