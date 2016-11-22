// https://isocpp.org/wiki/faq/templates#templates-defn-vs-decl
#include <cstdint>
#include <iostream>
#include "template-spec.hpp"

template<typename T>
void Dump(Rectangle<T>& R)
{
  std::cout << "Area: "        << R.Get_Area();
  std::cout << ", Perimeter: " << R.Get_Perimeter();
  std::cout << std::endl;
}

int main (int argc, char *argv[])
{
  Rectangle<uint32_t> Unsigned_Rect;
  Unsigned_Rect.Set_Width(10u);
  Unsigned_Rect.Set_Height(20u);
  Dump(Unsigned_Rect);

  Rectangle<double>   Real_Rect;
  Real_Rect.Set_Width(1.7);
  Real_Rect.Set_Height(3.4);
  Dump(Real_Rect);

  return 0;
}
