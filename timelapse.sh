
#!/usr/bin/python3

make_picture(){
	DATE=$(date +"%Y-%m-%d_%H%M%S")
	sudo raspistill -o $DATE.jpg -t 2000 -ISO 100 -ss 15000 -awb fluorescent -ex backlight -n
}

send_to_nas(){
	python3 /home/pi/Desktop/timelapse/copy_and_remove.py
}


make_picture
send_to_nas
