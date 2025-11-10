import Credentials from './Credentials';

const LoginPage = ({ server, player }) => {
	return (
		<div>
			<h1>Log in</h1>
			<Credentials player={player} />
			<button
				onClick={(e) => {
					let result = server.login(player);

					player.setToken(result.session_token);
					player.verified();
				}}
			>
				Log in
			</button>
		</div>
	);
};

export default LoginPage;
