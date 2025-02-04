from django.conf import settings

def add_csp_nonce(request):
    return {
        'nonce': settings.CSP_NONCE,
    }