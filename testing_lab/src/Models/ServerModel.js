import axios from 'axios';

export class ServerModel {
	constructor() {
		// set up the connection to the remote server ...
		this.server = 'http://lnx1073302govt:8000';
	}

	createUser(player) {
		/**
		 * post request
		 * receives success message or error
		 */
		// some sort of CORS issue going on...
		// axios
		// 	.post(this.server + '/user', {
		// 		username: player.getUsername(),
		// 		password: player.getPassword(),
		// 	})
		// 	.then((resp) => {
		// 		console.log(resp);
		// 	})
		// 	.catch((err) => {
		// 		console.log('Axios error');
		// 		console.error(err);
		// 	});
		console.log({
			METHOD: 'POST',
			url: this.server + '/user',
			body: {
				username: player.getUsername(),
				password: player.getPassword(),
			},
		});

		return {
			message: 'Success',
		};
	}

	login(player) {
		console.log({
			METHOD: 'POST',
			url: this.server + '/login',
			body: {
				username: player.getUsername(),
				password: player.getPassword(),
			},
		});

		return {
			session_token: 'SOME_RANDOM_TOKEN',
		};
	}

	move(player) {}

	look(player) {}

	doSomething(player) {}

	useItem(player) {}

	getPlayers() {}
}
