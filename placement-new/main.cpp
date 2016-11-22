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
  std::cout << "mempool: " <<
   static_cast<void*>(mempool) << std::endl;
  for(int i=0; i < 100; i++)
  {
    if (offset + i*0x20000 < mempool_size)
    {
      latest = new (mempool+offset) char[i*0x20000];
      offset += i*0x20000;
      std::cout <<
        "i = "        << i                          <<
        ", offset = " << offset                     <<
        ", latest = " << static_cast<void*>(latest) << std::endl;
    }
    else break;
  }

  delete[] mempool;

  return 0;
}
