from django.shortcuts import render

# Create your views here.
from .models import Img
import qrcode


# 图片上传
def uploadImg(request):
    if request.method == 'POST':
        files = request.FILES.getlist('img')
        for f in files:
            img = Img(img_url=f)
            save = img.save()
            print(img)

    return render(request, 'polls/imgUpload.html')
