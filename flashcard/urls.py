from django.urls import path
from . import views

urlpatterns = [
    path('deck/', views.deck_list, name='deck_list'),
    path('deck/<int:deck_id>/', views.deck_detail, name='deck_detail'),
    path('deck/create/', views.create_deck, name='create_deck'),
    path('deck/<int:deck_id>/card/create/', views.create_card, name='create_card'),
    path('deck/<int:deck_id>/card/<int:card_id>/delete/', views.delete_card, name='delete_card'),
    path('deck/<int:deck_id>/review/', views.review_deck, name='review_deck'),
]
