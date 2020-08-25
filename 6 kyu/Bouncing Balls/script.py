def bouncing_ball(h, bounce, window):
    if not (h > 0 and bounce > 0 and bounce < 1 and window < h):
        return -1
    else:
        time = 1
        h = h * bounce
        while h > window:
            h = h * bounce
            time += 2
    return time
