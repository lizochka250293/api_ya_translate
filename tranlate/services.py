import requests

from .config import folder_id, API_KEY

body = {
    "folderId": folder_id,
}

headers = {
    "Content-Type": "application/json",
    "Authorization": "Api-Key {0}".format(API_KEY)
}


def get_languages():
    """Получение всех языков для перевода"""
    response = requests.post('https://translate.api.cloud.yandex.net/translate/v2/languages',
        json=body,
        headers=headers
        ).json()
    languages = response['languages']
    languages_list = []
    for language in languages:
        lang = language['code']
        languages_list.append(lang)
    return languages_list


def get_current_text(target_language, texts):
    """Получение перевода"""
    body = {
        "targetLanguageCode": target_language,
        "texts": texts,
        "folderId": folder_id,
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Api-Key {0}".format(API_KEY)
    }

    response = requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate',
                             json=body,
                             headers=headers
                             ).json()
    current_text = response['translations']
    texts_list = []
    for text in current_text:
        current_word = text.get('text')
        texts_list.append(current_word)
    total_str = ' '.join(texts_list)
    return total_str