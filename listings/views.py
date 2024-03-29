from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


from .models import Listing
from listings.chooses import price_choices, state_choices, badroom_choices

def index(request):
  listings = Listing.objects.order_by('-list_date').filter(is_published=True)

  paginator = Paginator(listings, 6)
  page = request.GET.get('page')
  page_listings = paginator.get_page(page)

  context = {
    'listings': page_listings 
  }
  return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
      'listing': listing
    }
    return render(request, 'listings/listing.html', context)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # Keyword
    if 'keywords' in request.GET:
      keywords = request.GET['keywords']
      if keywords: 
        queryset_list = queryset_list.filter(description__icontains=keywords)
    
    # City 
    if 'city' in request.GET:
      city = request.GET['city']
      if city: 
        queryset_list = queryset_list.filter(city__iexact=city)
      
     # State 
    if 'state' in request.GET:
      state = request.GET['state']
      if state: 
        queryset_list = queryset_list.filter(state__iexact=state)

     # Bedroom 
    if 'bedrooms' in request.GET:
      bedroom = request.GET['bedrooms']
      if bedroom: 
        queryset_list = queryset_list.filter(bedroom__lte=bedroom)
    
    # Price
    if 'price' in request.GET:
      price = request.GET['price']
      if price: 
        queryset_list = queryset_list.filter(price__lte=price)
    
    context = { 
      'price_choices': price_choices,
      'state_choices': state_choices,
      'badrooms_choices': badroom_choices,
      'listings': queryset_list,
      'values': request.GET
    }
    return render(request, 'listings/search.html', context)