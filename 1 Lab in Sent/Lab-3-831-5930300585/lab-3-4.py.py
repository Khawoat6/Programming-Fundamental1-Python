def range_product(to, start_at = 1):
    if to > start_at:
        return to * range_product(to-1, start_at)
    elif to == start_at:
        return 1 * to
    else:
        return None
