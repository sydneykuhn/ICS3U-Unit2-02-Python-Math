#!/usr/bin/env python3

# Created by: Sydney Kuhn
# Created on: Sep 2020
# This program calculates the area and perimeter of a rectangle
#    with the dimensions provided by user


def main():

    # this function calculates area and perimeter

    # input
    length = int(input("Enter length of the rectangle (mm): "))
    width = int(input("Enter width of the rectangle (mm): "))

    # process
    area = length * width
    perimeter = 2 * (length + width)

    # output
    print("")
    print("Area is {0}mm2.".format(area))
    print("Perimeter is {0}mm.".format(perimeter))


if __name__ == "__main__":
    main()
