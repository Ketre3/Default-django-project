from django.core.management.base import BaseCommand
from pathlib import Path
import json

from django.core.files import File
# from decimal import Decimal

from Product.models import Product, ProductStyle, ProductTrend, ProductType
from Image.models import Image
import requests
import tarfile


PICTURES_GZIP_URL = "https://github.com/Ketre3/Test_pictures_for_projects/raw/master/test_pictures.tar.gz"


def download_test_pictures():
    test_pictures_path = Path('.') / 'Product' / 'test_pictures.tar.gz'
    test_pictures_path.touch()
    raw_gz = requests.get(PICTURES_GZIP_URL).content
    with test_pictures_path.open('wb') as f:
        f.write(raw_gz)

    tarfile.open(test_pictures_path).extractall(test_pictures_path.parent)


class Command(BaseCommand):
    help = """
    Create some test products, product styles and so on
    Make sure that you have images in "server/media/" path.
    """

    def handle(self, *args, **kwargs):
        to_import_file = Path('.') / 'Product' / 'to_import.json'
        path_to_image_folder = Path('.') / 'Product' / 'test_pictures'

        if not path_to_image_folder.exists():
            self.stdout.write('Download pictures...')
            download_test_pictures()
            self.stdout.write('Done!')

        with to_import_file.open() as f:
            to_import = json.load(f)

        # for prod_type in to_import['product_type']:
        #     ProductType.objects.create(name=prod_type)
        ProductType.objects.bulk_create(
            ProductType(name=prod_type)
            for prod_type in to_import['product_type']
        )
        self.stdout.write('Created product types.')

        # for prod_trend in to_import['product_trend']:
        #     ProductTrend.objects.create(name=prod_trend)

        ProductTrend.objects.bulk_create(
            ProductTrend(name=prod_trend)
            for prod_trend in to_import['product_trend']
        )
        self.stdout.write('Created product trends.')

        # for prod_style in to_import['product_style']:
        #     ProductStyle.objects.create(name=prod_style)

        ProductStyle.objects.bulk_create(
            ProductStyle(name=prod_style)
            for prod_style in to_import['product_style']
        )
        self.stdout.write('Created product styles.')

        def _get_image(object_name, filename):
            path_to_image = path_to_image_folder / filename
            with path_to_image.open('rb') as f:
                image = Image.objects.create(
                    name=object_name,
                    value=File(f),
                )
            return image

        Product.objects.bulk_create(
            Product(
                name=product['name'],
                image=_get_image(
                    object_name=product['image'],
                    filename=product['image']['value']
                ),
                description=product['description'],
                product_type=ProductType.objects.get(
                    name=product['product_type']
                ),
                style=ProductStyle.objects.get(name=product['style']),
                trend=ProductTrend.objects.get(name=product['trend']),
                color=product['color'], cost=product['cost'],
            )
            for product in to_import['products']
        )
        # for product in to_import['products']:
        self.stdout.write('Products created!')
