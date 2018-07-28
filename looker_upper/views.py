from django.shortcuts import render

def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    context = {'latest_question_list': latest_question_list}
    context = {}
    return render(request, 'looker_upper/index.html', context)


def find(request):
    product_name = request.POST["product_to_find"]
    ingredients = [ "first ingredient", "second ingredient" ]
    return render(request, 'looker_upper/results.html',
                  {'ingredients': ingredients,
                   'product_name': product_name})
