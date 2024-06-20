from django.conf import settings
from django_ratelimit.decorators import ratelimit
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from django.core.cache import cache
from django.utils import timezone

class MyRateLimitMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Check if the request is for /login/ and is a POST request
        if request.path == '/login/' and request.method == 'POST':
            
            # Define the login_view function with rate limiting decorator
            @ratelimit(key='ip', rate='3/m', block=True, method='POST')
            def login_view(request):
                # Check if IP is currently blocked
                blocked_until = cache.get(f'blocked_{request.META["REMOTE_ADDR"]}')
                if blocked_until:
                    # If blocked, check if the block time has passed
                    if blocked_until < timezone.now():
                        cache.delete(f'blocked_{request.META["REMOTE_ADDR"]}')
                    else:
                        # If still blocked, return None (request blocked)
                        return JsonResponse({'error': 'Too many attempts. Try again later.'}, status=429)

                # Get current attempt count from cache
                attempt_count = cache.get(f'login_attempts_{request.META["REMOTE_ADDR"]}', 0)
                attempt_count += 1

                # Update attempt count in cache
                cache.set(f'login_attempts_{request.META["REMOTE_ADDR"]}', attempt_count, timeout=300)

                # If attempts exceed limit, block IP for 10 minutes
                if attempt_count >= 5:
                    cache.set(f'blocked_{request.META["REMOTE_ADDR"]}', timezone.now() + timezone.timedelta(minutes=10), timeout=600)
                    return JsonResponse({'error': 'Too many attempts. Try again later.'}, status=429)

                # Return None to allow the request to proceed
                return None

            # Call the login_view function and return its response
            return login_view(request)

        # If request does not match /login/ POST, return None (continue processing)
        return None
