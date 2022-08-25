function App() {
	fetch('/api')
		.then((response) => response.json())
		.then((data) => console.log(data));

	// @ts-ignore
	return <>Hello, World</>;
}

export default App;
