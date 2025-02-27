from .lexer import Token
from .character import Character
from .colors import CHARACTER_COLORS
from .config import Config

TEMPLATE = """
<html lang="jp">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        .pos {{
            background-color: #FFF700;
        }}
        {character_color_style}
    </style>
</head>
<body>
    {content}
</body>
</html>
"""

CHARACTER_COLOR_STYLE = f"""
.character_0 {{
    background-color: {CHARACTER_COLORS[0]};
}}

.character_1 {{
    background-color: {CHARACTER_COLORS[1]};
}}

.character_2 {{
    background-color: {CHARACTER_COLORS[2]};
}}

.character_3 {{
    background-color: {CHARACTER_COLORS[3]};
}}

.character_4 {{
    background-color: {CHARACTER_COLORS[4]};
}}

.character_5 {{
    background-color: {CHARACTER_COLORS[5]};
}}
"""


def script_format_ch(token, character: Character, pos):
    if pos:
        return f"<span class=\"character_{character.number}\">{Config.CH_SYMBOL} {character.name} 【{pos}】</span>"
    else:
        return f"<span class=\"character_{character.number}\">{Config.CH_SYMBOL} {character.name} </span>"


def script_format_se(token, content):
    return f"<span class=\"se\">（{Config.SE_SYMBOL}SE： {content}）</span>"


def script_format_pos(token, content):
    return f"<span class=\"pos\">{Config.POS_SYMBOL} {content}</span>"


def script_format_line(token, content):
    return f"<span class=\"line\">{content}</span>"


def script_format_desc(token, content):
    return f"<span class=\"desc\">（{content}）</span>"
