Write a rule list for such a firewall such that hosts from the local network 1.2.3.0/24 can connect to the Internet (with TCP), but incoming connections are blocked. You can use subnet addresses like “1.2.3.0/24” in your rules to match all hosts in a local network. You can also use an address like “! 1.2.3.0/24” to refer to all hosts outside the local network.

Stateless firewalls don’t understand the concept of connections. You must allow TCP packets in both directions, otherwise your TCP connections will not work properly. The only thing you can do to prevent incoming connections is to block incoming SYN packets (be careful not to block incoming SYN-ACK packets!). This does not protect from all attacks (the attacker could still use other packets to do port scans, ACK scan)

allow TCP 1.2.3.0/24:* -> !1.2.3.0/24:* * // allow all packet types
deny TCP !1.2.3.0/24:* -> 1.2.3.0/24:* SYN // block incoming SYN packets
allow TCP !1.2.3.0/24:* -> 1.2.3.0/24:* * // allow other packet types


================================================================
Can you write similar rules for UDP? What problems could arise?

no flags in udp 
================================================================


    Imagine you want to allow connections to host 1.2.3.4. You do not want your host to be able to make connections to the outside. Is the following ruleset correct? Assume that only TCP is used.

allow TCP *:* -> 1.2.3.4:80,443 SYN
deny TCP 1.2.3.4:* -> *:* SYN
allow TCP 1.2.3.4:* -> *:* *
deny TCP *:* -> *:* *

The rules do not work. Hosts can only send SYN packets to 1.2.3.4. They cannot send any
data packets. (not even ACK)

=====================================================================
table ip 
chain in 

flush ruleset

table ip filter {
    chain input {
        type filter hook input priority 0; policy drop;

        tcp dport 80 accept
        tcp dport 22 accept
    }

    chain output {
        type filter hook output priority 0; policy drop;

        tcp sport 22 accept
    }
}

===========================================================================
example  : tcp dport 80 ct state { new, established } accept

chain output {
    type filter hook output priority 0; policy drop;

    ct state established,related accept
}

related = new connection linked to existing one

===========================================================================

tcp dport 22 ct count 10 accept = counts the number with the same source address

you can do :

tcp dport 80 ct count over 5 drop
tcp dport 80 accept