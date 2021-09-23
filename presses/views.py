from django.shortcuts import render
from .forms import Press
from .user_functions import get_user_tweets, get_user_info, get_img_20min

# Create your views here.
def press_view(request):
    if request.method == 'POST':
        form = Press(request.POST)
        if form.is_valid():
            presse = form.cleaned_data['choice_press']
            context_info = get_user_info(presse)
            context_tweets = get_user_tweets(presse)
     
            return render(request,'presses_headlines.html',{'Info':context_info, 'Tweets':context_tweets})
    else:
        form = Press()

    return render(request, 'presses_forms.html', {'form': form })
