from django.shortcuts import render
import requests

from .forms import LangForm

key = ''
catalog = ''
def translate(request):
    # IAM_TOKEN = key
    # folder_id = catalog
    #
    # body = {
    #     "folderId": folder_id,
    # }
    #
    # headers = {
    #     "Content-Type": "application/json",
    #     "Authorization": "Bearer {0}".format(IAM_TOKEN)
    # }
    #
    # response = requests.post('https://translate.api.cloud.yandex.net/translate/v2/languages',
    #     json=body,
    #     headers=headers
    # ).json()
    # total = response['languages']
    # langs = []
    # for i in total:
    #     t=i['code']
    #     langs.append(t)
    langs = ['ru', 'en', 'po']

    if request.method == 'GET':
        form = LangForm(initial={'word': 111})
        form.fields['langs'].choices = [('ru', 'ru'), ('en', 'en'), ('po', 'po')]
        # print(form['langs'])
        context = {
            "form": form
         }
        return render(request=request, template_name='translate/tr.html', context=context)
    if request.method == 'POST':
        target_language = request.POST.get('from_translate')
        texts = request.POST.get('lang')

        body = {
            "targetLanguageCode": target_language,
            "texts": texts,
            "folderId": folder_id,
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer {0}".format(IAM_TOKEN)
        }

        response = requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate',
            json=body,
            headers=headers
        ).json()
        cur = response['translations']
        total = []
        for i in cur:
            t = i.get('text')
            total.append(t)
        all = ' '.join(total)

        context = {
            'from_translate': target_language,
            'texts': texts,
            "all": all,
            "langs": langs

         }

        return render(request=request, template_name='translate/index.html', context=context)
