def get_num_words(words_list):
    return len(words_list)


def sort_on(text):
    return text["num"]

def count_xters(texts):
    letters_dict = {}
    for i in range(0, len(texts)):
        lower_text = texts[i].lower()
        if lower_text in letters_dict:
            letters_dict[lower_text] += 1
        else:
            letters_dict[lower_text] = 1
    return letters_dict


def dict_list(bulk_texts):

    dict_word = count_xters(bulk_texts)
    dict_keys = list(dict_word.keys())
    key_list = []
    dict_list = []
    dict_piece = {}
    for key in dict_keys:
        if key.isalpha():
            dict_piece = {"char": "", "num": 0}
            alpha_key = key
            dict_piece["char"] = alpha_key
            dict_piece["num"] = dict_word[alpha_key]
            dict_list.append(dict_piece)
            dict_list.sort(reverse=True,key=sort_on)
    return dict_list
