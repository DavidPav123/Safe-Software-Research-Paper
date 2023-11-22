#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *sourceFile, *destFile;
    int ch; // Use int to handle EOF correctly

    // Open the source file in read mode
    sourceFile = fopen("/workspaces/Rusty-Kernels-Code/read-write/source.txt", "r");
    if (sourceFile == NULL) {
        perror("Error opening source file");
        return 1;
    }

    // Open the destination file in write mode
    destFile = fopen("/workspaces/Rusty-Kernels-Code/read-write/destination.txt", "w");
    if (destFile == NULL) {
        perror("Error opening destination file");
        fclose(sourceFile);  // Close the source file before exiting
        return 1;
    }

    // Read characters from source file and write them to destination file
    while ((ch = fgetc(sourceFile)) != EOF) {
        fputc(ch, destFile);
    }

    // Close the files
    fclose(sourceFile);
    fclose(destFile);

    return 0;
}
