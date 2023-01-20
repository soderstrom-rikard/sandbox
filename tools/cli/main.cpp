// C++ standard library headers
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

// System dependencies
// NONE

// Library headers
#include "libraries/delta/delta.h"

// Local
// NONE

void list_casters(const std::vector<std::string> &casters)
{
    std::cout << "=========== List of data encoding casters ======================================" << std::endl;

    for (const auto &v: casters)
    {
        std::cout << "- " << v << std::endl;
    }
    std::cout << "================================================================================" << std::endl;
}

auto parse_casters(const std::vector<std::string> &casters, const std::string &ctest_casters_line) -> std::vector<std::string>
{
    std::vector<std::string> test_casters;

    for (const auto &v: casters)
    {
        // TODO
        // split test_casters_line and find casters among available casters.
    }

    // TODO: only sun for selected casters instead of all casters
    test_casters = casters;
    return test_casters;
}

void run_tests(const std::vector<std::string> &casters)
{
    std::cout << "=========== Built-in tests of data encoding casters ============================" << std::endl;

    const auto                        mode_rwb = std::ios::binary | std::ios::in | std::ios::out | std::ios::trunc;
    std::basic_fstream<unsigned char> source("/tmp/filecast.source", mode_rwb);
    std::basic_fstream<unsigned char> dest1("/tmp/filecast.dest1", mode_rwb);
    std::basic_fstream<unsigned char> dest2("/tmp/filecast.dest2", mode_rwb);

    if (source.is_open())
    {
        std::cout << "source is open" << std::endl;
    }
    else
    {
        std::cout << "source is closed" << std::endl;
    }

    std::string s = "hello world";
    source.write(reinterpret_cast<unsigned char *>(s.data()), s.size());
    source.seekp(0);

    filecast::libraries::delta::encode(
        static_cast<filecast::libraries::delta::uint8_istream &>(source),
        static_cast<filecast::libraries::delta::uint8_ostream &>(dest1));
    dest1.seekp(0);

    filecast::libraries::delta::decode(dest1, dest2);
    dest2.seekp(0);

    std::cout << "================================================================================" << std::endl;
}

auto main(int argc, const char **const argv) -> int
{
    const std::vector<std::string> casters = {
        "delta"};

    bool                     do_list_casters = false;
    std::vector<std::string> test_casters;

    for (int i = 1; i < argc; i++)
    {
        const std::string option(argv[i]);
        // options with zero values
        if (("-l" == option) or ("--list-casters" == option))
        {
            do_list_casters = true;
        }

        // options with single values
        if ((i + 1 < argc) and (("-t" == option) or ("--test-casters" == option)))
        {
            const std::string value(argv[++i]);
            test_casters = parse_casters(casters, value);
        }
    }

    if (do_list_casters)
    {
        list_casters(casters);
    }

    if (not test_casters.empty())
    {
        run_tests(test_casters);
    }

    return EXIT_SUCCESS;
}
