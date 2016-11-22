#include <iostream>
#include <limits>
#include <string>

void read_cin()
{
    for(std::string line; std::getline(std::cin, line);)
    {
        // CONSTRUCTED: TAG - PRIMITIVE CONTEXT_SPECIFIC 0, LENGTH - INDEFINITIVE 0
        std::cout << line << std::endl;

        size_t pos = line.find("CONTEXT_SPECIFIC");

        size_t pos_start = line.find(' ', pos);
        size_t pos_end   = line.find(',', pos_start);

        uint64_t value = std::stoull(line.substr(pos_start,pos_end));
        std::cout << "value " << value << std::endl;
    }
}

void parse_cmd(int argc, char *argv[])
{
    // skip app name
    argc--;
    argv++;

    for(auto i=0; i < argc; i++)
    {
        std::cout << argv[i] << std::endl;
    }
}

int main (int argc, char *argv[])
{
    parse_cmd(argc, argv);
    read_cin();
    (void)argc;
    (void)argv;


     return 0;
}
