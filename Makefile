gentoodebrpm: gentoodebrpm.c
	gcc -O3 -march=native gentoodebrpm.c -o /usr/bin/gentoodebrpm
	mkdir /var/log/gentoodebrpm
