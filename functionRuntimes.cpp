//Author: Unknown
//This code was written at some point while I was taking my Data Structues and Algorithms class. As I understand, this code pertains to the subject of 
//the uses of static and dynamic memory. This code has not been excuted since prior to 2020.
#include<iostream>
#include<chrono>
#include<string>

void staticArray();
void heapArray();
void stackArray();
void functionRuntimes(std::string);

int main() {
      functionRuntimes("static");
      functionRuntimes("heap");
      functionRuntimes("stack");
	return 0;
	}

void staticArray(){//declares an array as static
	static int arr[100000];
	}

void heapArray(){//declares an array whose space in memory is allocated at runtime
	int *arr = new int[100000];
	delete [] arr;
	}

void stackArray(){//declares a normal array 
	int arr[100000];
	}
		
void functionRuntimes(std::string name){//takes in one string parameter that represents the name of a function
	if(name == "static"){//staticArray is called one billion times
		auto start = std::chrono::high_resolution_clock::now();
		for(int i = 0; i <= 1000000000; i++) staticArray();
		auto stop = std::chrono::high_resolution_clock::now();
		auto duration = std::chrono::duration_cast<std::chrono::microseconds>(stop - start);
		std::cout << "The time taken to run staticArray() 1,000,000,000 times is: " << duration.count() << " microseconds"<< std::endl;
		}
	else if(name == "heap"){//heapArray is called one billion times
		auto start = std::chrono::high_resolution_clock::now();
		for(int i = 0; i <= 1000000000; i++) heapArray();
		auto stop = std::chrono::high_resolution_clock::now();
		auto duration = std::chrono::duration_cast<std::chrono::microseconds>(stop - start);
		std::cout << "The time taken to run heapArray() 1,000,000,000 times is: " << duration.count() << " microseconds" << std::endl;
		}
	else if(name == "stack"){//stackArray is called on billion times
		auto start = std::chrono::high_resolution_clock::now();
		for(int i = 0; i <= 1000000000; i++) stackArray();
		auto stop = std::chrono::high_resolution_clock::now();
		auto duration = std::chrono::duration_cast<std::chrono::microseconds>(stop - start);
		std::cout << "The time taken to run stackArray() 1,000,000,000 times is: " << duration.count() << " microseconds" << std::endl;
		}
	}
