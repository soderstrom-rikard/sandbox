// C++ standard library headers
#include <cstdlib>
#include <iostream>
#include <sstream>

// System dependencies
// NONE

// Local
#include "delta.h"

namespace filecast::libraries::delta
{

void decode(uint8_istream &source, uint8_ostream &dest)
{
    unsigned char last = 0;
    unsigned char current;
    while (source.read(&current, 1))
    {
        dest << current + last;
        last = current;
    }
}

void encode(uint8_istream &source, uint8_ostream &dest)
{
    unsigned char last = 0;
    unsigned char current;
    while (source.read(&current, 1))
    {
        dest << current - last;
        last = current;
    }
}

} // namespace filecast::libraries::delta
