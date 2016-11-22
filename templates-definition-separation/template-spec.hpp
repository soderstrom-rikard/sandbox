// https://isocpp.org/wiki/faq/templates#templates-defn-vs-decl
#ifndef TEMPLATE_SPEC_HPP
#define TEMPLATE_SPEC_HPP

template<typename T>
class Rectangle
{
public:
  void Set_Height(T a_Height);
  void Set_Width (T a_Width );

  T Get_Area();
  T Get_Perimeter();

private:
  T m_Height;
  T m_Width;
};

// Templates Declaration and Definition separation
#include "template-spec-get-area.hpp"
#include "template-spec-get-perimeter.hpp"
#include "template-spec-set-height.hpp"
#include "template-spec-set-width.hpp"


#endif // TEMPLATE_SPEC_HPP
