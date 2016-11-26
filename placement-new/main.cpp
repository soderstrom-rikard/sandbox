// Placement new
// http://en.cppreference.com/w/cpp/language/new
#include <iostream>

const int mempool_size = 0xA00000; // 10 MiB

int main (int argc, char *argv[])
{
  // Initialize
  int  offset   = 0;
  char *mempool = new char[mempool_size];
  char *latest  = 0;

  // Allocate
  printf("mempool: %p\n", mempool);
  for(int i=0; i < 100; i++)
  {
    if (offset + i*0x20000 < mempool_size)
    {
      latest = new (mempool+offset) char[i*0x20000];
      offset += i*0x20000;
      printf("i = %3d, offset = %8d, latest = %p\n", i, offset, latest);
    }
    else break;
  }

  delete[] mempool;

  return 0;
}
