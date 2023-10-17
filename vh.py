def open_browser(addr):
    """
    Open browser
    """
    url = "http://" + addr
    while True:
        sleep(0.1)
        try:
            with urllib.request.urlopen(url) as res:
                if res:
                    break
        except urllib.error.HTTPError as err:
            pass
        except urllib.error.URLError as err:
            pass
    webbrowser.open(url, new=2, autoraise=True)