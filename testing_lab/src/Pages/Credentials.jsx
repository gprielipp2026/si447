const Credentials = ({ player }) => {
	return (
		<div>
			<table>
				<tbody>
					<tr>
						<td>Username</td>
						<td>
							<input
								type="text"
								onInput={(e) => player.setUsername(e.target.value)}
							/>
						</td>
					</tr>

					<tr>
						<td>Password</td>
						<td>
							<input
								type="text"
								onInput={(e) => player.setPassword(e.target.value)}
							/>
						</td>
					</tr>
				</tbody>
			</table>
		</div>
	);
};

export default Credentials;
