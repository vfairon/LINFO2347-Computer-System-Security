qemu-system-x86_64 -cpu max -smp 4 -m 10G -drive file=mininet.qcow2 -net user,hostfwd=tcp::10022-:22 -net nic

export TERM=xterm-256color

ssh mininet@localhost -p 10022

sudo mn -c

sudo chmod o+w LINFO2347/ -R
sudo -E python3 topo.py 42172200

source attack_script.sh

touch /tmp/full_attack_test_to_show_teacher.pcap
chmod 644 /tmp/full_attack_test_to_show_teacher.pcap
sudo tshark -i any -w /tmp/full_attack_test_to_show_teacher.pcap

 scp -P 10022 mininet@localhost:/tmp/attack_b.pcap ./
