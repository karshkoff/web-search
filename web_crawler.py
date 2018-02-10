def continue_crawl(search_history, target_url):
    ''' Checking the input list
        search_history: list urls
        target_url: current url
    '''
    if target_url in search_history:
        print('Url has already found')
        return False
    elif len(search_history) > 25:
        print('Search history list cannot be more 25 links')
        return False
    return True

# Test continue_crawl
#search_history = []
#target_url = 'https://en.wikipedia.org/wiki/Football'
#print(continue_crawl(search_history, target_url))
