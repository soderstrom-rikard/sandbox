def bits_per_symbol(size):
  return len(bin(size + size%2)[2:]) - 1

def compress(uncompressed, dictionary):
    """Compress a bitstring to a list of output symbols."""

    # Build the dictionary.
    dict_size = len(dictionary)
    bps = bits_per_symbol(dict_size)

    if len(uncompressed)%bps != 0:
        raise ValueError('Input data cannot be compressed with current dictionary')

    w = ""
    result = []
    print('Current\tNext byte\tOutput\tExtended dictionary')
    for i in range(0,len(uncompressed),bps):
        c = uncompressed[i:i+bps]
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            # Add wc to the dictionary.
            dictionary[wc] = dict_size
            dict_size += 1

            # Current, next byte, output, extended dictionary
            print ('%s\t%s\t\t%s\t%d %s' %(w,c,dictionary[w],dict_size,wc))

            w = c

        #print ('c = %s' % (c))

    # Output the code for w.
    if w:
        result.append(dictionary[w])
        print ('%s\t%s\t\t%s' %(w,c,dictionary[w]))

    print ('dict=',dictionary)
    return result




def decompress(compressed, dictionary):
    """Decompress a list of output ks to a string."""

    # Build the dictionary.
    dict_size = len(dictionary)
    bits_per_symbol = len(bin(dict_size + dict_size%2)[2:]) - 1

    if len(uncompressed)%bits_per_symbol != 0:
        raise ValueError('Input data cannot be compressed with current dictionary')

    result = []
    w = compressed.pop(0)
    result.append(w)
    for k in compressed:
        if k in dictionary:
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
    return result


# How to use:
dictionary = { bin(i)[2:].rjust(2,'0'): i for i in range(4) }
print ('dict=',dictionary)
compressed = compress('000110110001101100010010', dictionary)
print (compressed)
#decompressed = decompress(compressed, dictionary)
#print (decompressed)

