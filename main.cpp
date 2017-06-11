#include "dlist.hpp"

struct Memo {
  Memo(): Data(), Is_Stored(false), Request_Id(-1) {}
  static const unsigned int SIZE = 1024;
  unsigned char Data[SIZE];
  bool Is_Stored;
  int Request_Id;
}; // Buffer_Segment

class Memo_Node: public Dnode {
public:
  Memo_Node(): m_Data(), Dnode() {}
  Memo& Get_Data() { return m_Data; }

private:
  Memo m_Data;
};

static const unsigned int NUMBER_OF_MEMOS = 50;
static Memo_Node Memo_List_Items[NUMBER_OF_MEMOS];

int main (int argc, char *argv[])
{
  Dlist Empty_Memos(NUMBER_OF_MEMOS);    // {1}
  Dlist Written_Memos(NUMBER_OF_MEMOS);  // {2]
  Dlist Queued_For_Storage_Memos(2);     // {3}

  // Fill Empty_Memos List with Memo_List_Items
  for(unsigned int i=0; i <NUMBER_OF_MEMOS; i++) {
    if (!Empty_Memos.Push_Back(&Memo_List_Items[i]))
      return -1; // Attempted to store more than list capacity
  }

  //   I: If memo is successfully stored release it (move from {3} to {1})

  // TODO: Implement iterator
  for(Memo_Node* it=static_cast<Memo_Node*>(Queued_For_Storage_Memos.Back()); it != static_cast<Memo_Node*>(Queued_For_Storage_Memos.Front()); it=static_cast<Memo_Node*>(Queued_For_Storage_Memos.Get_Next(it))) {
    Memo& memo = it->Get_Data();
    if (memo.Is_Stored) {
      //Empty_Memos.Push_Back(Queued_For_Storage_Memos.Remove(it));
      memo.Is_Stored = false;
    }
  }
  //  II: If current memo is full
  //    a: Place current memo as newest in {2}
  //    b: start a new memo (take any from {1}, if {1} is empty reuse oldest in {2})
  // III: If {3} not full, move oldest from {2} into {3}
  //  IV: Attempt to store oldest in {3} which isn't waiting to be stored

  // Cleanup
  return 0;
}
