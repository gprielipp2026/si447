import { useState } from 'react';
import LoginPage from './LoginPage';
import SignupPage from './SignupPage';

const LandingPage = ({ player, server }) => {
	const [isLogin, setIsLogin] = useState(false);
	const [isFirstPage, setIsFirstPage] = useState(true);

	return (
		<div>
			{isFirstPage ? (
				<>
					<button
						onClick={() => {
							setIsLogin(true);
							setIsFirstPage(false);
						}}
					>
						Login
					</button>
					<br />
					<button
						onClick={() => {
							setIsLogin(false);
							setIsFirstPage(false);
						}}
					>
						Sign up
					</button>
				</>
			) : isLogin ? (
				<LoginPage
					player={player}
					server={server}
				/>
			) : (
				<SignupPage
					player={player}
					server={server}
				/>
			)}
		</div>
	);
};

export default LandingPage;
