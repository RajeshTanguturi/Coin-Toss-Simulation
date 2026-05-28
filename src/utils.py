def get_powers_2(num: int):
    """Finds lower, upper, and nearest powers of 2 using binary bitwise shifts."""
    if num <= 0:
        return 1, 1, 1
        
    # Find how many binary digits the number has
    bits = num.bit_length()
    
    # 1 shifted left by (bits-1) gives the power of 2 just below/equal
    lower = 1 << (bits - 1)
    
    # If the number wasn't already a perfect power of 2, 
    # 1 shifted left by 'bits' gives the power of 2 just above
    upper = 1 << bits if lower != num else lower
    
    # Find the absolute nearest
    nearest = lower if (num - lower) < (upper - num) else upper
    
    return lower, upper, nearest