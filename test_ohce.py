from ohce import Ohce

def test_reverses_input():
    ohce = Ohce()
    result = ohce.process("hello")
    assert result == "olleh"
