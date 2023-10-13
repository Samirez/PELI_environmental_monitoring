.PHONY: compile flash monitor

build/esp32.ino.elf: esp32.ino secrets.h
	rm compile_commands.json # arduino-cli doesn't compile if present
	arduino-cli compile --build-path build --fqbn esp32:esp32:esp32c3
	ln -sr build/compile_commands.json compile_commands.json

compile: build/esp32.ino.elf

flash: build/esp32.ino.elf
	arduino-cli upload --input-dir build --fqbn esp32:esp32:esp32c3 -p /dev/ttyUSB0

monitor:
	arduino-cli monitor -p /dev/ttyUSB0 -c baudrate=115200  
