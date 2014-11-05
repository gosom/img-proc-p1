/*
* This is an exercise for the course:
* Image Processing, Retrieval, and Analysis (I) [university bonn]
*
* Accepts as an input the filename of an existing image (source)
* a target filename and two
* optional integers rmin ( 10 by default) and rmax (25 by default)
* it computes the euclidean distance of each pixel of the source image
* and if the distance is between rmin and rmax then makes the pixel black.
*
* Depends on the CImg library [http://cimg.sourceforge.net/index.shtml]
* The library consists only of one header file CImg.h
*
* Tested on Fedora Linux x86
* gcc version 4.8.3 20140911 (Red Hat 4.8.3-7) (GCC)
*
* CImg library was installed through yum package manager
*    yum install CImg-devel
* installed version: 1.5.8
*
* To compile:
* g++ -o task1 task1.cpp -lX11 -lpthread
*
*/
#include <iostream>

#include "CImg.h"

using namespace cimg_library;
using std::cout; using std::cerr;
using std::endl;

int main(int argc, char** argv) {

    if(argc < 3 || argc > 5){
        cerr << "Usage: " << argv[0] << " SOURCE" << " TARGET";
        cerr << " [rmin]" << " [rmax]" << endl;
        return 1;
    }

    const char* source_img = argv[1];
    const char* target_fname = argv[2];
    unsigned int rmin = 10, rmax = 25;

    if(argc == 4)
        rmin = atoi(argv[3]);

    if(argc == 5)
        rmax = atoi(argv[4]);

    CImg<unsigned char> src(source_img);

    const int w2 = src.width() / 2;
    const int h2 = src.height() / 2;

    // loop through image dimension
    // compute the euclidean distance
    // if the distace is between rmin and rmax then make the pixel black
    cimg_forXY(src, x, y){
        int delta_y = y - h2;
        int delta_x = x - w2;
        double distance = sqrt(delta_x * delta_x + delta_y * delta_y);
        if(rmin <= distance && distance <= rmax)
            src(x, y) = 0;
    }

    src.save(target_fname);
    return 0;

}
