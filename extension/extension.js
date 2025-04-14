const vscode = require("vscode");

//for dev {
const fs = require('fs');
const path = require('path');
//for dev }

/**
 * @param {vscode.ExtensionContext} context
 */
function activate(context) {
  console.log('Your extension "gitter-committer" is now active!');

  // Hello World sample command (optional)
  const disposable = vscode.commands.registerCommand(
    "gitter-committer.helloWorld",
    function () {
      vscode.window.showInformationMessage("Hello VS Code!");
    }
  );
  context.subscriptions.push(disposable);

  // gcpc with custom flags
  const disposable2 = vscode.commands.registerCommand(
    "gitter-committer.gcpc",
    async function () {
      const userInput = await vscode.window.showInputBox({
        placeHolder: "--staged --model gemini",
        prompt: "Enter custom flags for gcpc",
      });

      // for development purposes start
      // Get current workspace root
      const workspaceFolders = vscode.workspace.workspaceFolders;
      const projectRoot = path.resolve(__dirname, '..');

      // fallback for testing
      console.log("Project root:", projectRoot);
      // Determine platform and venv activation path
      const isWindows = process.platform === 'win32';

      const venvActivation = isWindows
        ? path.join(projectRoot, 'venv', 'Scripts', 'activate') // Windows
        : path.join(projectRoot, 'venv', 'bin', 'activate');    // macOS/Linux

      const terminal = vscode.window.createTerminal("GitterCommitter");
      terminal.show();

      if (fs.existsSync(venvActivation)) {
        console.log("Detected venv. Activating:", venvActivation);
        
        const activateCommand = isWindows
          ? `${venvActivation} && gcpc ${userInput || "--staged --model gemini"}`
          : `source ${venvActivation} && gcpc ${userInput || "--staged --model gemini"}`;
        
        terminal.sendText(activateCommand);
      } else {
        console.log("No venv detected. Falling back to gcpc from $PATH.");
        const command = `gcpc ${userInput || "--staged --model gemini"}`;
        terminal.sendText(command);
      }
    }
  );
  context.subscriptions.push(disposable2);

  // gcpull with custom flags
  const disposable3 = vscode.commands.registerCommand(
    "gitter-committer.gcpull",
    async function () {
      const userInput = await vscode.window.showInputBox({
        placeHolder: "--model gemini",
        prompt: "Enter custom flags for gcpull",
      });
      const command = `gcpull ${userInput || "--model gemini"}`;
      const terminal = vscode.window.createTerminal("GitterCommitter");
      terminal.show();
      terminal.sendText(command);
    }
  );
  context.subscriptions.push(disposable3);

  // gccommit with custom flags
  const disposable4 = vscode.commands.registerCommand(
    "gitter-committer.gccommit",
    async function () {
      const userInput = await vscode.window.showInputBox({
        placeHolder: "--staged --model gemini",
        prompt: "Enter custom flags for gccommit",
      });
      const command = `gccommit ${userInput || "--model gemini"}`;
      const terminal = vscode.window.createTerminal("GitterCommitter");
      terminal.show();
      terminal.sendText(command);
    }
  );
  context.subscriptions.push(disposable4);
}

function deactivate() {}

module.exports = {
  activate,
  deactivate,
};
