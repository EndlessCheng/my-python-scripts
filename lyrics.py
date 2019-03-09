import wx


def reset_on_click(event):
    text = text_ctrl.GetValue()

    # remove empty line
    text = [line for line in text.split('\n') if line]

    # remove translate
    text = text[::2]

    text_ctrl.SetValue('\n'.join(text))


if __name__ == '__main__':
    app = wx.App()

    # 默认显示在屏幕右下
    w, h = 600, 480
    screen_width, screen_height = wx.GetDisplaySize()
    frame = wx.Frame(None, title='歌词精简', size=(w, h), pos=(screen_width - w, screen_height - h))
    panel = wx.Panel(frame)

    text_ctrl = wx.TextCtrl(panel, style=wx.TE_MULTILINE)

    reset_button = wx.Button(panel, label='精简')
    reset_button.Bind(wx.EVT_BUTTON, reset_on_click)

    hbox = wx.BoxSizer()
    hbox.Add(text_ctrl, proportion=3, flag=wx.EXPAND)
    hbox.Add(reset_button, proportion=1, flag=wx.EXPAND, border=5)

    panel.SetSizer(hbox)

    frame.Show()
    app.MainLoop()
