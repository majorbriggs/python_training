import jinja2
from crossweb_events import get_list_of_events

list_of_events = get_list_of_events()
with open('templates/table.html') as f_in, open('output.html', 'w', encoding='utf-8') as f_out:
    template = jinja2.Template(f_in.read())
    rendered = template.render(items=list_of_events[:10])
    f_out.write(rendered)