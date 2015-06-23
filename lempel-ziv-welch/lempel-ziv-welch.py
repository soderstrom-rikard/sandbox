def compress(uncompressed, dictionary):
    """Compress a string to a list of output symbols."""

    # Build the dictionary.
    dict_size = len(dictionary)

    w = ""
    result = []
    for c in uncompressed:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            # Add wc to the dictionary.
            dictionary[wc] = dict_size
            dict_size += 1
            w = c

        print ('c=%d, w=%8s, result=%s' % (ord(c),list(w).__str__(),result))

    print ('dict=',dictionary)
    # Output the code for w.
    if w:
        result.append(dictionary[w])
    return result




def decompress(compressed, dictionary):
    """Decompress a list of output ks to a string."""

    # Build the dictionary.
    dict_size = len(dictionary)

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
dictionary = {chr(i): chr(i) for i in range(4)}
print ('dict=',dictionary)
compressed = compress('\0\1\2\3\0\1\2\3\0\1\0\2', dictionary)
print (compressed)
#decompressed = decompress(compressed, dictionary)
#print (decompressed)
