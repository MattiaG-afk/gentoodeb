debrpm: debrpm.py
	mkdir -p /var/log/debrpm
	chmod +x debrpm.py
	cp debrpm.py /usr/bin/debrpm
uninstall:
	rm -rf /var/log/debrpm /usr/bin/debrpm
