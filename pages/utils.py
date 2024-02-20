import  matplotlib.pyplot as plt
from io import BytesIO
import base64

def get_plot():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    plot = base64.b64encode(image_png)
    plot = plot.decode('utf-8')
    buffer.close()
    return plot

def make_plot(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.scatter(x,y)
    plot = get_plot()
    return plot