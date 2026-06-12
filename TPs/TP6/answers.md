Question 1: Confusion matrix^

Imagine you are testing an IDS for your company’s webserver. For the test, you send 1000 requests to the web server. 70 of them contain attacks. After the test, you check the log files and you discover that the IDS did not detect 50 of the attacks. You send an e-mail with this result to your boss.

    Your boss is not happy with your work. You forgot something important in your e-mail. What is it?
    Write down a possible confusion matrix for this result.





N = 1000
P = 70
N = 930

TP = 20
FN = 50


BAD ! FP/TN are not mentioned
missing info for the FP...


========================================================================


Snort rule has : action protocol src_ip src_port -> dst_ip dst_port (options;)
Example : alert tcp any any -> any any (msg:"TCP packet detected!"; sid:1;)
Which means :
alert     = raise an alert
tcp       = only TCP packets
any any   = any source IP and source port
->        = direction
any any   = any destination IP and destination port
msg       = alert message
sid       = Snort rule ID

========================================================================

Alert when admin : 
alert tcp any any -> any 80 (msg:"Admin page access detected"; content:"admin.html"; sid:1000001; rev:1;)

To evade can use other notation : /admin%2ehtml

To fix : use URI normalization (after cleaning)


alert tcp any any -> any 80 (msg:"Admin page access detected"; flow:to_server,established; content:"admin.html"; http_uri; nocase; sid:1000003; rev:1;)

"ok if 5connections/second"

alert tcp any any -> any 80 (msg:"Repeated admin page access"; content:"admin.html"; http_uri; nocase; detection_filter:track by_src, count 5, seconds 10; sid:1000005; rev:1;)
========================================================================

Exercise 2 — Detect DNS reflection attack
You have a pcap collected on the victim:

Victim = 192.168.1.140
DNS server = 192.168.1.1

The attack is a DNS reflection attack.

In a DNS reflection attack:

Attacker spoofs victim IP
        ↓
DNS servers receive fake queries
        ↓
DNS servers reply to victim
        ↓
Victim receives huge amount of DNS responses

The victim sees many packets like:

192.168.1.1:53 -> 192.168.1.140:random_port

So we want to detect too many DNS responses.

alert udp any 53 -> 192.168.1.140 any (msg:"Possible DNS reflection attack"; detection_filter:track by_dst, count 100, seconds 1; sid:2000002; rev:1;)

Detect amplified response & rate :
alert udp any 53 -> 192.168.1.140 any (msg:"Large DNS response / possible amplification"; dsize:>512; detection_filter:track by_dst, count 20, seconds 1; sid:2000003; rev:1;)

to make sure it is still ok : track the state, if already sent a query, can receive an answer, if not, no.


========================================================================
Exercise 3 — Port scanning detection

Syn Scan : 
alert tcp any any -> any any (msg:"Possible TCP SYN port scan"; flags:S; detection_filter:track by_src, count 20, seconds 5; sid:3000001; rev:1;)

Xmas scan :
alert tcp any any -> 192.168.1.140 any (msg:"Possible Xmas scan"; flags:FPU; detection_filter:track by_src, count 10, seconds 5; sid:3000004; rev:1;)


