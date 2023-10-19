
This week I am preparing for the Progress Meeting. I have built a simple front-end interface and database for my program, and completed a simple prototype for presentation. In addition I wrote some routes for interacting with the game library system, where users can buy, sell and manage games. . The /checkout route handles the user's cart items, adding them to the user's library and clearing the cart. The route /library displays the user's game library and wallet balance; the /sell_game route allows the user to sell games from their library, thus updating their wallet balance accordingly. The necessary functions of the backend are basically developed. Next week I will focus on debugging. For example, adding a free game to the shopping cart cannot be checked out. There is also the need to replace the front end and database.

user2:$6$fJX/OgcfBYTTcTQI$KSV7bjCNZlXlzXDJ7xg1cR6YGDV11Si6EZDIfujB2Oeg3zHYHMew3ZUrWDPlbzEUfFLgfgpcASlTaicswFeLG1
john --format=sha512crypt user2_hash.txt
john --show user2_hash.txt

nmap -p 80 --script=http-server-header scanme.nmap.org

nmap -p 80 -sV scanme.nmap.org

echo "user2:$6$fJX/OgcfBYTTcTQI$KSV7bjCNZlXlzXDJ7xg1cR6YGDV11Si6EZDIfujB2Oeg3zHYHMew3ZUrWDPlbzEUfFLgfgpcASlTaicswFeLG1" | john --format=sha512crypt --stdin

DENIED Redis is running in protected mode because protected mode is enabled and no password is set for the default user. In this mode connections are only accepted from the loopback interface. If you want to connect from external computers to Redis you may adopt one of the following solutions: 1) Just disable protected mode sending the command 'CONFIG SET protected-mode no' from the loopback interface by connecting to Redis from the same host the server is running, however MAKE SURE Redis is not publicly accessible from internet if you do so. Use CONFIG REWRITE to make this change permanent. 2) Alternatively you can just disable the protected mode by editing the Redis configuration file, and setting the protected mode option to 'no', and then restarting the server. 3) If you started the server manually just for testing, restart it with the '--protected-mode no' option. 4) Setup a an authentication password for the default user. NOTE: You only need to do one of the above things in order for the server to start accepting connections from the outside.


Connection to host lost.
