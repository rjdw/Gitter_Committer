const vscode = require('vscode');

/**
 * @param {vscode.ExtensionContext} context
 */
function activate(context) {
	console.log('Your extension "gitter-committer" is now active!');

	// Leaving this here for now, easy to understand
	const disposable = vscode.commands.registerCommand('gitter-committer.helloWorld', function () {
		vscode.window.showInformationMessage('Hello VS Code!');
	});
	context.subscriptions.push(disposable);

	const disposable2 = vscode.commands.registerCommand('gitter-committer.gcpc', function () {
		const terminal = vscode.window.createTerminal("GitterCommitter");
		terminal.show();
		terminal.sendText("gcpc --staged --model gemini");
	});
	context.subscriptions.push(disposable2);

	const disposable3 = vscode.commands.registerCommand('gitter-committer.gcpull', function () {
		const terminal = vscode.window.createTerminal("GitterCommitter");
		terminal.show();
		terminal.sendText("gcpull --model gemini");
	});
	context.subscriptions.push(disposable3);
}

function deactivate() {}

module.exports = {
	activate,
	deactivate
};
