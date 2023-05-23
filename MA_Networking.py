from scapy.all import *
info = '''
+=========================+
+    pyhton-Networking    +
+=========================+
'''
print(info)

# The network function has been modified to handle different packet types.
#has been extended to extract and display the source IP and destination IP addresses
#has been extended to extract and display the source port and destination port addresses
#is added to check for Raw packets using pkt.haslayer(Raw). If a Raw packet is detected, the packet and payload data are printed using pkt.show() and pkt[Raw].load, respectively.
def network(pkt):
    if pkt.haslayer(TCP):
        print("Packet sent...")
        print("TCP protocol:")
        pkt.show()
        print("-----------------------")
        src_ip = pkt[IP].src
        dst_ip = pkt[IP].dst
        s_port = pkt.sport
        d_port = pkt.dport
        print('SEND-IP : ' + src_ip)
        print('RESP_IP :' + dst_ip)
        print('SEND_PORT :' + str(s_port))
        print('RESP_PORT :' + str(d_port))
        print('-----------------------')
        if pkt.haslayer(Raw):
            print("DATA :",pkt[Raw].load)
            print("Packet size :" + str(len(pkt[TCP])))
    elif pkt.haslayer(UDP):
        print("Packet sent...")
        print("UDP protocol:")
        pkt.show()
        src_ip = pkt[IP].src
        dst_ip = pkt[IP].dst
        s_port = pkt.sport
        d_port = pkt.dport
        print('SEND-IP : ' + src_ip)
        print('RESP_IP :' + dst_ip)
        print('SEND_PORT :' + str(s_port))
        print('RESP_PORT :' + str(d_port))
        print('-----------------------')
        if pkt.haslayer(Raw):
            print("DATA :",pkt[Raw].load)
            print("Packet size :" + str(len(pkt[UDP])))

    elif pkt.haslayer(ICMP):
        print("Packet sent...")
        print("ICMP protocol:")
        pkt.show()
        src_ip = pkt[IP].src
        dst_ip = pkt[IP].dst
        s_port = pkt.sport
        d_port = pkt.dport
        print('SEND-IP : ' + src_ip)
        print('RESP_IP :' + dst_ip)
        print('SEND_PORT :' + str(s_port))
        print('RESP_PORT :' + str(d_port))
        print('-----------------------')
        if pkt.haslayer(Raw):
            print("DATA :",pkt[Raw].load)
            print("Packet size :" + str(len(pkt[TCMP])))


# Replace 'Wi-Fi' in the iface parameter with the correct name of the Wi-Fi interface on your system , or your ethernet interface

sniff(iface='Wi-Fi', prn=network)
