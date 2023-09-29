.PHONY: compile flash monitor

compile:
	arduino-cli compile --build-path build --fqbn esp32:esp32:esp32c3

flash:
	arduino-cli upload --fqbn esp32:esp32:esp32c3 -p /dev/ttyUSB0

monitor:
	arduino-cli monitor -p /dev/ttyUSB0 -c baudrate=115200  
