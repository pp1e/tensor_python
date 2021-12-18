import quad_equation as qe

class TestPow:
    def test_molecules_0(self):
        assert qe.quad_eq(1, 4, 3) == (-1, -3) 

    def test_molecules_1(self):
        assert qe.quad_eq(1, 0, -16) == (4, -4)

    def test_molecules_c_2(self):
        assert qe.quad_eq(0, 2, -4) == 2

    def test_molecules_h_6(self):
        assert qe.quad_eq(0, 0, 0) == 'No roots'

    def test_molecules_o_1(self):
        assert qe.quad_eq(2, 1, 2) == 'No roots'