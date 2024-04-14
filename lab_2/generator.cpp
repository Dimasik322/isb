#include <ctime>
#include <iostream>

#define ROW_SIZE 128


//This file contains function that generates 
//pseudo-random binary row by defined size.
void generate_row() {
    srand(time(NULL));
    for (int i(0); i < ROW_SIZE; ++i) {
        std::cout << rand() % 2;
    }
    std::cout << std::endl;
}

int main() {
    generate_row();
    return 0;
}