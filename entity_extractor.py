import spacy
from wikipediaapi import Wikipedia

# Load the spaCy language model (download with `python -m spacy download en_core_web_sm`)
nlp = spacy.load('en_core_web_sm')

def extract_entities(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

def map_to_wikipedia(entity_list):
    wiki = Wikipedia('en') #cange to own wikipediapi string
    mapped_entities = {}
    for entity in entity_list:
        page = wiki.page(entity[0])
        if page.exists():
            mapped_entities[entity[0]] = page.fullurl
    return mapped_entities

# Example usage
example_text = "Yes, Managua is the capital city of Nicaragua."
entities = extract_entities(example_text)
print("Entities:", entities)
print("Wikipedia Links:", map_to_wikipedia(entities))