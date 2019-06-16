#ifndef __ELEMENTS_H__
#define __ELEMENTS_H__

#include <cstdint>
#include <string_view>

struct element_t
{
    enum class phase_t
    {
        unknown,
        gas,
        solid,
        liquid,
        plasma
    }; // enum class phase_t

    enum class category_t
    {
        unknown, // unknown chemical properties
        actinide,
        alkali_metal,
        alkaline_earth_metal,
        lanthanide,
        metalloid,
        noble_gas,
        post_transition_metal,
        reactive_nonmetal,
        transition_metal
    }; // enum class - category_t

    enum class natural_t
    {
        primordial, // Existed before earth was formed
        from_decay, // Trace radioisotope, radioisotope that exists naturally in trace amounts
        synthetic,  // Artificially created element
    }; // enum class - natural_t

    const uint32_t    atomic_number;
    const std::string_view symbol;
    const std::string_view name;
    const double      atomic_weight;
    const phase_t     phase;
    const category_t  category;
    const natural_t   occurrence;
}; // struct - element_t

#endif // __ELEMENTS_H__
