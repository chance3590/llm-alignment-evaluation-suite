from llm_eval.reasoning import ReasoningEvaluator
from llm_eval.hallucination import HallucinationEvaluator
from llm_eval.safety import SafetyEvaluator
from llm_eval.bias import BiasEvaluator
from llm_eval.reward_model import RewardModel


class LLMEvaluationEngine:

    def __init__(self):
        self.reasoning = ReasoningEvaluator()
        self.hallucination = HallucinationEvaluator()
        self.safety = SafetyEvaluator()
        self.bias = BiasEvaluator()
        self.reward_model = RewardModel()

    def evaluate(self, response: str) -> dict:
        reasoning_score = self.reasoning.score(response)
        hallucination_score = self.hallucination.score(response)
        safety_score = self.safety.score(response)
        bias_score = self.bias.score(response)

        reward = self.reward_model.compute(
            reasoning_score,
            hallucination_score,
            safety_score,
            bias_score,
        )

        return {
            "reasoning": reasoning_score,
            "hallucination": hallucination_score,
            "safety": safety_score,
            "bias": bias_score,
            "reward_score": round(reward, 2),
        }