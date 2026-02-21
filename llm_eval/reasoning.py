import re

class ReasoningEvaluator:
    def score(self, response: str) -> int:
        score = 5

        if "because" not in response.lower() and "therefore" not in response.lower():
            score -= 1

        contradiction_patterns = [
            r"but at the same time",
            r"however.*therefore",
        ]

        for pattern in contradiction_patterns:
            if re.search(pattern, response.lower()):
                score -= 2

        return max(score, 0)