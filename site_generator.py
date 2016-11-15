from markdown import markdown
import json
import os
from jinja2 import Environment, FileSystemLoader
from collections import defaultdict
import argparse
BASE_DIR = 'site/articles'


def load_data(file):
    with open(file, 'r') as f:
        return json.load(f)


def convert_md_to_html(file):
    with open(file, 'r') as f:
        return markdown(f.read(), extensions=['codehilite', 'fenced_code'])


def render_base_page(data):
    env = Environment(loader=FileSystemLoader('./'))
    template = env.get_template('templates/base.html')
    return template.render(data)


def mk_site_struct(config):
    for item in config['articles']:
        outdir, filename = os.path.split(item['source'])
        outdir = os.path.join(BASE_DIR, outdir)
        filename = filename.replace('md', 'html')
        if not os.path.exists(outdir):
            os.makedirs(outdir)
        html = convert_md_to_html(os.path.join('articles', item['source']))
        data = {'html': html,
                'title': item['title'],
                'topic': item['topic']}
        with open(os.path.join(outdir, filename), 'w') as f:
            f.write(render_base_page(data))


def mk_site_index(config):
    data = defaultdict(list)
    for item in config['articles']:
        path = item['source'].replace('md', 'html')
        data[item['topic']].append([os.path.join('articles', path),
                                    item['title']])
    env = Environment(loader=FileSystemLoader('./'))
    template = env.get_template('templates/index.html')
    with open('site/index.html', 'w') as f:
        f.write(template.render(struct=data))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Make static site from markdown files')
    parser.add_argument('filepath', help='json file')
    args = parser.parse_args()
    struct = load_data(args.filepath)
    mk_site_struct(struct)
    mk_site_index(struct)
