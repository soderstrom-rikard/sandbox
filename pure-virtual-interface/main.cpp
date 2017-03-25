// Pure virtual interface example
#include <cstdint>
#include <map>
#include <list>

// Abstract class
// With pure virtual functions
// However, since the derived class contains a map (container)
// this abstract class needs a virtual destructor.
// Either as below or as `inline Base::~Base() {}` on separate row
// Otherwise the derived class destructor won't get called and we get
// a memory leak
class Base
{
public:
  virtual ~Base() {}                              // Virtual destructor
  virtual void Add(uint8_t Id, uint64_t Val) = 0; // Pure virtual function
};

// Concrete Class
class Derived: public Base
{
public:
  Derived() : m_Values() {}

  void Add(uint8_t Id, uint64_t Val) { m_Values[Id] = Val; }

private:
  std::map<uint8_t,uint64_t> m_Values;
};


int main (int argc, char *argv[])
{
  // Initialize
  std::list<Base *> v;

  // Allocate
  v.push_back(new Derived());
  v.back()->Add(1u, 2u);
  v.back()->Add(2u, 4u);
  v.back()->Add(3u, 8u);
  v.push_back(new Derived());
  v.back()->Add(10u, 1u);
  v.back()->Add(20u, 0u);

  for(std::list<Base *>::iterator it = v.begin(); it != v.end(); it++)
  {
    if (*it != static_cast<Base *>(0))
      delete *it;
  }

  return 0;
}
