import markdown

def render_markdown(md_text : str) -> str:
    return markdown.markdown(md_text)