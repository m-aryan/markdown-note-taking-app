import language_tool_python

tool = language_tool_python.LanguageTool("en-US")


def check_grammar(text: str):
    matches = tool.check(text)
    mistakes = []

    for m in matches:
        mistakes.append(
            {
                "message": m.message,
                "suggestions": m.replacements,
                "offset": m.offset,
                "length": m.error_length,
            }
        )

    return mistakes
