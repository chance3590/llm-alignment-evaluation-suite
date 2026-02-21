class PromptInjectionDetector:
    def detect(self, prompt: str) -> bool:
        injection_phrases = [
            "ignore previous instructions",
            "override the system",
            "disregard policy",
        ]

        for phrase in injection_phrases:
            if phrase in prompt.lower():
                return True

        return False