from llm_eval.evaluator import LLMEvaluationEngine


def main():
    engine = LLMEvaluationEngine()

    print("Enter LLM response to evaluate:")
    response = input("> ")

    results = engine.evaluate(response)

    print("\nEvaluation Results:")
    for key, value in results.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()