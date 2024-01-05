from modules import *


class canvas:
    def __init__(self, size: tuple[int, int]) -> None:
        self.size = size
        self.content = [[" "]*size[0] for _ in range(size[1])]

    def fill(self, char: str) -> None:
        for x in range(0, self.size[0]):
            for y in range(0, self.size[1]):
                self.content[y][x] = char
        return

    def blit(self, text: str, pos: tuple[int, int], front_modifier: str = "", back_modifier: str = "") -> None:
        n = self.size[0]
        lines = [list(text[i:i+n]) for i in range(0, len(text), n)]
        y = 0
        while y < len(lines):
            for x, char in enumerate(lines[y]):
                if char == "\n":
                    lines.insert(y+1, lines[y][x+1:])
                    lines[y] = lines[y][:x]
                    break
                self.content[pos[1]+y][pos[0] +
                                       x] = front_modifier+char+back_modifier
            y += 1


class Screen(canvas):
    def __init__(self, size: tuple, pos: tuple) -> None:
        super().__init__(size)
        self.pos = pos

    def draw(self) -> None:
        for i, line in enumerate(self.content):
            if len(line)-1 > self.size[0]:
                self.clear()
                print_at(self.pos[0]+1, self.pos[1]+1,
                         f"line {i} too long!\n{len(line)}\ncropping line for next frame!")
                self.content[i] = self.content[i][:-(len(line)-self.size[0])]
                return
            # print(line)
            compiled = "".join(line)
            print_at(self.pos[0]+1, self.pos[1]+i+1, compiled)

    def clear(self) -> None:
        lines = []
        for i in range(self.size[1]):
            lines.append(" "*self.size[0])
        for i, line in enumerate(lines):
            print_at(self.pos[0]+1, self.pos[1]+i+1, line)


class cluster:
    def __init__(self):
        self.screens = []

    def draw(self, index: int):
        if not index > len(self.screens):
            self.screens[index].draw()

    def draw_all(self):
        for screen in self.screens:
            screen.draw()

    def remove_screen(self, index: int):
        if not index > len(self.screens):
            self.screens[index].clear()
            self.screens.remove(self.screens[index])
