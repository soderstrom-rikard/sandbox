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
static size_t     match_index = 0u;
static string_vec matches;
static string_vec vocabulary;
static char *     line = nullptr;

char* completion_generator(const char* text, int state)
{
    // This function is called with state=0 the first time; subsequent calls are
    // with a nonzero state. state=0 can be used to perform one-time
    // initialization for this completion session.

    if (state == 0)
    {
        // During initialization, compute the actual matches for 'text' and keep
        // them in a static vector.
        matches.clear();
        match_index = 0;

        // Collect a vector of matches: vocabulary words that begin with text.
        std::string textstr = std::string(text);
        for (auto word : vocabulary)
        {
            if (word.size() >= textstr.size() && word.compare(0, textstr.size(), textstr) == 0)
            {
                matches.push_back(word);
            }
        }
    }

    if (match_index >= matches.size())
    {
        // We return nullptr to notify the caller no more matches are available.
        return nullptr;
    }
    else
    {
        // Return a malloc'd char* for the match. The caller frees it.
        return strdup(matches[match_index++].c_str());
    }
}

char** completer(const char* text, int start, int end)
{
    (void)text;
    (void)start;
    (void)end;

    // Note: returning nullptr here will make readline use the default filename
    // completer.
    return rl_completion_matches(text, completion_generator);
    //return nullptr;
}
} //namespace: anonymous

void initialize()
{
    vocabulary.push_back("info" );
    vocabulary.push_back("read" );
    vocabulary.push_back("write");

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
