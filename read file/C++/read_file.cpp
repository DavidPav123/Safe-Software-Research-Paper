#include <iostream>
#include <fstream>
#include <string>

int main() {
    std::ifstream sourceFile("source.txt");
    std::ofstream destFile("destination.txt");

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
        destFile << line << '\n';
    }

    sourceFile.close();
    destFile.close();

    return 0;
}
