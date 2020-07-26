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
                }// ,
                //Use this label as an example as to how to make the GUI execute a python command. Use arguments to
                //  decide what function is to be executed.
                // {
                //     label: "Python Test", click() {
                //
                //         // expressapp.get('/name', callFUNC);
                //         //
                //         // function callFUNC(req, res) {
                //         //     let spawn = require('child_process').spawn;
                //         //     let process = spawn('python', ['./PythonAPI/pythonTESTING.py',
                //         //     req.query.pyarg]);
                //         //
                //         //     process.stdout.on('data', function(data){
                //         //         res.send(data.toString());
                //         //     });
                //         // }
                //         // client.invoke("TESTING", (error, result) => {
                //         //     if (error) {
                //         //         console.log(error)
                //         //     } else {
                //         //         console.log(result)
                //         //     }
                //         // })
                //
                //         var python = require("child_process").spawn("python", ["./PythonAPI/scriptEXECUTOR.py", "hello"]);
                //         python.stdout.on("data", function (data) {
                //             console.log("data: ", data.toString());
                //             let abc = document.getElementById("pythonTESTINGground");
                //             abc.innerHTML = data.toString();
                //         });
                //     }
                // }
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

// const ipc = require('electron').ipcMain;
// ipc.on('testButton', (event, args) => {
//     console.log(args);
//     event.returnValue = 'Hello';
// });

app.whenReady().then(createWindow);

//app.on('ready', createWindow)

app.on("window-all-closed", () => {
    // On macOS it is common for applications and their menu bar
    // to stay active until the user quits explicitly with Cmd + Q
    if (process.platform !== "darwin") {
        app.quit();
    }
});