export class PlayerModel {
	constructor(setSignedIn) {
		this.username = '';
		this.password = '';
		this.session_token = '';
		this.items = [];
		this.action = '';
		this.setSignedIn = setSignedIn;
	}

	getUsername() {
		return this.username;
	}
	setUsername(u) {
		this.username = u;
	}

	verified() {
		this.setSignedIn(true);
	}

	getPassword() {
		return this.password;
	}
	setPassword(p) {
		this.password = p;
	}

	getToken() {
		return this.session_token;
	}
	setToken(t) {
		this.session_token = t;
	}

	getItems() {
		return this.items;
	}
	getItem(i) {
		return this.items[i];
	}
	addItem(e) {
		this.items.push(e);
	}
	rmItem(e) {
		const beg = this.items.length;
		this.items = this.items.filter((v) => {
			if (e !== v) return v;
		});
		const end = this.items.length;

		return beg > end; // true if item was removed, false if it was not (or not found)
	}

	getAction() {
		return this.action;
	}
	setAction(a) {
		this.action = a;
	}
}
