class RewardModel:
    def compute(self, reasoning: int, hallucination: int, safety: int, bias: int) -> float:
        return (
            0.35 * reasoning
            + 0.25 * hallucination
            + 0.25 * safety
            + 0.15 * bias
        )