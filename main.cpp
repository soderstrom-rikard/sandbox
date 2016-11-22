#include <iostream>
#include <limits>
#include <string>

enum class             event_tag       { ENTER_SECURE_MODE , LEAVE_SECURE_MODE , NUMBER_OF_EVENTS};
constexpr const char * event_names[] = {"ENTER_SECURE_MODE","LEAVE_SECURE_MODE", "UNKNOWN"};

enum class             state_tag       { SECURE_MODE , OPEN_MODE , NUMBER_OF_STATES};
constexpr const char * state_names[] = {"SECURE_MODE","OPEN_MODE","UNKNOWN"};

const std::string event_name(event_tag event)
{
    if (event <= event_tag::NUMBER_OF_EVENTS)
        return event_names[static_cast<size_t>(event)];
    else
        return event_names[static_cast<size_t>(event_tag::NUMBER_OF_EVENTS)];
}

const std::string state_name(state_tag state)
{
    if (state <= state_tag::NUMBER_OF_STATES)
        return state_names[static_cast<size_t>(state)];
    else
        return state_names[static_cast<size_t>(state_tag::NUMBER_OF_STATES)];
}

struct state;
typedef void (*action_fn)(state *state, event_tag event);
struct state
{
    state_tag tag;
    action_fn action[static_cast<size_t>(event_tag::NUMBER_OF_EVENTS)];
};

namespace transitions
{
  void invalid(state *state, event_tag event)
  {
      // P_FATAL !!
      std::cout << "error - " << state_name(state->tag) << ", " << event_name(event) << "\n";
  }

  void open(state *state, event_tag event)
  {
      std::cout << "open - " << state_name(state->tag) << ", " << event_name(event) << "\n";
      state->tag = state_tag::OPEN_MODE;
  }

  void secure(state *state, event_tag event)
  {
      std::cout << "secure - " << state_name(state->tag) << ", " << event_name(event) << "\n";
      state->tag = state_tag::SECURE_MODE;
  }

} // ns: transitions


state sm[] =
{
    // state                      ->SECURE_MODE        ->OPEN_MODE
    { state_tag::SECURE_MODE, {  transitions::invalid, transitions::open   }},
    { state_tag::OPEN_MODE  , {  transitions::secure , transitions::invalid}}
};

void handle_event(state * state, event_tag event)
{
      if ((event >= event_tag::NUMBER_OF_EVENTS) || (state->tag >= state_tag::NUMBER_OF_STATES))
          transitions::invalid(state, event);
      else
          sm[static_cast<size_t>(state->tag)] .action[static_cast<size_t>(event)](state, event);
}

int main (int, char *[])
{

    state st;
    st.tag    = state_tag::OPEN_MODE;
    st.action[0] = transitions::secure;
    st.action[1] = transitions::open;

    std::cout << "Start\n";

    handle_event(&st, event_tag::ENTER_SECURE_MODE);
    handle_event(&st, event_tag::ENTER_SECURE_MODE);

    handle_event(&st, event_tag::LEAVE_SECURE_MODE);
    handle_event(&st, event_tag::LEAVE_SECURE_MODE);

     return 0;
}
