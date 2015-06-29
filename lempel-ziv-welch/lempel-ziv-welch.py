class CodeBookElement:
  def __init__(self, start, length):
    self.start = start
    self.end = start + length

  def __add__(self,other):
    return CodeBookElement(self.start,self.end+other)

  def __eq__(self,other):
    if not isinstance(other,CodeBookElement):
      return False

    return (self.start == other.start) and (self.end == other.end)

  def __repr__(self):
    return '%s(%s:%s)' % (self.__class__, repr(self.start), repr(self.end))

  def __str__(self):
    return self.__repr__().split('.')[-1]

class CodeBook:
  def __init__(self, dictionary):
    self.initial = dictionary
    self.book = []

  def __contains__(self, item_data_tuple):
    item = item_data_tuple[0]
    data = item_data_tuple[1]

    print ("Checking code", str(item))

    if data[item.start:item.end] in self.initial:
      print "code in dict"
      return True

    for ecb in self.book:
      if data[item.start:item.end] == data[ecb.start:ecb.end]:
        print "code in book"
        return True

    print ("code not in book", str(item))
    return False

  def __len__(self):
    return len(self.initial)+len(self.book)

  def _str_or_repr(self, is_str=False):
    s = ''
    cbi = []
    cbe = []

    for key in self.initial:
      cbi.append(str(key).rjust(10) + ':' + str(self.initial[key]).rjust(5))
    for item in self.book:
      cbe.append(str(item))

    if is_str:
      s += '\nDictionary(\n'       + '\n'.join(cbi) + ')'
      s += '\nCodeBookElements(\n' + '\n'.join(cbe) + ')'
    else:
      s += 'Dictionary('       + ','.join(cbi) + '),'
      s += 'CodeBookElements(' + ','.join(cbe) + ')'

    return s

  def __repr__(self):
    return '%s(%s)' % (self.__class__, self._str_or_repr())

  def __str__(self):
    return '%s(%s)' % (str(self.__class__).split('.')[-1], self._str_or_repr(True))

  def append(self, item):
    self.book.append(item)

  def index_of(self, item, data):
    if item.start == item.end:
      print ('Item length is zero', item)
      return None

    if data[item.start:item.end] in self.initial:
      return self.initial[data[item.start:item.end]]

    for index,ecb in enumerate(self.book):
      if data[item.start:item.end] == data[ecb.start:ecb.end]:
        return len(self.initial)+index

    print ('Could not find', item)
    return None

class LZW:
  def __init__(self, codebook):
    self.cb  = codebook
    self.bpc = self.bits_per_code()

  def bits_per_code(self):
    size = len(self.cb)
    return len(bin(size + size%2)[2:]) - 1

  def compress(self, uncompressed):
    """Compress a bitstring to a list of output symbols."""

    # Build the dictionary.
    dict_size = len(self.cb)

    if len(uncompressed)%self.bpc != 0:
        raise ValueError('Input data cannot be compressed with current dictionary')

    w        = CodeBookElement(0,0)
    result   = []
    extended = []
    print [uncompressed[i:i+self.bpc] for i in range(0,len(uncompressed),self.bpc)]
    print('Current\t\t\tNext byte\tOutput\tExtended dictionary')
    for i in range(0,len(uncompressed),self.bpc):
        print ('i = %d' %(i))
        print str(w + self.bpc)
        if (w+self.bpc,uncompressed) in self.cb:
            w += self.bpc
        else:
            result.append(self.cb.index_of(w,uncompressed))
            # Add wc to the dictionary.
            self.cb.append(w+self.bpc)
            dict_size += 1

            # Current, next byte, output, extended dictionary
            #print ('%s\t%s\t\t%s\t%d %s' %(w,uncompressed[i:i+self.bpc],result[-1],dict_size,w))

            w = CodeBookElement(i-self.bpc,0)

        #print ('c = %s' % (c))

    # Output the code for w.
    if w:
        result.append(self.cb.index_of(w,uncompressed))
        print ('%s\t\t\t\t%s' %(w,result[-1]))

    print '\n' , self.cb
    return result

def decompress(compressed, dictionary):
    """Decompress a list of output ks to a string."""

    # Build the dictionary.
    dict_size = len(dictionary)

    result = []
    w = compressed.pop(0)
    result.append(w)
    i = o
    while i-self.bpc < len(uncompressed):
        k = compressed[i:i+self.bpc]
        if dictionary.has_key(k):
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError('Bad compressed k: %s' % k)
        result.append(entry)

        # Add w+entry[0] to the dictionary.
        dictionary[dict_size] = w + entry[0]
        dict_size += 1

        w = entry
        i += self.bpc
    return result


# How to use:
cb = CodeBook({ bin(i)[2:].rjust(2,'0'): i for i in range(4) })
lzw = LZW(cb)
print cb,'\n'
compressed = lzw.compress('000110110001101100010010')
print (compressed)
#decompressed = lzw.decompress(compressed)
#print (decompressed)

