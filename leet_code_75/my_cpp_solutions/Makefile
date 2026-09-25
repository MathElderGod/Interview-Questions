CXX = g++ 
CXXFLAGS = -std=c++17 -Wall -Wextra 

CPP_FILES = $(wildcard *.cpp) 
EXECUTABLES = $(CPP_FILES:.cpp=) 

all: $(EXECUTABLES) 

%: %.cpp 
	$(CXX) $(CXXFLAGS) $< -o $@ 

clean: 
	find . -maxdepth 1 -type f -executable -delete
