# How it works
it uses bs4 to scrape the wca for competitions and alerts you when it finds a comp in your city
btw it alerts you by creating 50 files in your desktop folder server telling you you need to go the wca website
# How to set up
1. go to https://www.worldcubeassociation.org/competitions and enter your cuntry and if you want to also what event to compete in and copy the url
2. open main.py
3. change the url variable to the url you copied but dont forget to add "" around it
4.change the city variable to the city you want to scrape
5. change the desktop var to the path of the desktop where you want to create files to alert you
6. test the program by running it and it should alert you when it finds a competition in your city if you want to test it but there are no comps in your city you can use the wca domain and change the timeframe to all years
7.you need to set the script up to run on a schedule/on startup how is your thing i made a aplication with pyinstaller and used systemctl but you can use crontab or any other scheduler
8. you did it or not if it failed idk :)