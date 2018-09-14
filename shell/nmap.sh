echo -e "\e[33mSpecify your gateway"
echo -e "\e[0m192.168.?.*"; read "Gateway"
echo -e "\e[5m\e[101m\e[1mResults\e[0m"
echo -e "------------------------------"
sudo nmap -sn 192.168.$Gateway.* 

echo -e "------------------------------"
