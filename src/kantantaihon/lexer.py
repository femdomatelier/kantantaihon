from enum import Enum, auto
import re


class Token(Enum):
    CH_NAME = auto()
    SE = auto()
    AS = auto()
    AE = auto()
    POS = auto()
    DESC = auto()
    LINE = auto()
    EMPTY = auto()


def ch_name(scanner, token):
    result = re.match(r"([^:]+)(:|：)(.*)", token)
    return Token.CH_NAME, [result.group(1), result.group(3)]


def cmd(scanner, token: str):
    if not token:
        return Token.DESC, ""
    c = token.split()[0]
    s = token[len(c)+1:]
    if c == "\\se":
        return Token.SE, s
    elif c == "\\p":
        return Token.POS, s
    else:
        return Token.DESC, s


def empty_cmd(scanner, token):
    return Token.EMPTY, ""


def line(scanner, token):
    return Token.LINE, token


class Lexer:
    def __init__(self):
        self.scanner = re.Scanner([
            (r"[^:]+(:|：).*", ch_name),
            (r"\\[\S^　]*[\s|　].*", cmd),
            (r"\\", empty_cmd),
            (r".+", line)
        ])

    def lex(self, line):
        token, raw = self.scanner.scan(line)
        return token[0], raw
