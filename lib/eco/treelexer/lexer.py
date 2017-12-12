class RE_OR(object):
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

    def __repr__(self):
        return "OR(%s, %s)" % (self.lhs, self.rhs)

    def __eq__(self, other):
        return type(other) is type(self) and \
                self.lhs == other.lhs and self.rhs == other.rhs

class RE_DEFAULT(object):
    def __init__(self, c):
        self.c = c

    def __eq__(self, other):
        return type(other) is type(self) and self.c == other.c

    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, self.c)

class RE_CHAR(RE_DEFAULT): pass
class RE_STAR(RE_DEFAULT): pass
class RE_PLUS(RE_DEFAULT): pass
class RE_QUESTION(RE_DEFAULT): pass

class RE_RANGE(RE_DEFAULT):
    def __init__(self, c, neg=False):
        RE_DEFAULT.__init__(self, c)
        self.neg = neg

class PatternMatcher(object):

    def __init__(self):
        self.pos = 0
        self.exactmatch = True

    def reset(self):
        self.pos = 0
        self.exactmatch = True

    def inc(self):
        self.pos += 1

    def char(self):
        return self.text[self.pos]

    def isend(self):
        return self.pos >= len(self.text)

    def textlength(self):
        return len(self.text)

    def load_state(self, state):
        self.pos = state[0]
        self.exactmatch = state[1]
        self.result = state[2]

    def save_state(self):
        return (self.pos, self.exactmatch, list(self.result))

    def match_one(self, pattern):
        if self.isend():
            # Existing pattern can't match empty input
            return False
        char = self.char()
        if pattern.c == ".":
            # Wild card always matches
            return True
        if pattern.c == char:
            return True
        if pattern.c[0] == "\\" and pattern.c[1] == char:
            return True
        self.exactmatch = False
        return False

    def match_star(self, pattern):
        while self._match(pattern.c):
             pass
        return True

    def match_plus(self, pattern):
        if not self._match(pattern.c):
            # we have to at least match one
            return False
        return self.match_star(pattern)

    def match_question(self, pattern):
        self._match(pattern.c)
        return True

    def match_list(self, pattern):
        for p in pattern:
            if not self._match(p):
                return False
        return True

    def match_or(self, pattern):
        tmp = self.save_state()
        if self._match(pattern.lhs):
            return True
        self.load_state(tmp)
        return self._match(pattern.rhs)

    def match_range(self, pattern):
        if self.isend():
            return False
        if (pattern.neg and ord(self.char()) not in pattern.c) \
                    or (not pattern.neg and ord(self.char()) in pattern.c):
            return True
        self.exactmatch = False
        return False

    def _match(self, pattern):
        if not pattern:
            self.pos = self.textlength()
            return True
        if type(pattern) is list:
            return self.match_list(pattern)
        if type(pattern) is RE_CHAR:
            if self.match_one(pattern):
                self.result.append(self.char())
                self.inc()
                return True
            return False
        if type(pattern) is RE_STAR:
            return self.match_star(pattern)
        if type(pattern) is RE_STAR:
            return self.match_star(pattern)
        if type(pattern) is RE_PLUS:
            return self.match_plus(pattern)
        if type(pattern) is RE_OR:
            return self.match_or(pattern)
        if type(pattern) is RE_RANGE:
            if self.match_range(pattern):
                self.result.append(self.char())
                self.inc()
                return True
            return False
        if type(pattern) is RE_QUESTION:
            return self.match_question(pattern)
        raise NotImplementedError(pattern)

    def match(self, pattern, text, pos=0):
        self.reset()
        self.pos = pos
        self.text = text
        self.result = []
        if self._match(pattern):
            return "".join(self.result)
        return None

from incparser.astree import TextNode, BOS, EOS

class TreePatternMatcher(PatternMatcher):
    def char(self):
        return self.text.symbol.name[self.pos]

    def inc(self):
        self.pos += 1
        if self.pos >= len(self.text.symbol.name):
            self.text = self.text.next_term
            self.pos = 0

    def isend(self):
        if type(self.text) is EOS:
            return True
        return False

    def load_state(self, state):
        self.pos = state[0]
        self.text = state[1]
        self.exactmatch = state[2]
        self.result = state[3]

    def save_state(self):
        return (self.pos, self.text, self.exactmatch, list(self.result))

class RegexParser(object):

    def __init__(self):
        from grammars.grammars import regex
        p, l = regex.load()
        self.incparser = p
        self.inclexer = l

    def load(self, pattern):
        from incparser.astree import TextNode
        from grammar_parser.gparser import Terminal
        self.incparser.reset()
        bos = self.incparser.previous_version.parent.children[0]
        bos.insert_after(TextNode(Terminal(pattern)))
        self.inclexer.relex(bos)
        self.incparser.reparse()
        return self.incparser.last_status

    def compile(self, pattern):
        self.load(pattern)
        start = self.incparser.previous_version.parent.children[1].alternate
        return self.parse(start)

    def parse(self, node):
        from grammar_parser.bootstrap import ListNode
        if type(node) is ListNode:
            return self.parse_list(node)
        if node.name == "OR":
            return self.parse_or(node)
        elif node.name == "GROUP":
            return self.parse_group(node)
        elif node.name == "STAR":
            return self.parse_star(node)
        elif node.name == "PLUS":
            return self.parse_plus(node)
        elif node.name == "CHAR":
            return self.parse_char(node)
        elif node.name == "RANGE":
            return self.parse_range(node)
        elif node.name == "NRANGE":
            return self.parse_range(node, True)
        elif node.name == "QST":
            return self.parse_question(node)
        raise NotImplementedError(node)

    def parse_list(self, node):
        if len(node.children) > 1:
            return [self.parse(c) for c in node.children]
        return self.parse(node.children[0])

    def parse_or(self, node):
        lhs = self.parse(node.get("lhs"))
        rhs = self.parse(node.get("rhs"))
        return RE_OR(lhs, rhs)

    def parse_char(self, node):
        return RE_CHAR(node.get("value").symbol.name)

    def parse_range(self, node, neg=False):
        l = []
        for n in node.get("value").children:
            if n.lookup == "rangetype":
                a = ord(n.symbol.name[0])
                b = ord(n.symbol.name[2])
                if a > b:
                    l.extend(range(b, a+1))
                else:
                    l.extend(range(a, b+1))
            elif len(n.symbol.name) == 2: # escaped
                l.append(ord(n.symbol.name[1]))
            else:
                l.append(ord(n.symbol.name))
        if neg:
            return RE_RANGE(l, True)
        return RE_RANGE(l)

    def parse_star(self, node):
        content = self.parse(node.get("value"))
        return RE_STAR(content)

    def parse_group(self, node):
        return self.parse(node.get("value"))

    def parse_plus(self, node):
        content = self.parse(node.get("value"))
        return RE_PLUS(content)

    def parse_question(self, node):
        content = self.parse(node.get("value"))
        return RE_QUESTION(content)

class Lexer(object):

    def __init__(self, rules):
        rp = RegexParser()
        self.patterns = []
        for name, rule in rules:
            pattern = rp.compile(rule)
            self.patterns.append((pattern, name))

    def lex(self, text):
        """Lexes a given string by trying all patterns. When a match is found a
        token is created, and the lexing continues with the remainder of the
        string. Lookahead is calculated by observing how far the patternmatcher
        got before returning 'no match'. If a token was matched by a plus or
        star rule (e.g. [a-z]+), then the generated token is not an exact match,
        as it could potentially be longer. This means its lookahead is one
        character longer (and at least 1), since the pattern matcher had to look
        ahead one character to decide that the token is complete."""
        pm = PatternMatcher()
        self.pos = 0
        result = []
        while True:
            lookahead = 0
            oldpos = self.pos
            for p, n in self.patterns:
                pm.reset()
                if pm.match(p, text[self.pos:]):
                    if not pm.exactmatch:
                        lookahead += 1
                    result.append((text[self.pos:self.pos + pm.pos], n, lookahead))
                    self.pos += pm.pos
                    lookahead = 0
                else:
                    lookahead = max(pm.pos, lookahead)
            if self.pos == oldpos:
                # no more matches
                if self.pos < len(text):
                    result.append((text[self.pos:], None, 0))
                break
        return result

    def treelex(self, node):
        pm = TreePatternMatcher()
        pos = 0
        result = []
        while True:
            lookahead = 0
            oldpos = pos
            oldnode = node
            for p, n in self.patterns:
                pm.reset()
                token = pm.match(p, node)
                if token:
                    lookahead = lookahead + (1 if not pm.exactmatch else 0)
                    result.append((token, n, lookahead))
                    pos = pm.pos
                    node = pm.text
                    lookahead = 0
                else:
                    lookahead = max(pm.pos, lookahead)
            if pos == oldpos and oldnode is node:
                # no more matches
                break
        return result
