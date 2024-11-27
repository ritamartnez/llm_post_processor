
from entity_extractor import extract_entities, map_to_wikipedia
from answer_parser import extract_answer
from verify import verify_answer
from utils import query_llm

def main():
    input_text = input("Enter your question: ")
    raw_output = query_llm(input_text)
    print("Raw LLM Output:", raw_output)

    entities = extract_entities(raw_output)
    print("Entities Extracted:", entities)

    wiki_links = map_to_wikipedia(entities)
    print("Mapped Wikipedia Links:", wiki_links)

    answer = extract_answer(raw_output)
    print("Extracted Answer:", answer)

    verification_result = verify_answer(answer, "Managua")
    print("Verification Result:", verification_result)

if __name__ == "__main__":
    main()