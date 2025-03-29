all: 
	make build

build:
	python generate.py --mode build

clean:
	python generate.py --mode clean