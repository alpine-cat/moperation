from rest_framework import serializers
from .models import Adv
from django.contrib.auth.models import User


class AdvSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Adv
        fields = ('url', 'owner', 'datetime_start', 'datetime_end', 'content', 'wn8', 'wins_percent', 'url_clan')


class UserSerializer(serializers.ModelSerializer):
    ads = serializers.PrimaryKeyRelatedField(many=True, queryset=Adv.objects.all())

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'is_superuser', 'ads')

