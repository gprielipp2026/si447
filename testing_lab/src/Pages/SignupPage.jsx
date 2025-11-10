import Credentials from './Credentials';

const SignupPage = ({ server, player }) => {
	return (
		<div>
			<h1>Sign up</h1>
			<Credentials player={player} />
			<button
				onClick={(e) => {
					let resp = server.createUser(player);
					console.log(resp);
					player.verified();
				}}
			>
				Sign up
			</button>
		</div>
	);
};

export default SignupPage;
