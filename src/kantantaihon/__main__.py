import argparse
import html
import os
from collections import defaultdict
from .se import SELibrary
from .lexer import Lexer, Token
from .character import CharacterManager, Character, GlobalDialogues
from .formatter import *
from .config import Config


def parse_script(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    lexer = Lexer()
    result = ""

    curr_character = None
    prev_character = None

    for line in lines:
        line = line.strip()
        if not line:
            result += "<br>"
            continue
        parsed, raw = lexer.lex(line)
        token, content = parsed

        match token:
            case Token.CH_NAME:
                name, pos = content
                prev_character = curr_character
                curr_character = CharacterManager.get_character(name)
                if prev_character != None and prev_character != curr_character:
                    result += "<br>"
                result += script_format_ch(token, curr_character, pos)
            case Token.SE:
                SELibrary.add(content)
                result += script_format_se(token, content)
            case Token.POS:
                result += script_format_pos(token, content)
            case Token.DESC:
                result += script_format_desc(token, content)
            case Token.LINE:
                GlobalDialogues.count(content)
                if curr_character:
                    curr_character.add_dialogue(content)
                result += script_format_line(token, content)
        result += "<br>"

    print(f"character count: {GlobalDialogues.character_count}")
    print(f"se: {SELibrary.get()}")
    for name, character in CharacterManager.characters.items():
        print(f"{name}: {character.character_count}")

    return TEMPLATE.format(title=os.path.basename(file_path), content=result, character_color_style=CHARACTER_COLOR_STYLE)


def main():
    parser = argparse.ArgumentParser(
        description='Parse a script file into an HTML-based format.')
    parser.add_argument('file', help='Input script file (UTF-8)')
    parser.add_argument('--percharacter', action='store_true',
                        help='Extract individual scripts per character')
    parser.add_argument("-c", "--config", required=False,
                        help='Configuration file for formatting')
    args = parser.parse_args()

    if args.config:
        Config.load(args.config)
    parsed_text = parse_script(args.file)

    with open('output.html', 'w', encoding='utf-8') as f:
        f.write(parsed_text)


if __name__ == '__main__':
    main()
