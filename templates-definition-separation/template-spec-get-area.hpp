#ifndef TEMPLATE_SPEC_GET_AREA_HPP
#define TEMPLATE_SPEC_GET_AREA_HPP

template<typename T>
T Rectangle<T>::Get_Area()
{
  return m_Width*m_Height;
}

#endif // TEMPLATE_SPEC_GET_AREA_HPP
