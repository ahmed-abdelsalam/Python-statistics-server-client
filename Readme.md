


the project runs a server script to do the follow :

	1- read configuration data from config.xml
	2- depending on the read in the previous step it shpuld connect to the clients using ssh connection
	3- upload using sftp protocol the client script "monitor.py"
	4- run this script on each client
	5- recieve the statistics (ram usage , cpu usage , uptime) from the client script using HTTP PUT Request and send (200) status Respond
	6- decrypt the information in PUT Request using 16-bit decryption
	7- connect to the database (sqlite3) to store the statistics in the file db.sqlite3
	8- check the alerts limit given in the "config.xml" with the statistics read by the client script
	9- send e-mail to the given address if the statistics exceeds the alert limits
	10- handle error exceptions in connection in the previous steps and print messages to informe the server user with these errors






Prerequisites :

	On the server side:
	
		1- python must be installed on the server and added to the system path in case of windows system
		2- the modules (sqlite3, paramiko , pycrypto , numpy , base64 ) must be installed on python
		3- ssh must be enabled using the command sudo apt-get install openssh or install the program openssh in windows

	On the client side:
	
		1- python must be installed on the client and added to the system path in case of windows system
		2- the modules (psutil ,json, paramiko , pycrypto , numpy , base64) must be installed on python
		3- ssh must be enabled using the command sudo apt-get install openssh or install the program openssh in windows	
	
	

initialize the database:

	the sqlite3 should be installed on the server
			1- download the proper version to your server for the url https://sqlite.org/download.html
			2- in case of windows OS make a directory in the C partition named "sqlite"
			3- add this directory to the system path variable - search on google if you don't know
			
			
	
Assumptions:

	Firstly I've assumed that each XML file handle only one client and for demo purposes I read only one XML file.
	Secondly I used SSH to send a command to the client to run the script.
	Third I used the idea of API to send the statistics using HTTP PUT REQUEST with simple encryption form to speed the connection 
	Forth I've made a file on the server named "config.py" which contain al the variables needed to be set before running the server
	




Issues: 

	please add responds for any issues found
	
	
	
	
