import logging

from reader import txt_reader

logging.basicConfig(level=logging.INFO)


def char_frequency(path : str) -> dict:
    try:
        text = txt_reader(path)
        frequency = {}
        count = 0
        for i in text:
            count += 1
            if i in frequency:
                frequency[i] += 1
            else:
                frequency[i] = 1
        frequency = sorted(frequency.items(), key=lambda item : item[1], reverse=True)
        return frequency
    except Exception as exc:
            logging.error(f"Frequency analisys error: {exc}")