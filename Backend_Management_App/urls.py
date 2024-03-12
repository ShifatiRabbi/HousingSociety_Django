from django.urls import path
from .views import *


urlpatterns = [
    path('', homePage, name='home'),

    path('members/', MemberListView.as_view(), name='member_list'),
    path('members/create/', MemberCreateView.as_view(), name='member_create'),
    path('members/<int:pk>/update/', MemberUpdateView.as_view(), name='member_update'),
    path('members/<int:pk>/delete/', MemberDeleteView.as_view(), name='member_delete'),
    
    path('communitycenters/', CommunityCenterListView.as_view(), name='communitycenter_list'),
    path('communitycenters/create/', CommunityCenterCreateView.as_view(), name='communitycenter_create'),
    path('communitycenters/<int:pk>/update/', CommunityCenterUpdateView.as_view(), name='communitycenter_update'),
    path('communitycenters/<int:pk>/delete/', CommunityCenterDeleteView.as_view(), name='communitycenter_delete'),
    
    path('bookings/', BookingListView.as_view(), name='booking_list'),
    path('bookings/<int:community_center_id>/create/', book_community_center, name='booking_create'),
    path('community_centers', community_centers, name='community_centers'),
    path('bookings/<int:pk>/update/', BookingUpdateView.as_view(), name='booking_update'),
    path('bookings/<int:pk>/delete/', BookingDeleteView.as_view(), name='booking_delete'),
    
    
    

    path('playgrounds/', PlayGroundListView.as_view(), name='playground_list'),
    path('playgrounds/create/', PlayGroundCreateView.as_view(), name='playground_create'),
    path('playgrounds/<int:pk>/update/', PlayGroundUpdateView.as_view(), name='playground_update'),
    path('playgrounds/<int:pk>/delete/', PlayGroundDeleteView.as_view(), name='playground_delete'),
    
    path('bookinggrounds/', BookingGroundListView.as_view(), name='bookingground_list'),
    path('bookinggrounds/<int:play_ground_id>/create/', book_play_ground, name='bookingground_create'),
    path('play_grounds', play_grounds, name='play_grounds'),
    path('bookinggrounds/<int:pk>/update/', BookingGroundUpdateView.as_view(), name='bookingground_update'),
    path('bookinggrounds/<int:pk>/delete/', BookingGroundDeleteView.as_view(), name='bookingground_delete'),

    
]

