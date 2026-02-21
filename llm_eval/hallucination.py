class HallucinationEvaluator:
    def score(self, response: str) -> int:
        suspicious_phrases = [
            "according to a 2023 study",
            "research proves",
            "statistics show",
        ]

        for phrase in suspicious_phrases:
            if phrase in response.lower():
                return 3

        return 5