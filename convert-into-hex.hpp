// https://isocpp.org/wiki/faq/templates#templates-defn-vs-decl
#ifndef CONVERT_TO_HEX_HPP
#define CONVERT_TO_HEX_HPP

#include <iostream> // DEBUG
#include <cstdint>
#include <string>
#include <type_traits>

inline std::string convert_into_hexstr(uint8_t * source, size_t bytes_to_convert)
{
    //printf("\tbytes_2_conv %d\n", bytes_to_convert);
    static const char *lookup = "0123456789ABCDEF";

    const size_t string_size = 2 + 2 * bytes_to_convert;
    //printf("\tstring_size  %d\n", string_size     );

    std::string hexstring(string_size,'0');
    hexstring[1] = 'x';
    //printf("\thexstring    %s\n", hexstring.c_str());

    //printf("\tsource at    %p\n", source          );

    for(auto i=0u; i<bytes_to_convert; i++)
    {
        //printf("at offset %d with value %d\n", i, source[i]);
        hexstring[2u+2*i+0u] = lookup[static_cast<uint8_t>((source[i] >> 0u) & 0x0Fu)];
        hexstring[2u+2*i+1u] = lookup[static_cast<uint8_t>((source[i] >> 4u) & 0x0Fu)];
    }

    return hexstring;
}

template<typename T>
std::string convert_into_hexstr(T value)
{
    static_assert(!std::is_pointer<T>  ::value, "Unable to convert raw pointer to hexstr");
    return convert_into_hexstr(reinterpret_cast<uint8_t*>(&value), sizeof(T));
}

#endif // CONVERT_TO_HEX_HPP
