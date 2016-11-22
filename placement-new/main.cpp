// Placement new
// http://en.cppreference.com/w/cpp/language/new
#include <array>
#include <cstddef>
#include <cstdint>
#include <iostream>

const std::size_t mempool_size  = 0xA00000; // 10 MiB
const std::size_t chunk_size    = 0x20000;  // 128 KiB
const std::size_t num_of_arrays = mempool_size/chunk_size; // ~ 80 arrays

template <size_t N> struct byte_array : std::array<std::byte, N> {};
typedef byte_array<mempool_size > byte_pool;
typedef byte_array<chunk_size   > chunk_array;

int main ()
{
  // Initialize
  std::size_t  offset   = 0;
  auto mempool = new byte_pool(); // Allocated on heap
  std::array<chunk_array*, num_of_arrays> arrays_in_mempool = {nullptr};

  // Allocate
  std::cout << "memory pool address: " << mempool->data();
  for(auto&& a : arrays_in_mempool)
  {
    a = new (mempool->data()+offset) chunk_array();
    std::cout << "\ni = " << offset/chunk_size << ", offset = " << offset << ", latest = " << a;
    offset+=chunk_size;
  } std::cout << std::endl;

  delete mempool;
  return 0;
}
