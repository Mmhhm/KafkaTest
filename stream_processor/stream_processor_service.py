


def find_hostile_words(script: list):
    hostile_sentences = {
        'explosive_sentences': [],
        'hostage_sentences': [],
        'fully_explosive': [],
        'is_hostile': False
    }
    for sentence in script:
        letters = sentence.replace(" ", "").lower()
        if 'hostage' in letters and 'explos' in letters:
            hostile_sentences['is_hostile'] = True
            hostile_sentences['fully_explosive'].append(sentence)
        elif 'hostage' in letters:
            hostile_sentences['is_hostile'] = True
            hostile_sentences['hostage_sentences'].append(sentence)
        elif 'explos' in letters:
            hostile_sentences['is_hostile'] = True
            hostile_sentences['explosive_sentences'].append(sentence)

    return hostile_sentences
            

# def order_script_by_hostility(sentences_dict: dict):
#     ordered = []
#     for k v in sentences_dict:

    




