from styles.models import Banner1 as Banner

def get_image():
    try:
        styles = Banner.objects.get(id=1)
        return styles.login_image
    except:
        return "Error"