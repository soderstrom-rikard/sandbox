def compress(uncompressed):
    """Compress a string to a list of output symbols."""

    # Build the dictionary.
    dict_size = 256
    dictionary = {chr(i): chr(i) for i in range(dict_size)}

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

    # Output the code for w.
    if w:
        result.append(dictionary[w])
    return result




def decompress(compressed):
    """Decompress a list of output ks to a string."""

    # Build the dictionary.
    dict_size = 256
    dictionary = {chr(i): chr(i) for i in range(dict_size)}

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
compressed = compress('\0\1\2\3\0\1\2\3\0\1\0\2')
print (compressed)
decompressed = decompress(compressed)
print (decompressed)
