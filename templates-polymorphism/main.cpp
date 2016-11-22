// https://isocpp.org/wiki/faq/templates#templates-defn-vs-decl
// Example for this use case is extremly overcomplicated, its purpose
// is only to demonstrate how to subclass templates that have members/classes
// that doesn't depend on the template type
#include <cstdint>
#include <iostream>
#include <map>
#include <list>

template<typename T>
class Material { public: void Dump(T a_T) { std::cout << a_T << std::endl; }};

template<typename T>
class Building : public Material<T>
{
public:
  class Property
  {
  public:
    uint64_t Get_Size(void           ) { return m_Size;   }
    void     Set_Size(uint64_t a_Size) { m_Size = a_Size; }
  private:
    uint64_t m_Size;
  };

  Building() : Properties() {}
  std::list<Property> Properties;
};

template<typename T>
class Appartment: public Building<T>
{
typedef Building<T> BT;
public:
  void Add(uint64_t Val)
  {
    BT::Properties.push_back(typename BT::Property());
    BT::Properties.back().Set_Size(Val);
  }

  void Dump_Properties()
  {
    for(typename std::list<typename BT::Property>::iterator it=BT::Properties.begin(); it!=BT::Properties.end(); it++)
    {
      T Value = static_cast<T>(it->Get_Size());
      BT::Dump(Value);
    }
  }
};


int main (int argc, char *argv[])
{
  // Initialize
  Appartment<uint32_t> Small;
  Appartment<uint64_t> Large;

  Small.Add(1u);
  Small.Add(2u);
  Small.Add(3u);

  Large.Add(1111u);
  Large.Add(2222u);
  Large.Add(3333u);

  Small.Dump_Properties();
  Large.Dump_Properties();

  return 0;
}
