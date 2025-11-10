import { useState } from 'react';
import './App.css';

import { PlayerModel } from './Models/PlayerModel';
import { ServerModel } from './Models/ServerModel';
import LandingPage from './Pages/LandingPage';

function App() {
	const [signedIn, setSignedIn] = useState(false);

	let player = new PlayerModel(setSignedIn);
	let server = new ServerModel();

	return (
		<div className="App">
			{signedIn ? (
				<>
					<h1>Signed in :)</h1>
				</>
			) : (
				<LandingPage
					player={player}
					server={server}
				/>
			)}
		</div>
	);
}

export default App;
