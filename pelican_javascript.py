"""
Include JavaScript and CSS files for Pelican
============================================

This plugin allows you to easily embed JS and CSS in the header of individual
articles.
"""
import os
import shutil

from pelican import signals

def copy_resources(src, dest, file_list):
    """
    Copy files from content folder to output folder

    Parameters
    ----------
    src: string
        Content folder path
    dest: string,
        Output folder path
    file_list: list
        List of files to be transferred

    Output
    ------
    Copies files from content to output
    """
    if not os.path.exists(dest):
        os.makedirs(dest)
    for file_ in file_list:
        file_src = os.path.join(src, file_)
        shutil.copy2(file_src, dest)

def add_files(gen, metadata):
    """
    The registered handler for the dynamic resources plugin. It will
    add the javascripts and/or stylesheets to the article
    """
    site_url = gen.settings['SITEURL']
    formatters = {'stylesheets': '<link rel="stylesheet" href="{0}" type="text/css" />',
                  'javascripts': '<script src="{0}"></script>'}
    dirnames = {'stylesheets': 'css',
                'javascripts': 'js'}
    for key in ['stylesheets', 'javascripts']:
        if key in metadata:
            files = metadata[key].replace(" ", "").split(",")
            htmls = []
            for f in files:
                if f.startswith('http://') or f.startswith('https://'):
                    link = f
                else:
                    if gen.settings['RELATIVE_URLS']:
                        link = "%s/%s" % (dirnames[key], f)
                    else:
                        link = "%s/%s/%s" % (site_url, dirnames[key], f)
                html = formatters[key].format(link)
                htmls.append(html)
            metadata[key] = htmls

def move_resources(gen):
    """
    Move files from js/css folders to output folder
    """
    js_files = gen.get_files('js', extensions='js')
    css_files = gen.get_files('css', extensions='css')

    js_dest = os.path.join(gen.output_path, 'js')
    copy_resources(gen.path, js_dest, js_files)

    css_dest = os.path.join(gen.output_path, 'css')
    copy_resources(gen.path, css_dest, css_files)


def register():
    """
    Plugin registration
    """
    signals.article_generator_context.connect(add_files)
    signals.page_generator_context.connect(add_files)
    signals.article_generator_finalized.connect(move_resources)
