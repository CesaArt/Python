from flexx import flx

class Example(flx.Widget):

    def init(self):
        flx.Button(text='hello')
        flx.Button(text='world')

app = flx.App(Example)
app.export('example.html', link=0)  # Export to single file

app.launch('browser')  # show it now in a browser
flx.run()  # enter the mainloop