#include <ctime>
#include <iostream>
#include <fstream>

#define ROW_SIZE 128

void generate_row() {
    std::fstream file;
    file.open("cpp_row.txt", std::ios::out);
    if (!file) {
        std::cout << "File is not opened";
        return;
    }
    else {
        file << fflush;
        std::cout << "Opened";
        srand(time(NULL));
        for (int i(0); i < ROW_SIZE; ++i) {
            file << rand() % 2;
        }
        file.close();
    }
}

int main(int argc, char* argv[]) {
    generate_row();
    return 0;
}