def get_hiragana_data():
    phonemes = {
    "consonants": "kstnhmrwy",
    "vowels": "aiueo"
    }
    conversion_table = get_hiragana_table()
    return {"phonemes": phonemes, "table": conversion_table}
    
def get_hiragana_table():
    hiragana = {}
    with open("hiragana/hiragana.csv", "r", encoding='utf-8') as f:
        lines = f.read().split(" ")
        for line in lines:
            romaji, kana = line.split(",")
            hiragana.update({romaji: kana})
    return hiragana