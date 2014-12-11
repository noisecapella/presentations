import sys

if (sys.version_info) < (3,):
    raise Exception("Need Python 3")

from IPython.nbconvert.exporters import SlidesExporter
from IPython.config import Config

from IPython.nbformat import current as nbformat

name = "Testing with Docker"
infile = name + ".ipynb" # load the name of your slideshow
outfile = name + ".slides.html"

notebook = open(infile).read()
notebook_json = nbformat.reads_json(notebook)

# This is the config object I talked before: 
# After the 'url_prefix', you can set the location of your 
# local reveal.js library, i.e. if the reveal.js is located 
# in the same directory as your talk.slides.html, then 
# set 'url_prefix':'reveal.js'.

c = Config({
            'RevealHelpTransformer':{
                'enabled':True,
                'url_prefix':'reveal.js',
                },                
            })

exportHtml = SlidesExporter(config=c)
(body,resources) = exportHtml.from_notebook_node(notebook_json)

text = body
text = text.replace("@media print", "")
text = text.replace("/* Overrides of notebook CSS for static HTML export */", ".rendered_html li { font-size: 36pt; line-height: 150%; } .rendered_html h1 { font-size: 30pt; } .rendered_html > p { font-size: 30pt; } .input_prompt { display: none; } .input_area>.highlight>pre { font-size: 15pt; }  ")
text = text.replace(" <section>", " <section style='padding: 0px !important;'>")
open(outfile, 'w').write(text)
