#include "helpers.h"
#include <stdio.h>
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
//Iterate over input image's height
    for (int i = 0; i < height; i++)
    {
        //Iterate over input image's width
        for (int j = 0; j < width; j++)
        {
            //Find RGB average
            float avg = (image[i][j].rgbtBlue + image[i][j].rgbtGreen +  image[i][j].rgbtRed) / 3.0;
            //Make sure that the average is rounded
            int iavg = nearbyintf(avg);
            //Set all values to average
            image[i][j].rgbtBlue = iavg;
            image[i][j].rgbtRed = iavg;
            image[i][j].rgbtGreen = iavg;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    //Set variables to 0
    int SepiaRed = 0;
    int SepiaGreen = 0;
    int SepiaBlue = 0;

    //Iterate over input image's height
    for (int i = 0; i < height; i++)
    {
        //Iterate over input image's width
        for (int j = 0; j < width; j++)
        {
            //Apply sepia formula and calculate new color value in integer format
            SepiaRed = round((0.393 * image[i][j].rgbtRed) + (0.769 * image[i][j].rgbtGreen) + (0.189 * image[i][j].rgbtBlue));
            SepiaGreen = round((0.349 * image[i][j].rgbtRed) + (0.686 * image[i][j].rgbtGreen) + (0.168 * image[i][j].rgbtBlue));
            SepiaBlue = round((0.272 * image[i][j].rgbtRed) + (0.534 * image[i][j].rgbtGreen) + (0.131 * image[i][j].rgbtBlue));

            //Check that RGB values are not greater than 255 and set to 255 otherwise
            if (SepiaGreen > 255)
            {
                SepiaGreen = 255;
            }

            if (SepiaBlue > 255)
            {
                SepiaBlue = 255;
            }

            if (SepiaRed > 255)
            {
                SepiaRed = 255;
            }

            //Set all values to new sepia values
            image[i][j].rgbtBlue = SepiaBlue;
            image[i][j].rgbtRed = SepiaRed;
            image[i][j].rgbtGreen = SepiaGreen;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    //Iterate over input image's height
    for (int i = 0; i < height; i++)
    {
        //Create temporary variable for the pixel values at a given location
        RGBTRIPLE temp[width];
        RGBTRIPLE temp2[width];
        //Iterate over input image's width (on a specific row)
        for (int j = 0; j < (width / 2); j++)
        {
            //Set temp value to pixel at a certain point
            temp[j] = image[i][j];
            //Swap pixels on horizonally opposite sides
            image[i][j] = image[i][(width - 1 - j)];
            image[i][(width - 1 - j)] = temp[j];
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    //Create a copy of image by declaring a new 2D array
    RGBTRIPLE copy[height][width];
    //Iterate over input image's height
    for (int i = 0; i < height; i++)
    {
        //Iterate over input image's width (on a specific row)
        for (int j = 0; j < width; j++)
        {
            //Copy image into "copy", pixel by pixel
            copy[i][j] = image[i][j];
        }
    }

    //Iterate over input image's height
    for (int i = 0; i < height; i++)
    {
        //Iterate over input image's width (on a specific row)
        for (int j = 0; j < width; j++)
        {
            //Set variables for sums to zero
            float red = 0.0;
            float green = 0.0;
            float blue = 0.0;

            //Series of "if" statements to cover edge cases
            //1) If i = 0 and subcases for j = 0, j = width - 1, and all other values
            if (i == 0)
            {
                if (j == 0)
                {
                    red = (copy[0][0].rgbtRed + copy[0][1].rgbtRed + copy[1][0].rgbtRed + copy[1][1].rgbtRed) / 4.0;
                    blue = (copy[0][0].rgbtBlue + copy[0][1].rgbtBlue + copy[1][0].rgbtBlue + copy[1][1].rgbtBlue) / 4.0;
                    green = (copy[0][0].rgbtGreen + copy[0][1].rgbtGreen + copy[1][0].rgbtGreen + copy[1][1].rgbtGreen) / 4.0;
                }

                else if (j == width - 1)
                {
                    red = (copy[0][width - 2].rgbtRed + copy[0][width - 1].rgbtRed + copy[1][width - 1].rgbtRed + copy[1][width - 2].rgbtRed) / 4.0;
                    blue = (copy[0][width - 2].rgbtBlue + copy[0][width - 1].rgbtBlue + copy[1][width - 1].rgbtBlue + copy[1][width - 2].rgbtBlue) /
                        4.0;
                    green = (copy[0][width - 2].rgbtGreen + copy[0][width - 1].rgbtGreen + copy[1][width - 1].rgbtGreen + copy[1][width -
                            2].rgbtGreen) / 4.0;
                }

                else
                {
                    red = (copy[0][j - 1].rgbtRed + copy[1][j - 1].rgbtRed + copy[0][j].rgbtRed + copy[1][j].rgbtRed + copy[0][j + 1].rgbtRed +
                            copy[1][j + 1].rgbtRed) / 6.0;
                    blue = (copy[0][j - 1].rgbtBlue + copy[1][j - 1].rgbtBlue + copy[0][j].rgbtBlue + copy[1][j].rgbtBlue + copy[0][j + 1].rgbtBlue +
                            copy[1][j + 1].rgbtBlue) / 6.0;
                    green = (copy[0][j - 1].rgbtGreen + copy[1][j - 1].rgbtGreen + copy[0][j].rgbtGreen + copy[1][j].rgbtGreen + copy[0][j +
                            1].rgbtGreen + copy[1][j + 1].rgbtGreen) / 6.0;
                }
            }

            //2) If i = height - 1 and subcases for j = 0, j = width - 1, and all other values
            else if (i == height - 1)
            {
                if (j == 0)
                {
                    red = (copy[height - 2][1].rgbtRed + copy[height - 1][0].rgbtRed + copy[height - 2][0].rgbtRed + copy[height - 1][1].rgbtRed) / 4.0;
                    blue = (copy[height - 2][1].rgbtBlue + copy[height - 1][0].rgbtBlue + copy[height - 2][0].rgbtBlue + copy[height - 1][1].rgbtBlue) /
                        4.0;
                    green = (copy[height - 2][1].rgbtGreen + copy[height - 1][0].rgbtGreen + copy[height - 2][0].rgbtGreen + copy[height -
                                1][1].rgbtGreen) / 4.0;
                }
                else if (j == width - 1)
                {
                    red = (copy[height - 2][width - 2].rgbtRed + copy[height - 1][width - 1].rgbtRed + copy[height - 2][width - 1].rgbtRed + copy[height
                            - 1][width - 2].rgbtRed) / 4.0;
                    blue = (copy[height - 2][width - 2].rgbtBlue + copy[height - 1][width - 1].rgbtBlue + copy[height - 2][width - 1].rgbtBlue +
                            copy[height - 1][width - 2].rgbtBlue) / 4.0;
                    green = (copy[height - 2][width - 2].rgbtGreen + copy[height - 1][width - 1].rgbtGreen + copy[height - 2][width - 1].rgbtGreen +
                                copy[height - 1][width - 2].rgbtGreen) / 4.0;
                }
                else
                {
                    red = (copy[height - 2][j - 1].rgbtRed + copy[height - 1][j - 1].rgbtRed + copy[height - 2][j].rgbtRed + copy[height - 1][j].rgbtRed
                            + copy[height - 2][j + 1].rgbtRed + copy[height - 1][j + 1].rgbtRed) / 6.0;
                    blue = (copy[height - 2][j - 1].rgbtBlue + copy[height - 1][j - 1].rgbtBlue + copy[height - 2][j].rgbtBlue +
                            copy[height - 1][j].rgbtBlue + copy[height - 2][j + 1].rgbtBlue + copy[height - 1][j + 1].rgbtBlue) / 6.0;
                    green = (copy[height - 2][j - 1].rgbtGreen + copy[height - 1][j - 1].rgbtGreen + copy[height - 2][j].rgbtGreen +
                            copy[height - 1][j].rgbtGreen + copy[height - 2][j + 1].rgbtGreen + copy[height - 1][j + 1].rgbtGreen) /
                            6.0;
                }
            }

            //3) If j = 0, but i is okay
            else if (j == 0)
            {
                red = (copy[i - 1][0].rgbtRed + copy[i - 1][1].rgbtRed + copy[i][0].rgbtRed + copy[i][1].rgbtRed + copy[i + 1][0].rgbtRed +
                      copy[i + 1][1].rgbtRed) / 6.0;
                blue = (copy[i - 1][0].rgbtBlue + copy[i - 1][1].rgbtBlue + copy[i][0].rgbtBlue + copy[i][1].rgbtBlue +
                        copy[i + 1][0].rgbtBlue + copy[i + 1][1].rgbtBlue) / 6.0;
                green = (copy[i - 1][0].rgbtGreen + copy[i - 1][1].rgbtGreen + copy[i][0].rgbtGreen + copy[i][1].rgbtGreen +
                        copy[i + 1][0].rgbtGreen + copy[i + 1][1].rgbtGreen) / 6.0;
            }

            //4) If j = width, but i is okay
            else if ((i > 0) && (i < (height - 1)) && (j == (width - 1)))
            {
                red = (copy[i - 1][width - 2].rgbtRed + copy[i - 1][width - 1].rgbtRed + copy[i][width - 2].rgbtRed +
                     copy[i][width - 1].rgbtRed + copy[i + 1][width - 2].rgbtRed + copy[i + 1][width - 1].rgbtRed) / 6.0;
                blue = (copy[i - 1][width - 2].rgbtBlue + copy[i - 1][width - 1].rgbtBlue + copy[i][width - 2].rgbtBlue +
                        copy[i][width - 1].rgbtBlue + copy[i + 1][width - 2].rgbtBlue + copy[i + 1][width - 1].rgbtBlue) / 6.0;
                green = (copy[i - 1][width - 2].rgbtGreen + copy[i - 1][width - 1].rgbtGreen + copy[i][width - 2].rgbtGreen +
                        copy[i][width - 1].rgbtGreen + copy[i + 1][width - 2].rgbtGreen + copy[i + 1][width - 1].rgbtGreen) / 6.0;
            }

            //For non-special cases, general formula to calculate the RGB pixels in a 3x3 area
            else if ((i > 0) && (i < (height - 1)) && (j > 0) && (j < (width - 1)))
            {
                red = (copy[i - 1][j - 1].rgbtRed + copy[i - 1][j].rgbtRed + copy[i - 1][j + 1].rgbtRed + copy[i][j - 1].rgbtRed +
                        copy[i][j].rgbtRed + copy[i][j + 1].rgbtRed + copy[i + 1][j - 1].rgbtRed + copy[i + 1][j].rgbtRed +
                        copy[i + 1][j + 1].rgbtRed) / 9.0;
                blue = (copy[i - 1][j - 1].rgbtBlue + copy[i - 1][j].rgbtBlue + copy[i - 1][j + 1].rgbtBlue + copy[i][j - 1].rgbtBlue +
                        copy[i][j].rgbtBlue + copy[i][j + 1].rgbtBlue + copy[i + 1][j - 1].rgbtBlue + copy[i + 1][j].rgbtBlue +
                        copy[i + 1][j + 1].rgbtBlue) / 9.0;
                green = (copy[i - 1][j - 1].rgbtGreen + copy[i - 1][j].rgbtGreen + copy[i - 1][j + 1].rgbtGreen + copy[i][j - 1].rgbtGreen +
                        copy[i][j].rgbtGreen + copy[i][j + 1].rgbtGreen + copy[i + 1][j - 1].rgbtGreen + copy[i + 1][j].rgbtGreen +
                        copy[i + 1][j + 1].rgbtGreen) / 9.0;
            }

            //Create averaged values
            int ared = round(red);
            int ablue = round(blue);
            int agreen = round(green);

            //Set image pixels to averaged pixels
            image[i][j].rgbtRed = ared;
            image[i][j].rgbtBlue = ablue;
            image[i][j].rgbtGreen = agreen;
        }
    }
    return;
}