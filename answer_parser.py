import re

def extract_answer(text):
    # For yes/no answers, search for keywords
    yes_no_patterns = [r'\b(yes|no)\b', r'\b(correct|incorrect)\b']
    for pattern in yes_no_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group().lower()
    # For specific entity answers, assume the entity extraction module helps extract the main answer
    return "Entity-based answer"

# Example usage
llm_response = "Yes, Managua is the capital city of Nicaragua."
print("Extracted Answer:", extract_answer(llm_response))