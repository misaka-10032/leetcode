CC := g++
CXXFLAGS := -std=c++11
CXXFLAGS += -g -O0

all: main

main.o: main.cpp solution.hpp

main: main.o

test: all
	./main

clean:
	rm -f main *.o

.PHONY:
	test clean
