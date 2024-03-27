const fs = require('fs');

function readfs(fp) {
	fs.readFile(fp, 'utf-8', (err, data) => {
		if (err) {
			console.error(err);
		}
		else {
			console.log(data);
		}
	});
}

readfs(process.argv[2])