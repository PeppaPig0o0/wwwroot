from django.shortcuts import render, redirect, reverse
from django.conf import settings
from django.http import HttpResponseRedirect

# def image(request):
#     img_path = 'image/a.jpg'
#     data = {
#         'img_path': img_path
#     }
#     return render(request, "image.html", context=data)


import os
def image(request):
    image_dir = os.path.join(settings.BASE_DIR, 'static', 'image')
    images = []
    for filename in os.listdir(image_dir):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            images.append(filename)
    context = {'images': images}
    return render(request, 'image.html', context)



def upload_image(request):
    if request.method == 'POST':
        file = request.FILES['file']  # 获取上传的文件对象

        # 生成文件的保存路径file.name
        file_path = os.path.join(settings.BASE_DIR, 'static', 'image', file.name)

        # 将文件保存到服务器上
        with open(file_path, 'wb') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        print(reverse('drf:image'))
        return HttpResponseRedirect(reverse('drf:image'))

    return HttpResponseRedirect(reverse('drf:image'))


def delete_image(request, image_path):
    # 构建完整的图片路径
    full_path = os.path.join(settings.BASE_DIR, 'static', 'image', image_path)

    # 判断图片是否存在并删除
    if os.path.exists(full_path):
        os.remove(full_path)

    return HttpResponseRedirect(reverse('drf:image'))


