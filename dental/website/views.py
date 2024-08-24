from django.shortcuts import render


def homepage(request):
    return render(request, "home.html", {})


def about(request):
    return render(request, "about.html")


def blog(request):
    return render(request, "blog.html")


def blogpost(request):
    return render(request, "blogpost.html")


def pricing(request):
    return render(request, "pricing.html")


def service(request):
    return render(request, "service.html")


def contact(request):
    if request.method == "POST":
        message_name = request.POST["message-name"]
        message_email = request.POST["message-email"]
        message = request.POST["message"]

        return render(request, "contact.html", {"meessage": message_name})

    else:
        return render(request, "contact.html", {})
