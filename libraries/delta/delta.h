// C++ standard library headers
#include <cstdint>
#include <istream>

// System dependencies
// NONE

// Local
// NONE

namespace filecast::libraries::delta
{
using istream = std::istream;
using ostream = std::ostream;

void decode(istream &source, ostream &dest);
void encode(istream &source, ostream &dest);

} // namespace filecast::libraries::delta
