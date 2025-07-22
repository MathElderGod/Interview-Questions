CXX=g++
CXXFLAGS=-std=c++17 -Wall -Wextra -O2
TARGET=TemperaturePrompt
SRCS=TemperaturePrompt.cpp
OBJS=TemperaturePrompt.o
HEADERS=TemperaturePrompt.hpp

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CXX) $(CXXFLAGS) -o $@ $^

TemperaturePrompt.o: TemperaturePrompt.cpp TemperaturePrompt.hpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

.PHONY: clean

clean:
	rm -f $(OBJS) $(TARGET)

