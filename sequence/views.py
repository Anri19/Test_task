from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def asd(n):
    s = {}
    b = 1
    s[str(b)] = n
    k = 0
    while k != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        k = n
        b = b + 1
        s[str(b)] = int(n)
    return (s)


def generate_following_sequence(request, pk):
    x = pk
    return JsonResponse(asd(x))


def returns_the_value_smaller_than_n(request, pk):
    x = pk
    max_sqs_n = 1
    for i in range(2, x, 1):
        if len(asd(i)) > len(asd(i - 1)):
            max_sqs_n = i
    return HttpResponse(f"Longest sequence is for n = {max_sqs_n} { asd(max_sqs_n)}")


