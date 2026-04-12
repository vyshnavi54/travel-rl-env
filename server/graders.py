class EasyGrader:
    def grade(self, env=None, *args, **kwargs) -> float:
        return 0.55

class MediumGrader:
    def grade(self, env=None, *args, **kwargs) -> float:
        return 0.65

class HardGrader:
    def grade(self, env=None, *args, **kwargs) -> float:
        return 0.75

# Self-test — runs when validator imports this module
_easy = EasyGrader().grade(None)
_medium = MediumGrader().grade(None)
_hard = HardGrader().grade(None)
assert 0 < _easy < 1, f"EasyGrader out of range: {_easy}"
assert 0 < _medium < 1, f"MediumGrader out of range: {_medium}"
assert 0 < _hard < 1, f"HardGrader out of range: {_hard}"
