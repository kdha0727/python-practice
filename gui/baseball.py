import tkinter as tk
import random


class NumericBaseballApp:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Numeric Baseball")
        tk.Label(
            self.window,
            font=3, height=3, anchor='n',
            text="\nNumeric Baseball\n"
        ).pack()
        frame = tk.Frame(self.window)
        frame.pack(anchor='n', fill='x', padx=5)
        self.entry = tk.Entry(frame, width=35)
        self.entry.pack(padx=5, side='left')
        self.button_enter = tk.Button(
            frame, text="입력", width=5,
            command=self.command_enter
        )
        self.button_enter.pack(padx=5, side='left')
        self.button_start_text = tk.StringVar()
        self.button_start_text.set('시작하기')
        self.button_start = tk.Button(
            frame, textvariable=self.button_start_text, width=10,
            command=self.command_start
        )
        self.button_start.pack(padx=5, anchor='n', side='left')
        frame = tk.Frame(self.window)
        frame.pack(fill='x', anchor='n', pady=5)
        self.label_text = tk.StringVar()
        self.label_text.set('시작하기 버튼을 클릭해주세요.')
        self.label = tk.Label(frame, bg="white", textvariable=self.label_text, width=55)
        self.label.pack(side='left', padx=5)
        frame = tk.Frame(self.window)
        frame.pack(fill='x', anchor='n')
        scroll = tk.Scrollbar(frame)
        self.textbox = tk.Listbox(frame, width=53, height=13, yscrollcommand=scroll.set, bg='white')
        self.textbox.pack(side='left')
        scroll.pack(side='left', fill='y')
        scroll.config(command=self.textbox.yview)

        self.ball = None

    def get_entry(self):
        return self.entry.get()

    def set_entry(self, message=None):
        self.entry.delete(0, 'end')
        self.entry.insert('end', message or '')

    def set_label(self, message=None):
        self.label_text.set(message or '')

    def set_textbox(self, message=None):
        self.textbox.insert('end', message or '')

    @staticmethod
    def create_ball():
        ball = ''
        sequence = list(range(1, 10))
        while len(ball) < 3:
            b = random.choice(sequence)
            if str(b) in ball:
                continue
            sequence.remove(b)
            ball += str(b)
        return ball

    def command_start(self):
        self.button_start_text.set('다시하기')
        self.set_entry()
        self.ball = self.create_ball()
        self.set_label('서로 다른 세자리 숫자를 입력하세요.')
        self.set_textbox('게임 시작')

    def command_enter(self):

        if self.ball is None:
            self.set_label('게임을 시작해야 합니다.')
            return

        ball_number = self.get_entry()
        if not ball_number.isnumeric() or len(set(ball_number)) != 3:
            self.set_label('서로 다른 세자리 숫자가 아닙니다.')

        elif ball_number == self.ball:
            self.set_label('1아웃! 다시하기를 눌러주세요.')
            self.set_textbox('{0}: 1아웃!'.format(ball_number))
            self.ball = None

        else:
            b = len(set(self.ball).intersection(set(ball_number)))
            s = len(list(True for i, j in zip(self.ball, ball_number) if i == j))
            b -= s
            state = '{0} 스트라이크 {1} 볼'.format(s, b)
            self.set_label(state)
            self.set_textbox('{0}: {1}'.format(ball_number, state))

    def __call__(self):
        self.window.mainloop()


if __name__ == '__main__':
    app = NumericBaseballApp()
    app()
