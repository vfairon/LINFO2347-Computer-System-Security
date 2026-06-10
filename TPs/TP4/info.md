tcpdump -i eth0 tcp port 22


save into a file :  -w ssh.pcap

Question 1: Imagine you want to monitor UDP traffic using flow monitoring. What is the role of the Inactive Timeout? Why do we need it and how does the timeout value affect the monitoring result?

===== inactive timeout determines how much the flow waits before saying it is finshed and exporting it. Since UDP is connectionless, there is no "end" of connection since there is no connection... so the timer is important.

Question 2: You have an application in your company that continuously sends data to a server. You see the following lines in the log files of your Netflow monitor (times are in HH:MM:SS format):

starttime endtime   source            destination     #pkts
13:32:10  13:34:09  139.23.4.5:45322  139.23.4.9:2222 320
13:34:10  13:36:09  139.23.4.5:45322  139.23.4.9:2222 252
13:36:10  13:38:09  139.23.4.5:45322  139.23.4.9:2222 295
...

You want to reduce the number of entries in your log file. Which parameter of the Netflow exporter do you have to change? What is the parameter’s current value and what would be a better value?


==== there is the inactivity timeout and the active timemout that stops and samples each.... this is what to modify (increase)

yaf uniflow is used to create one flow per connection and not per side of the connection. Yaf creates a binary file intended to be read by a flow collector (ex yafscii)

reste des questions à faire si nécéssaire
