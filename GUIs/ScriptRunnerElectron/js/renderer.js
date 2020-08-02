const ipc = require("electron").ipcRenderer;
const pytestbtn = document.querySelector("#python_test");
let test_reply = document.querySelector("#TEST_reply");

function buttonTest() {
    console.log("hi");
}

pytestbtn.addEventListener("click", () => {
    // let reply = ipc.sendSync('testButton', 'Button Works');
    // test_reply.innerHTML = 'from renderer';
    buttonTest();
    var python = require("child_process").spawn("python", ["./PythonAPI/scriptEXECUTOR.py", "hello"]);
    python.stdout.on("data", function (data) {
        //console.log("data: ", data.toString());
        test_reply.innerHTML = data.toString();
    });
});

// ipc.on('buttonReply', (event, args) => {
//     test_reply.innerHTML = args;
// });