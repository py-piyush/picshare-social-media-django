from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse, HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import ImageBookmarkForm, ImagePostForm, CommentForm
from .models import Image

# Create your views here.


@login_required
def image_post(request):
    if request.method == "POST":
        # print(request.user)
        form = ImagePostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            new_image = form.save(commit=False)
            new_image.user = request.user
            new_image.save()
            messages.success(request, "Posted successfully")
            return redirect(new_image.get_absolute_url())
    else:
        form = ImagePostForm()
    return render(request, "images/image/post.html", {"form": form})


@login_required
def image_bookmark(request):
    if request.method == "POST":
        form = ImageBookmarkForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_image = form.save(commit=False)
            new_image.user = request.user
            new_image.save()
            messages.success(request, "Posted successfully")
            return redirect(new_image.get_absolute_url())
    else:
        form = ImageBookmarkForm(data=request.GET)
    return render(
        request, "images/image/create.html", {"section": "images", "form": form}
    )


def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    form = CommentForm()
    return render(
        request,
        "images/image/detail.html",
        {"section": "images", "image": image, "form": form},
    )


@login_required
@require_POST
def image_like(request):
    image_id = request.POST.get("id")
    action = request.POST.get("action")
    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            if action == "like":
                image.users_like.add(request.user)
            else:
                image.users_like.remove(request.user)
            return JsonResponse({"status": "ok"})
        except Image.DoesNotExist:
            pass
    return JsonResponse({"status": "error"})


@login_required
def image_list(request):
    images = Image.objects.all()
    paginator = Paginator(images, 8)
    page = request.GET.get("page")
    images_only = request.GET.get("images_only")
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        images = paginator.page(1)
    except EmptyPage:
        if images_only:
            return HttpResponse("")
        images = paginator.page(paginator.num_pages)
    if images_only:
        return render(
            request,
            "images/image/list_images.html",
            {"section": "images", "images": images},
        )

    return render(
        request, "images/image/list.html", {"section": "images", "images": images}
    )


@login_required
@require_POST
def image_comment(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = image
        comment.user = request.user
        comment.save()
    return render(
        request,
        "images/image/detail.html",
        {"section": "images", "image": image, "form": form},
    )
