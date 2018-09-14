echo -e "\e[33mSpecify your gateway"
echo -e "\e[0m192.168.?.*"; read "Gateway"

nmap -sL 192.168.$Gateway.* > result.txt

echo -e "\e[33mResults written in result.txt!!"
