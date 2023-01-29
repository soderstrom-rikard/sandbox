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

void decode(istream &source, ostream &dest)
{
    // stop istream from eating new lines
    source.unsetf(std::ios::skipws);

    unsigned char last = 0;
    unsigned char current;
    while (source >> current)
    {
        unsigned char delta = current + last;
        std::cout << "current '" << current << "' last '" << last << "' delta '" << static_cast<unsigned>(delta) << "'" << std::endl;
        dest << delta;
        last = delta;
    }
}

void encode(istream &source, ostream &dest)
{
    // stop istream from eating new lines
    source.unsetf(std::ios::skipws);

    unsigned char last = 0;
    unsigned char current;
    while (source >> current)
    {
        unsigned char delta = current - last;
        std::cout << "current '" << current << "' last '" << last << "' delta '" << static_cast<unsigned>(delta) << "'" << std::endl;
        dest << delta;
        last = current;
    }
}

} // namespace filecast::libraries::delta
