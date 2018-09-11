echo -e "\e[36mYour Public IP is:"
curl ifconfig.io
echo -e "Your Local IP(s) is:"
ips=($(hostname -I))

for ip in "${ips[@]}"
do
    echo $ip
done
