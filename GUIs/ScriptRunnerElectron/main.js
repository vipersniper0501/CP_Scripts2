const {app, BrowserWindow, Menu} = require("electron");

function createWindow () {
    const window = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            nodeIntegration: true
        }
    });

    var menu = Menu.buildFromTemplate([
        {
            label: "Help",
            submenu: [
                {
                    label: "About Creators", click() {
                        console.log("About Creator Window Opened");
                        //window.location.href = '../menu_files/about_creators.html'
                        window.loadFile("./menu_files/about_creators.html");
                    }
                },
                {label: "How to use program"},
                {label: "Command Descriptions"},
                {
                    label: "Change Configurations", click() {

                    }
                },
                //Use this label as an example as to how to make the GUI execute a python command. Use arguments to
                //  decide what function is to be executed.
                {
                    label: "Python Test", click() {
                        var python = require("child_process").spawn("python", ["./PythonAPI/scriptEXECUTOR.exe", "hello"]);
                        python.stdout.on("data", function (data) {
                            console.log("data: ", data.toString("utf8"));
                        });
                    }
                }
            ]
        }
    ]);
    Menu.setApplicationMenu(menu);

    window.loadFile("./index.html");
    //window.webContents.openDevTools()
}

function changeconfTEST(){
    console.log("test");
}

app.whenReady().then(createWindow);

//app.on('ready', createWindow)

app.on("window-all-closed", () => {
    // On macOS it is common for applications and their menu bar
    // to stay active until the user quits explicitly with Cmd + Q
    if (process.platform !== "darwin") {
        app.quit();
    }
});