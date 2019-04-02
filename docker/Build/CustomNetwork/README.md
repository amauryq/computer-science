sudo ip link add br10 type bridge
sudo ip addr add 10.10.100.1/24 dev br10
sudo ip link set br10 up
ifconfig
