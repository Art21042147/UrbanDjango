from django.shortcuts import render
from django.views.generic import TemplateView


def main_page(request):
    title = "Main Page"
    main_head = "Game Booster"
    second_head = "Let's play!"
    shop = "Shop"
    cart = "Cart"
    context = {
        'title': title,
        'main_head': main_head,
        'second_head': second_head,
        'shop': shop,
        'cart': cart,
    }
    return render(request, 'third_task/platform.html', context)


class ShopView(TemplateView):
    template_name = 'third_task/games.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Shop'
        context['head'] = 'New Games'
        context['buy'] = 'Buy'
        context['return'] = 'Return to home page'
        context['games'] = ['Metal Beer Liquid',
                            'Tomb Provider',
                            'Resident Liver']
        return context


class CartView(TemplateView):
    template_name = 'third_task/cart.html'
