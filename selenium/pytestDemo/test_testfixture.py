import pytest




def test_bank(setup):
    print("i'm inside the bank")

def test_bank2(setup):
    print("I'm again inside bank")

# if above is the case where we need to pass the fixture(setup) so go with class implementation where for each function it will call fixture
# but if we apply scope then it will execute based on scope
# class name also should prefixed with Test
@pytest.mark.usefixtures("setup")
class TestExample:

    def test_banka(self):
        print("im inside banka")

    def test_bankb(self):
        print("im inside bankb")
