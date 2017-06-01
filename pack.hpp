// Highly inspired by http://graphics.stanford.edu/~seander/bithacks.html
//
// 32 bit aligned bit packing
// Num Bits | Dst Bytes | Assign  | Rationale
//     1- 7 |       1   | No      | Need at least one bit to pack, and at most 7 can be placed with offset
//        8 |       1   | Yes     | Equals 1 byte, assign directly
//     2-15 |       2   | No      | Need at least two bits to split on two   bytes, and at most 15 can be offset inside 2 bytes
//       16 |       2   | Yes     | Equals 2 bytes, assign directly
//    10-23 |       3   | No      | Need at least ten bits to split on three bytes, and at most 23 can be offset inside 3 bytes
//       24 |       3   | Yes     | Equals 3 bytes, assign directly
//    18-31 |       4   | No      | Need at least 18  bits to split on four  bytes, and at most 31 can be offset inside 4 bytes
//       32 |       4   | Yes     | Equals 4 bytes, assign directly
#ifndef __PACK_HPP__
#define __PACK_HPP__

#include <cstdint>

namespace pack {

/* Low-level bit manipulation */
inline void pack_1to7bits_in_one_byte     (uint8_t *dst, uint8_t *src, const uint8_t offset, const uint8_t mask)
{ dst[0] ^= (dst[0] ^ (src[0] << offset    )) & mask; }
inline void pack_8bits_in_one_byte        (uint8_t *dst, uint8_t *src)
{ dst[0] = src[0]; }
inline void pack_2to15bits_in_two_bytes   (uint8_t *dst, uint8_t *src, const uint8_t offset, const uint8_t mask)
{ dst[0] ^= (dst[0] ^ (src[0] >> offset    )) & mask;
  dst[1] ^= (dst[1] ^ (src[1] << (8-offset))) & mask;}
inline void pack_16bits_in_two_bytes      (uint8_t *dst, uint8_t *src)
{ dst[0] = src[0]; dst[1] = src[1]; }
inline void pack_10to23bits_in_three_bytes(uint8_t *dst, uint8_t *src, const uint8_t offset, const uint8_t mask)
{ dst[0] ^= (dst[0] ^ (src[0] >> offset    )) & mask;
  dst[1] ^= (dst[1] ^ (src[1] << (8-offset))) & mask;
  dst[1] ^= (dst[1] ^ (src[1] >> offset    )) & mask;
  dst[2] ^= (dst[2] ^ (src[2] << (8-offset))) & mask; }
inline void pack_24bits_in_three_bytes    (uint8_t *dst, uint8_t *src)
{ dst[0] = src[0]; dst[1] = src[1]; dst[2] = src[2]; }
inline void pack_18to31bits_in_four_bytes (uint8_t *dst, uint8_t *src, const uint8_t offset, const uint8_t mask)
{ dst[0] ^= (dst[0] ^ (src[0] >> offset    )) & mask;
  dst[1] ^= (dst[1] ^ (src[1] << (8-offset))) & mask;
  dst[1] ^= (dst[1] ^ (src[1] >> offset    )) & mask;
  dst[2] ^= (dst[2] ^ (src[2] << (8-offset))) & mask;
  dst[2] ^= (dst[2] ^ (src[2] >> offset    )) & mask;
  dst[3] ^= (dst[3] ^ (src[3] << (8-offset))) & mask; }
inline void pack_32bits_in_four_bytes     (uint8_t *dst, uint8_t *src)
{ dst[0] = src[0]; dst[1] = src[1]; dst[2] = src[2]; dst[3] = src[3]; }

};

#endif // __PACK_HPP__
