from django.shortcuts import render

# Create your views here.
def calc(req):
    if req.method == "POST":
        try:
            first = int(req.POST["first"])
            second = int(req.POST["second"])
            result = first + second
        except (ValueError, KeyError):
            first = second = result = "Invalid input"
    else:
        first = second = result = 0
    
    return render(req, 'calc.html', {
        'first': first,
        'second': second,
        'result': result
    })
