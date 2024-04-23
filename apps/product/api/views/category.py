from django.shortcuts import get_object_or_404
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from apps.product.models import *
from apps.product.api.serializers import (
    CategoryListSerializers, MainCategorySerializer, CategoryOrderSerializer, CategoryProductsSerializer
)
from utils.pagination import StandardResultsSetPagination
from utils.responses import (
    bad_request_response,
    success_response,
    success_created_response,
    success_deleted_response,
)
from utils.pagination import PaginationMethod
from utils.expected_fields import check_required_key
from drf_yasg.utils import swagger_auto_schema
from apps.product.filters import ProductCategoryFilter


class CategoryListView(APIView):
    permission_classes = [AllowAny]
    """ Category Get View """

    is_popular = openapi.Parameter('popular_category', openapi.IN_QUERY,
                                   description="Filter by Popular categories",
                                   type=openapi.TYPE_BOOLEAN)
    is_new = openapi.Parameter('new_category', openapi.IN_QUERY,
                               description="Filter by New categories",
                               type=openapi.TYPE_BOOLEAN)
    is_hits = openapi.Parameter('hits_category', openapi.IN_QUERY,
                                description="Filter by Hits categories",
                                type=openapi.TYPE_BOOLEAN)
    search = openapi.Parameter('search', openapi.IN_QUERY,
                               description="Seraching ...",
                               type=openapi.TYPE_STRING)
    is_available = openapi.Parameter('is_available', openapi.IN_QUERY,
                                     description="AVAILABLE products",
                                     type=openapi.TYPE_BOOLEAN)

    @swagger_auto_schema(operation_description="Retrieve a list of categories",
                         manual_parameters=[is_popular, is_new, is_hits, search, is_available],
                         tags=['Categories'],
                         responses={200: CategoryListSerializers(many=True)})
    def get(self, request):
        queryset = ProductCategories.objects.all().order_by('-id', 'order').filter(
            parent=None,
            # is_available=True
        )
        filterset = ProductCategoryFilter(request.GET, queryset=queryset)
        if filterset.is_valid():
            queryset = filterset.qs
        serializers = MainCategorySerializer(queryset, many=True,
                                             context={'request': request})
        return success_response(serializers.data)

    """ Category Post View """

    @swagger_auto_schema(request_body=MainCategorySerializer,
                         operation_description="Category create",
                         tags=['Categories'],
                         responses={201: MainCategorySerializer(many=False)})
    def post(self, request):
        # valid_fields = {'name', 'icon', 'logo'}
        # unexpected_fields = check_required_key(request, valid_fields)
        # if unexpected_fields:
        #     return bad_request_response(f"Unexpected fields: {', '.join(unexpected_fields)}")

        serializers = MainCategorySerializer(data=request.data, context={'request': request})
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return success_created_response(serializers.data)
        return bad_request_response(serializers.errors)


class CategoryDetailView(APIView, PaginationMethod):
    pagination_class = StandardResultsSetPagination
    permission_classes = [AllowAny]
    """ Category Get View """

    is_hits = openapi.Parameter('hits_category', openapi.IN_QUERY,
                                description="Filter by Hits categories",
                                type=openapi.TYPE_BOOLEAN)

    @swagger_auto_schema(operation_description="Retrieve category or sub categories",
                         tags=['Categories'],
                         responses={200: CategoryListSerializers(many=True)})
    def get(self, request, pk):
        queryset = get_object_or_404(ProductCategories, pk=pk)
        serializers = MainCategorySerializer(queryset, context={'request': request, })
        return success_response(serializers.data)

    """ Category Put View """

    @swagger_auto_schema(request_body=CategoryListSerializers,
                         operation_description="Category update",
                         tags=['Categories'],
                         responses={200: MainCategorySerializer(many=False)})
    def put(self, request, pk):
        # valid_fields = {'name', 'icon'}
        # unexpected_fields = check_required_key(request, valid_fields)
        # if unexpected_fields:
        #     return bad_request_response(f"Unexpected fields: {', '.join(unexpected_fields)}")

        queryset = get_object_or_404(ProductCategories, pk=pk)
        request.data._mutable = True
        request.data.pop('logo', None)
        request.data.pop('icon', None)
        request.data._mutable = False
        serializers = MainCategorySerializer(instance=queryset, data=request.data, context={
            'request': request,
            'logo': request.FILES.get('logo', None),
            'icon': request.FILES.get('icon', None)
        })
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return success_response(serializers.data)
        return bad_request_response(serializers.errors)

    """ Category Delete View """

    @swagger_auto_schema(operation_description="Delete a category",
                         tags=['Categories'],
                         responses={204: 'No content'})
    def delete(self, request, pk):
        queryset = get_object_or_404(ProductCategories, pk=pk)
        queryset.delete()
        return success_deleted_response("Successfully deleted")


class HomeCategoryView(APIView):
    pagination_class = StandardResultsSetPagination
    permission_classes = [AllowAny]

    @swagger_auto_schema(operation_description="Retrieve category or sub categories",
                         tags=['Categories'],
                         responses={200: CategoryProductsSerializer(many=True)})
    def get(self, request):
        category = ProductCategories.objects.filter(home=True).first()
        serializers = CategoryProductsSerializer(category, context={'request': request, })
        return success_response(serializers.data)

    def post(self, request):
        category_id = request.data['id']
        category = get_object_or_404(ProductCategories, id=category_id)
        old_category = ProductCategories.objects.filter(home=True).first()
        old_category.home = False
        old_category.save()
        category.home = True
        category.save()

        serializers = CategoryProductsSerializer(category, context={'request': request, })
        return success_response(serializers.data)


class CategoryChangeOrderView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body=CategoryListSerializers,
                         operation_description="Category update",
                         tags=['Categories'],
                         responses={200: CategoryOrderSerializer(many=False)})
    def patch(self, request, pk):
        valid_fields = {'order'}
        unexpected_fields = check_required_key(request, valid_fields)

        if unexpected_fields:
            return bad_request_response(f"Unexpected fields: {', '.join(unexpected_fields)}")

        queryset = get_object_or_404(ProductCategories, pk=pk)
        serializers = CategoryOrderSerializer(instance=queryset, data=request.data,
                                              context={'request': request})
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return success_response(serializers.data)
        return bad_request_response(serializers.errors)
