#include <stdio.h>
#include <stdlib.h>

int main() {
    char* source = NULL;
    FILE* sourceFile = fopen("/workspaces/Rusty-Kernels-Code/read-write/source.txt", "r");
    FILE* destFile = fopen("/workspaces/Rusty-Kernels-Code/read-write/destination.txt", "w");

    if (sourceFile != NULL && destFile != NULL) {
        /* Go to the end of the file. */
        if (fseek(sourceFile, 0L, SEEK_END) == 0) {
            /* Get the size of the file. */
            long bufsize = ftell(sourceFile);
            if (bufsize == -1) { /* Error */ }

            /* Allocate our buffer to that size. */
            source = malloc(sizeof(char) * (bufsize + 1));

            /* Go back to the start of the file. */
            if (fseek(sourceFile, 0L, SEEK_SET) != 0) { /* Error */ }

            /* Read the entire file into memory. */
            size_t newLen = fread(source, sizeof(char), bufsize, sourceFile);
            if (ferror(sourceFile) != 0) {
                fputs("Error reading file", stderr);
            }
            else {
                source[newLen++] = '\0'; /* Just to be safe. */

                // Write to the destination file
                fwrite(source, sizeof(char), newLen, destFile);
            }
        }
        fclose(sourceFile);
        fclose(destFile); // Close the destination file
    }
    else {
        printf("Source or destination file could not be found");
    }

    if (source != NULL) {
        free(source); // Free the allocated memory
    }

    return 0;
}
