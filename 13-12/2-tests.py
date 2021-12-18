import molecules as ml

class TestPow:
    def test_molecules_0(self):
        assert ml.molecules(0, 0, 0) == 0

    def test_molecules_1(self):
        assert ml.molecules(1, 1, 1) == 0

    def test_molecules_c_2(self):
        assert ml.molecules(2, 20, 20) == 1

    def test_molecules_h_6(self):
        assert ml.molecules(20, 6, 20) == 1

    def test_molecules_o_1(self):
        assert ml.molecules(20, 20, 1) == 1