IP   ?= 127.0.0.1
PORT ?= 8000

.PHONY: runserver
runserver: bin/python3 manage.py
	$^ $@ $(IP):$(PORT)

.PHONY: install update gz
install: gz
	$(MAKE) update
update:
	sudo apt update
	sudo apt install -uy `cat apt.txt`
	bin/pip3 install -Ur reqirements.in
gz:
