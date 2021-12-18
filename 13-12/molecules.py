def molecules(c, h, o):
    c_max = c // 2
    h_max = h // 6
    o_max = o

    molecule_max = c_max
    if (molecule_max > h_max):
        molecule_max = h_max
    if (molecule_max > o_max):
        molecule_max = o_max

    return molecule_max
