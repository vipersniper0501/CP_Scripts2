const {app, BrowserWindow, Menu} = require('electron')

function createWindow () {
    const window = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
        nodeIntegration: true
        }
    })

    var menu = Menu.buildFromTemplate([
        {
            label: 'Help',
            submenu: [
                {label:'About Creators'},
                {label:'How to use program'}
            ]
        }
    ])
    Menu.setApplicationMenu(menu);

    window.loadFile('./index.html')

    window.webContents.openDevTools()

}


app.whenReady().then(createWindow)

//app.on('ready', createWindow)

app.on('window-all-closed', () => {
  // On macOS it is common for applications and their menu bar
  // to stay active until the user quits explicitly with Cmd + Q
  if (process.platform !== 'darwin') {
    app.quit()
  }
})