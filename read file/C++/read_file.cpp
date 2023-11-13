#include <iostream>
#include <fstream>
#include <string>

int main() {
    std::ifstream sourceFile("/workspaces/Rusty-Kernels-Code/read file/source.txt");
    std::ofstream destFile("/workspaces/Rusty-Kernels-Code/read file/destination.txt");

    if (!sourceFile.is_open()) {
        std::cerr << "Unable to open source file.\n";
        return EXIT_FAILURE;
    }

    if (!destFile.is_open()) {
        std::cerr << "Unable to open destination file.\n";
        return EXIT_FAILURE;
    }

    std::string line;
    while (std::getline(sourceFile, line)) {
        destFile << line;
    }

    sourceFile.close();
    destFile.close();

    return 0;
}
