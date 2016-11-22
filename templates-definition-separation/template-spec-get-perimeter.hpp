#ifndef TEMPLATE_SPEC_GET_PERIMETER_HPP
#define TEMPLATE_SPEC_GET_PERIMETER_HPP

template<typename T>
T Rectangle<T>::Get_Perimeter()
{
  return 2*m_Width+2*m_Height;
}
#endif // TEMPLATE_SPEC_GET_PERIMETER_HPP
