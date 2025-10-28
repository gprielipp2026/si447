import './App.css';

import { PlayerModel } from './Models/PlayerModel.ts';
import { ServerModel } from './Models/ServerModel.ts';

function App() {
  let player = new PlayerModel();
  let server = new ServerModel();

  return (
    <div className="App">
      <div>
        <p>
          {player.getUsername()}
        </p>
        <input type="text" name="username" id="username" onInput={e => player.setUsername(e.target.value)}/>

      </div>
    </div>
  );
}

export default App;
