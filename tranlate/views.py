from django.shortcuts import render

from .services import get_languages, get_current_text

api_key = 'AQVNzj8jRt0GwFNQIpGNCNFes_0F6FwGPtBL13r8'
catalog = 'b1g6ivmkutm3bjjtltku'


def translate(request):
    languages = get_languages
    if request.method == 'GET':
        context = {
            "langs": languages
         }
        return render(request=request, template_name='tranlate/index.html', context=context)
    if request.method == 'POST':
        target_language = request.POST.get('from_translate')
        texts = request.POST.get('lang')
        translated_text = get_current_text(target_language, texts)
        context = {
            'from_translate': target_language,
            'texts': texts,
            "all": translated_text,
            "langs": languages

         }
        return render(request=request, template_name='tranlate/index.html', context=context)
