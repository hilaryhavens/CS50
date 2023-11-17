#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    //OPEN memory card
    // Set input filename
    char *infile = argv[1];

    // Ensure only one file
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    // Open input file
    FILE *file = fopen(infile, "rb");
    //If unable to open / file not there
    if (file == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    //Define buffer
    BYTE buffer[512];
    //Set null value to image pointer
    FILE *img = NULL;
    //Create a variable to store new filename
    char filename[100];
    //Set counter to 0
    int counter = 0;

    //Read 512 bytes into a buffer and repeat until end of card:
    while (fread(buffer, sizeof(buffer), 1, file))
    {
        //If start of JPEG
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            //If not the first first JPEG
            if (img != NULL)
            {
                //Close previous image
                fclose(img);
            }
            //Create filenames of format ###.jpg, starting at 000.jpg
            sprintf(filename, "%03i.jpg", counter);
            //OPEN a new jpeg with that file name
            img = fopen(filename, "w");
            //Use fwrite(data (pointer to all of the bytes that will be written), size (size of each elements to write), number (number of elements to write to file), outptr(FILE * to write to -likely the jpeg just opened))
            fwrite(buffer, sizeof(buffer), 1, img);
            //Increase counter
            counter++;

        }

        //Otherwise keep writing that file or keep looking for start of images
        else if (img != NULL)
        {
            fwrite(buffer, sizeof(buffer), 1, img);
        }
    }

    //Close any remaining files
    fclose(img);
    fclose(file);
    return 0;
}