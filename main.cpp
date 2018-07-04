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


// abstract
typedef struct state_i* state_i_ptr;

typedef void (*evt_enter_secure_mode_fk)(state_i_ptr);
typedef void (*evt_leave_secure_mode_fk)(state_i_ptr);

struct state_i
{
    evt_enter_secure_mode_fk secure;
    evt_leave_secure_mode_fk open;
#if 1
    std::string name;
#endif
};

// concrete defaults
void default_impl(state_i_ptr state);

static void default_secure(state_i_ptr)
{
    /* Event not supported in concrete state */
    std::cout << "secure (default)\n";
}

static void default_open(state_i_ptr)
{
    /* Event not supported in concrete state */
    std::cout << "open (default)\n";
}

void default_impl(state_i_ptr state)
{
    state->secure = default_secure;
    state->open   = default_open;
}

// Interface of concrete state

void tranistion_to_secure(state_i_ptr state);
void transition_to_open  (state_i_ptr state);

static void secure_mode_evt(state_i_ptr state)
{
    tranistion_to_secure(state);
}

void tranistion_to_secure(state_i_ptr state)
{
    default_impl(state);
    state->secure = secure_mode_evt;
    state->name   = "secure mode";

    std::cout << "secure\n";
}

static void open_mode_evt(state_i_ptr state)
{
    transition_to_open(state);
}

void transition_to_open(state_i_ptr state)
{
    default_impl(state);
    state->open = open_mode_evt;
    state->name = "open mode";

    std::cout << "open\n";
}

struct operation_mode
{
    state_i state;
    // data
};


int main (int, char *[])
{

    // Table based state machine
    state st;
    st.tag    = state_tag::OPEN_MODE;
    st.action[0] = transitions::secure;
    st.action[1] = transitions::open;

    std::cout << "Start table based state machine\n";

    handle_event(&st, event_tag::ENTER_SECURE_MODE);
    handle_event(&st, event_tag::ENTER_SECURE_MODE);

    handle_event(&st, event_tag::LEAVE_SECURE_MODE);
    handle_event(&st, event_tag::LEAVE_SECURE_MODE);
    std::cout << "End Table-based state machine\n";


    // State pattern based state machine
    operation_mode op;
    transition_to_open(&op.state);

    std::cout << "Start state pattern\n";
    secure_mode_evt(&op.state);
    open_mode_evt(&op.state);
    std::cout << "End state pattern\n";

     return 0;
}
