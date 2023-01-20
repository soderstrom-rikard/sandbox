// C++ standard library headers
#include <cstdint>
#include <istream>

// System dependencies
// NONE

// Local
// NONE

namespace filecast::libraries::delta
{
using uint8_istream = std::basic_istream<std::uint8_t>;
using uint8_ostream = std::basic_ostream<std::uint8_t>;

void decode(uint8_istream &source, uint8_ostream &dest);
void encode(uint8_istream &source, uint8_ostream &dest);

} // namespace filecast::libraries::delta
