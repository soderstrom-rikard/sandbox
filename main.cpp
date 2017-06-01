#include "pack.hpp"

int main (int argc, char *argv[])
{
  // Initialize
  uint8_t data[1] = {255};
  uint8_t pack[21] = {0};

  // Pack
  pack::pack_1to7bits_in_one_byte     (pack + 0, data, 5, 0x0F);
  pack::pack_8bits_in_one_byte        (pack + 1, data);
  pack::pack_2to15bits_in_two_bytes   (pack + 2, data, 5, 0xA0);
  pack::pack_16bits_in_two_bytes      (pack + 4, data);
  pack::pack_10to23bits_in_three_bytes(pack + 6, data, 5, 0x1E);
  pack::pack_24bits_in_three_bytes    (pack + 9, data);
  pack::pack_18to31bits_in_four_bytes (pack +12, data, 5, 0x1E);
  pack::pack_32bits_in_four_bytes     (pack +16, data);

  // Cleanup
  return 0;
}
