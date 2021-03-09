from rest_framework import serializers

from products.models import Category, Smartphone, Notebook


class CategorySerializer(serializers.ModelSerializer):

    name = serializers.CharField(required=True)
    slug = serializers.CharField()

    class Meta:
        model = Category
        fields =[
            'id','name','slug'
        ]


class BaseProductSerializer:

    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects)
    title = serializers.CharField(required=True)
    slug = serializers.SlugField(required=True)
    image = serializers.ImageField(required=True)
    description = serializers.CharField(required=False)
    price = serializers.DecimalField(max_digits=9, decimal_places=2, required=True)


class SmartphoneSerializer(BaseProductSerializer, serializers.ModelSerializer):
    diagonal = serializers.CharField(required=True)
    display_type = serializers.CharField(required=True)
    resolution = serializers.CharField(required=True)
    accum_volume = serializers.CharField(required=True)
    ram = serializers.CharField(required=True)
    sd = serializers.BooleanField(required=True)
    sd_volume = serializers.CharField(required=True)
    main_cam_mp = serializers.CharField(required=False)
    frontal_cam_mp = serializers.CharField(required=False)

    class Meta:
        model = Smartphone
        fields = '__all__'


class NotebookSerializer(BaseProductSerializer, serializers.ModelSerializer):
    diagonal = serializers.CharField(required=False)
    display_type = serializers.CharField(required=False)
    processor_freq = serializers.CharField(required=False)
    ram = serializers.CharField(required=False)
    video = serializers.CharField(required=False)
    time_without_charge = serializers.CharField(required=False)

    class Meta:
        model = Notebook
        fields = '__all__'
