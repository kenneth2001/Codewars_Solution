def de_nico(key,msg):
    
    pw = [sorted(key).index(c) for c in key]
    key_length = len(key)
    decode = ""

    while msg:
        decode += ''.join(msg[i] for i in pw if i < len(msg))
        msg = msg[key_length:]
    return decode.rstrip(" ")
