#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <memory>
#include <string>
#include <vector>

namespace cmdline
{
/* shielding (us from) inclusions */
#include <readline/readline.h>
#include <readline/history.h>

using string_vec = std::vector<std::string>;

namespace /* anonymous */
{
static char *     line = nullptr;
static const string_vec commands{
    "info-all",
    "info-allocations",
    "info-memory-usage",
    "read-memory-area",
    "read-single-byte",
    "write-memory-area",
    "write-single-byte"
    };


char** completer(const char* text, int start, int end)
{
    (void)start;
    (void)end;
    // Don't do filename completion even if our generator finds no matches.
    rl_attempted_completion_over = 1;

    // Fill matches with all words from commands that begins with `text`.
    std::string textstr(text);
    string_vec matches;
    std::copy_if(commands.begin(), commands.end(), std::back_inserter(matches),
        [&textstr](const std::string& s)
        {
            return (s.size() >= textstr.size() && s.compare(0, textstr.size(),textstr) == 0);
        });

    if (matches.empty()) return nullptr;

    char** array = static_cast<char**>(malloc((2 + matches.size()) * sizeof(*array)));

    size_t pos = 1;
    std::string longest_common_prefix(matches.back());
    for (const auto& m : matches)
    {
        array[pos++] = strdup(m.c_str());

        // find longest longest_common_prefix with m.
        size_t i=0u;
        for(; i < std::min(longest_common_prefix.size(),m.size()); i++)
        {
            if (longest_common_prefix[i] != m[i]) break;
        }
        longest_common_prefix = longest_common_prefix.substr(0,i);

    }

    array[0] = strdup(longest_common_prefix.c_str());

    array[pos] = nullptr;
    return array;
}
} //namespace: anonymous

void initialize()
{
    // bindings
    rl_attempted_completion_function = completer;
}

int run()
{
    printf("Welcome! You can exit by pressing Ctrl+D at any time...\n");

    while ((line = readline(">> ")) != nullptr)
    {
        if (strlen(line) > 0)
        {
            add_history(line);
        }

        printf("[%s]\n", line);

        // readline malloc's a new buffer every time.
        free(line);
    }
    return 0;
}

} //namespace: cmdline


int main (int argc, char *argv[])
{
    (void)argc;
    (void)argv;

    cmdline::initialize();

    return cmdline::run();
}
