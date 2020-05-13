
Clipping input data to the valid range for imshow with RGB data ([0..1] for floats or [0..255] for integers).
Traceback (most recent call last):

  File "F:\Tools\Anaconda\lib\site-packages\IPython\core\formatters.py", line 341, in __call__
    return printer(obj)

  File "F:\Tools\Anaconda\lib\site-packages\IPython\core\pylabtools.py", line 248, in <lambda>
    png_formatter.for_type(Figure, lambda fig: print_figure(fig, 'png', **kwargs))

  File "F:\Tools\Anaconda\lib\site-packages\IPython\core\pylabtools.py", line 132, in print_figure
    fig.canvas.print_figure(bytes_io, **kw)

  File "F:\Tools\Anaconda\lib\site-packages\matplotlib\backend_bases.py", line 2065, in print_figure
    **kwargs)

  File "F:\Tools\Anaconda\lib\site-packages\matplotlib\backends\backend_agg.py", line 527, in print_png
    FigureCanvasAgg.draw(self)

  File "F:\Tools\Anaconda\lib\site-packages\matplotlib\backends\backend_agg.py", line 388, in draw
    self.figure.draw(self.renderer)

  File "F:\Tools\Anaconda\lib\site-packages\matplotlib\artist.py", line 38, in draw_wrapper
    return draw(artist, renderer, *args, **kwargs)

  File "F:\Tools\Anaconda\lib\site-packages\matplotlib\figure.py", line 1709, in draw
    renderer, self, artists, self.suppressComposite)

  File "F:\Tools\Anaconda\lib\site-packages\matplotlib\image.py", line 135, in _draw_list_compositing_images
    a.draw(renderer)

  File "F:\Tools\Anaconda\lib\site-packages\matplotlib\artist.py", line 38, in draw_wrapper
    return draw(artist, renderer, *args, **kwargs)

  File "F:\Tools\Anaconda\lib\site-packages\matplotlib\axes\_base.py", line 2647, in draw
    mimage._draw_list_compositing_images(renderer, self, artists)

  File "F:\Tools\Anaconda\lib\site-packages\matplotlib\image.py", line 135, in _draw_list_compositing_images
    a.draw(renderer)

  File "F:\Tools\Anaconda\lib\site-packages\matplotlib\artist.py", line 38, in draw_wrapper
    return draw(artist, renderer, *args, **kwargs)

  File "F:\Tools\Anaconda\lib\site-packages\matplotlib\image.py", line 619, in draw
    renderer, renderer.get_image_magnification())

  File "F:\Tools\Anaconda\lib\site-packages\matplotlib\image.py", line 881, in make_image
    unsampled=unsampled)

  File "F:\Tools\Anaconda\lib\site-packages\matplotlib\image.py", line 504, in _make_image
    self.get_filternorm(), self.get_filterrad())

ValueError: Unsupported dtype

<Figure size 1080x1080 with 8 Axes>