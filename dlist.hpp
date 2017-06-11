#ifndef __DLIST_HPP__
#define __DLIST_HPP__

class Dlist;
class Dnode {
  friend class Dlist;

public:
  Dnode() : m_Next(static_cast<Dnode*>(0)), m_Prev(m_Next) {}

private:
  Dnode* m_Next;
  Dnode* m_Prev;
};

class Dlist {
public:
  Dlist(const unsigned int a_Capacity) : m_Capacity(a_Capacity), m_Size(0), m_Front(static_cast<Dnode*>(0)), m_Back(m_Front) {}

  unsigned int Size()     { return m_Size;              }
  bool         Is_Empty() { return m_Size == 0;         }
  bool         Is_Full()  { return m_Size == m_Capacity;}

  Dnode* Front()            { return m_Front;   }
  Dnode* Back()             { return m_Back;    }
  Dnode* Get_Prev(Dnode* v) { return v->m_Prev; } // User need to verify that v != prev
  Dnode* Get_Next(Dnode* v) { return v->m_Next; } // User need to verify that v != next

  Dnode* Pop_Back() {
    if (m_Size == 0) return static_cast<Dnode*>(0);

    Dnode *v       = m_Back;
    m_Back         = m_Back->m_Next;
    m_Back->m_Prev = static_cast<Dnode*>(0);
    v->m_Next      = static_cast<Dnode*>(0);
    m_Size--;

    return v;
  }

  Dnode* Pop_Front() {
    if (m_Size == 0) return static_cast<Dnode*>(0);

    Dnode *v        = m_Front;
    m_Front         = m_Front->m_Prev;
    m_Front->m_Next = static_cast<Dnode*>(0);
    v->m_Prev       = static_cast<Dnode*>(0);
    m_Size--;

    return v;
  }


  bool Push_Back(Dnode *v) {
    if (Is_Full()) return false;

    if (Is_Empty()) {
      m_Back    = v;
      m_Front   = v;
      v->m_Prev = static_cast<Dnode*>(0);
      v->m_Next = static_cast<Dnode*>(0);
    } else {
      m_Back->m_Prev  = v;
      v->m_Prev       = static_cast<Dnode*>(0); // TODO: What to do if v already in a list?
      v->m_Next       = m_Back;
      m_Back          = v;
    }
    m_Size++;

    return true;
  }

  bool Push_Front(Dnode *v) {
    if (Is_Full()) return false;

    if (Is_Empty()) {
      m_Back    = v;
      m_Front   = v;
      v->m_Prev = static_cast<Dnode*>(0);
      v->m_Next = static_cast<Dnode*>(0);
    } else {
      m_Front->m_Next = v;
      v->m_Prev       = m_Front;
      v->m_Next       = static_cast<Dnode*>(0); // TODO: What to do if v already in a list?
      m_Front         = v;
    }
    m_Size++;

    return true;
  }

private:
  const unsigned int m_Capacity;
  unsigned int m_Size;
  Dnode* m_Front; // header
  Dnode* m_Back ; // trailer
};

#endif // __DLIST_HPP__
