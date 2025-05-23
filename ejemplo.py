from jinja2 import Template

template = Template(
"""
<ul>
  {% for part in partlist %}
    <li>{{ part }}</li>
  {% endfor %}
</ul>
"""
)

partlist = ["A", "B", "C"]

texto_final = template.render(partlist=partlist)


print(texto_final)