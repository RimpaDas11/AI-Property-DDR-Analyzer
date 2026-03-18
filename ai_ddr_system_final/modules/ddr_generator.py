from jinja2 import Environment, FileSystemLoader

def generate_ddr(data, images, output_path):
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("report_template.html")
    html = template.render(summary=data[:5], observations=data, images=images)
    with open(output_path, "w") as f:
        f.write(html)
