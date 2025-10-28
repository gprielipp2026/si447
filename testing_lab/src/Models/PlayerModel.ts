import sha256 from 'crypto-js/sha256';

export class PlayerModel {
    username: string
    password: string
    session_token: string
    items: Array<string>
    action: string


    constructor() {
        this.username = "";
        this.password = "";
        this.session_token = "";
        this.items = [];
        this.action = "";
    }

    getUsername() { return this.username; }
    setUsername(u: string) { this.username = u; }

    getPassword() { return this.password; }
    setPassword(p: string) { this.password = sha256(p); }

    getToken() { return this.session_token; }
    setToken(t: string) { this.session_token = t; }

    getItems() { return this.items; }
    getItem(i: number) { return this.items[i]; }
    addItem(e: string) { this.items.push(e); }
    rmItem(e: string) { 
        const beg = this.items.length;
        this.items = this.items.filter(v => {
            if (e != v) return v;
        });
        const end = this.items.length;

        return beg > end; // true if item was removed, false if it was not (or not found)
    }

    getAction() { return this.action; }
    setAction(a: string) { this.action = a; }
}