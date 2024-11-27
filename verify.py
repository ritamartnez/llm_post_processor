from wikipediaapi import Wikipedia

def verify_answer(answer, expected_fact):
    wiki = Wikipedia('en')
    page = wiki.page(answer)
    if page.exists():
        return "correct" if expected_fact.lower() in page.text.lower() else "incorrect"
    return "verification failed"

# Example usage
print("Verification Result:", verify_answer("Managua", "capital of Nicaragua"))