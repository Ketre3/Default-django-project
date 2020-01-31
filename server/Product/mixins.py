from django.shortcuts import redirect


class AdminGroupRequired:
    redirect_url = ''

    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perms(
            [
                'products.add_product',
                'products.update_product',
                'products.delete_product'
            ]
        ):
            return super().dispatch(request, *args, **kwargs)
        return redirect(self.redirect_url)
