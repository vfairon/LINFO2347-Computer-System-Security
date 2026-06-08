import random
"""
Answers : 
Dest : since it is id 2 it is ip : 10.12.0.40
Src : it is the one of the topology : 10.2.0.2

filters : ip.src == 10.2.0.2 &&  ssh && _ws.col.info contains "Encrypted" => gives 104 totally diff donc wierd no ?

 tshark -r full_test_cpyfilter_with_filter.pcap -Y 'ip.src == 10.2.0.2 && ssh && _ws.col.info contains "Encrypted"' -T fields -e frame.number -e frame.len | awk '{ if ($2 > max) { max=$2; max_idx=NR-1; frame=$1 } } END { print "0-Based Index: " max_idx " | Frame Number: " frame " | Size: " max }'
"""



noma = 42172200

print(f"id of ip {noma//10000%3 }")
num_iters_low = 10
num_iters_high = 60
random.seed(noma)

print(f"the num of iterations {random.randint(num_iters_low, num_iters_high)}")


#---------------------------

# 10.12.0.20

num_iters_low = 1000
num_iters_high = 2000

print(f" second dest ip is : {noma // 10000 %2}")
random.seed(noma)
num_iters = random.randint(num_iters_low, num_iters_high)
print(f"the num of iterations {num_iters}")
"""
Answsers : 


- Ip source : either topology (10.2.0.2) or dns server (10.12.0.20)
- IP attack : 10.1.0.3 the one "sending" (by spoofed) the packet
- Occurences : tshark -r full_test_cpyfilter_with_filter.pcap -Y 'ip.src == 10.1.0.3 && ip.dst == 10.12.0.20 && dns.flags.response == 0 && dns.qry.type == 255 && dns.qry.name contains "example.com"' -T fields -e dns.qry.name | sort -u | wc -l
- id of max packet : tshark -r full_test_cpyfilter_with_filter.pcap -Y 'ip.src == 10.1.0.3 && ip.dst == 10.12.0.20 && dns.flags.response == 0 && dns.qry.type == 255 && dns.qry.name contains "example.com" && udp && !tcp' -T fields -e frame.number -e frame.len -e dns.qry.name | awk '!seen[$3]++ { if ($2 > max) { max=$2; max_idx=idx; frame=$1 }; idx++ } END { print "0-Based Index: " max_idx " | Frame Number: " frame " | Size: " max }'
=> 0-Based Index: 35 | Frame Number: 4562 | Size: 134
"""
## 


