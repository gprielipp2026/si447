import axios from "axios";
import { PlayerModel } from "./PlayerModel.ts";

export class ServerModel {
    server: string

    constructor() {
        // set up the connection to the remote server ...
        this.server = 'http://lnx1073302govt:8000/';
    }

    createUser(player: PlayerModel) {
        /**
         * post request
         * receives success message or error
         */
        axios.post(
            this.server,
            {
                'username': player.getUsername(),
                'password': player.getPassword()
            }
        )
        .then(resp => {
            console.log(resp);
        })
    }

    login(player: PlayerModel) {

    }

    move(player: PlayerModel) {

    }

    look(player: PlayerModel) {

    }

    doSomething(player: PlayerModel) {

    }

    useItem(player: PlayerModel) {

    }

    getPlayers() {

    }

}