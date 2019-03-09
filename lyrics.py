import wx


def modify_on_click(event):
    text = text_ctrl.GetValue()

    # remove empty line
    text = [line for line in text.split('\n') if line]

    # remove translate
    text = text[::2]

    text = '\n'.join(text)

    text_ctrl.SetValue(text)

    if wx.TheClipboard.Open():
        data_obj = wx.TextDataObject()
        data_obj.SetText(text)
        wx.TheClipboard.SetData(data_obj)
        wx.TheClipboard.Close()


def clear_on_click(event):
    text_ctrl.Clear()


if __name__ == '__main__':
    app = wx.App()

    # 默认显示在屏幕右下
    w, h = 600, 480
    screen_width, screen_height = wx.GetDisplaySize()
    frame = wx.Frame(None, title='歌词精简', size=(w, h), pos=(screen_width - w, screen_height - h))

    panel = wx.Panel(frame)

    # 组件
    text_ctrl = wx.TextCtrl(panel, style=wx.TE_MULTILINE)

    modify_button = wx.Button(panel, label='精简')
    modify_button.Bind(wx.EVT_BUTTON, modify_on_click)

    clear_button = wx.Button(panel, label='清空')
    clear_button.Bind(wx.EVT_BUTTON, clear_on_click)

    # 结构
    vbox = wx.BoxSizer(wx.VERTICAL)
    vbox.Add(modify_button, flag=wx.EXPAND | wx.ALL, border=5)
    vbox.Add(clear_button, flag=wx.EXPAND | wx.ALL, border=5)

    hbox = wx.BoxSizer()
    hbox.Add(text_ctrl, proportion=3, flag=wx.EXPAND)
    hbox.Add(vbox, proportion=1, flag=wx.EXPAND)

    panel.SetSizer(hbox)

    #
    frame.Show()
    app.MainLoop()
