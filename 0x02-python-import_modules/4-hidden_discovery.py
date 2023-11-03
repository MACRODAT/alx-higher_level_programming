#!/usr/bin/python3

if __name__ == "__main__":
    """someklj"""
    import hidden_4

    nn = dir(hidden_4)
    for name in nn:
        if name[:2] != "__":
            print(name)
