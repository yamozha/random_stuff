echo "Do you want to see the weather or the state of the moon? (1 or 2)"
echo "Number:"; read "Foremoon"
if $Foremoon == "1"; echo "Please specify your city";read "City"

if $Foremoon == "2"
   then curl wttr.in/Moon
if $Foremoon == "1"
   then curl wttr.in/~$City

echo "hope you have nice day!!!"

#this is a work in progress application.
