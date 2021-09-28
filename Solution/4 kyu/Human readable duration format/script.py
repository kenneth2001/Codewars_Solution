def format_duration(seconds):
    if seconds == 0: return "now"
    time = {"year":0, "day":0, "hour":0, "minute":0, "second":0}
    time["year"] = seconds // (3600*24*365)
    time["day"] = (seconds % (3600*24*365))//(3600*24)
    time["hour"] = (seconds % (3600*24)) // 3600
    time["minute"] = (seconds % 3600) // 60
    time["second"] = seconds % 60
    
    nonzero = len(time.values()) - list(time.values()).count(0)
    ans = ""
    
    for key, val in time.items():
        if val == 0: continue
        ans += str(val) + " " + key + ("s" if val > 1 else "")
        ans += ", " if nonzero > 2 else ""
        ans += " and " if nonzero == 2 else ""
        nonzero -= 1
    return ans