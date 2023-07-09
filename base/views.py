from django.shortcuts import render
import RazorPay
from django.views.decorators.csrf import csrf_exempt


def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        amount = 5000

        client = RazorPay.Client(auth=("rzp_test_Po0ByeOrpzroyx", "5LQbaXtQSjNp7dtHHdltpqkN"))

        payment = client.order.create({'amount': amount, 'currency': 'INR',
                                       'payment_capture': '1'})
    return render(request, 'index.html')

@csrf_exempt
def success(request):
    return render(request, "success.html")
