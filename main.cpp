#include <limits>
#include "convert-into-hex.hpp"

void test_arithmetic()
{
    // 1 to 8 bytes unsigned
    uint8_t  u8  = std::numeric_limits<uint8_t >::max();
    uint16_t u16 = std::numeric_limits<uint16_t>::max();
    uint32_t u32 = std::numeric_limits<uint32_t>::max();
    uint64_t u64 = std::numeric_limits<uint64_t>::max();

    std::cout << u8  << "\t" << convert_into_hexstr(u8 ) << "\n";
    std::cout << u16 << "\t" << convert_into_hexstr(u16) << "\n";
    std::cout << u32 << "\t" << convert_into_hexstr(u32) << "\n";
    std::cout << u64 << "\t" << convert_into_hexstr(u64) << "\n";

    // 1 to 8 bytes signed
    int8_t  s8  = std::numeric_limits<int8_t >::max();
    int16_t s16 = std::numeric_limits<int16_t>::max();
    int32_t s32 = std::numeric_limits<int32_t>::max();
    int64_t s64 = std::numeric_limits<int64_t>::max();

    std::cout << s8  << "\t" << convert_into_hexstr(s8 ) << "\n";
    std::cout << s16 << "\t" << convert_into_hexstr(s16) << "\n";
    std::cout << s32 << "\t" << convert_into_hexstr(s32) << "\n";
    std::cout << s64 << "\t" << convert_into_hexstr(s64) << "\n";

    // 4 and 8 bytes floating point numbers
    float  f32 = std::numeric_limits<float >::max();
    double f64 = std::numeric_limits<double>::max();

    std::cout << f32 << "\t" << convert_into_hexstr(f32) << "\n";
    std::cout << f64 << "\t" << convert_into_hexstr(f64) << "\n";
}

void test_pointers()
{
    for (auto i=1u; i <= 8; i++)
    {
        size_t    size    = i*i*i*i; // 8**4 = 4096
        uint8_t * pointer = new uint8_t[size];
        for (auto j=0u; j < size; j++)
          pointer[j] = static_cast<uint8_t>(j & 0xFF);

        std::string s = convert_into_hexstr(pointer, size);
        std::cout << "pointer " << "\t" << s << "\n";

        std::cout << std::flush;
        delete[] pointer;
    }
}

void test_array_on_stack()
{
    uint8_t arr[4] = {0x04,0x05,0x06,0x07};
    uint8_t *pointer = arr;

    for(auto i=0u; i < sizeof(arr); i++)
        printf("at offset %d with value %d\n", i, pointer[i]);

    std::cout << "arr     size " << sizeof(arr) << "\n";
    std::string s = convert_into_hexstr(pointer,sizeof(arr));
    std::cout << arr << "\t" << s << "\n";

    std::cout << std::flush;
}

int main (int argc, char *argv[])
{
    (void)argc;
    (void)argv;

    // Test converting arithmethic values into hex
    //test_arithmetic();

    // Test converting raw pointer data into hex
    //test_pointers();

    // Test converting array on stack data into hex
    test_array_on_stack();

     return 0;
}
