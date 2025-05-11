from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import random


def lotto(request):
    # 產生 1~49 的隨機數字
    numbers = sorted(random.sample(range(1, 50), 6))
    # 字串化
    numbers = " ".join(map(str, numbers))
    # 特別號
    special = random.randint(1, 49)
    # 將結果組合
    result = {
        "numbers": numbers,
        "special": special,
    }

    return render(request, "lotto.html", result)

    return JsonResponse(result)


# Create your views here.
def hello(request):
    result = {
        "name": "John Doe",
        "age": 30,
        "city": "New York",
    }
    return JsonResponse(result)
