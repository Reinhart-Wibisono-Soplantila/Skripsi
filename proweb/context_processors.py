def active_menu(request):
    namespace = request.resolver_match.namespace
    url_name = request.resolver_match.url_name
    return {
        'current_url': f'{namespace}:{url_name}' if namespace else url_name
    }