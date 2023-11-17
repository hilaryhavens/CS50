// Modifies the volume of an audio file

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Number of bytes in .wav header
const int HEADER_SIZE = 44;

int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc != 4)
    {
        printf("Usage: ./volume input.wav output.wav factor\n");
        return 1;
    }

    // Open files and determine scaling factor
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    float factor = atof(argv[3]);

    //Copy header from input file to output file - START around 2:45 of walkthrough
    //Create an array of bytes to store the header from the input file
    uint8_t header[HEADER_SIZE];
    //Get information about the header from the input file
    fread(header, HEADER_SIZE, 1, input);
    //Copy that information about the header into the output file
    fwrite(header, HEADER_SIZE, 1, output);

    // TODO: Read samples from input file and write updated data to output file - consider uint16_t - allocate memory in computer?
    //Create a buffer variable
    int16_t buffer;
    //Run a loop for each sample as the file is being read
    while (fread(&buffer, sizeof(int16_t), 1, input))
    {
        //Multiply the sample value by the volume factor
        buffer = buffer * factor;
        //Write the new sample to the output file, so that updated sample becomes output
        fwrite(&buffer, sizeof(int16_t), 1, output);
    }

    // Close files
    fclose(input);
    fclose(output);
}
