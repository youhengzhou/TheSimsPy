import "./App.css";

let dummy = ({ num }) => {
    <>{num}</>;
};

function MyComponent(props) {
    return (
        <div>
            <p>Prop 1: {props.prop1}</p>
            <p>Prop 2: {props.prop2}</p>
        </div>
    );
}

function Square(dictionary) {
    function handleClick() {
        console.log(dictionary);
        console.log("clicked!");
    }

    return (
        <>
            <button className="square" onClick={handleClick}>
                {dictionary.key1}
            </button>
            <button className="square" onClick={handleClick}>
                {dictionary.key2}
            </button>
        </>
    );
}

function Board() {
    return (
        <>
            <MyComponent prop1="value1" prop2="value2" />
            <div className="board-row">
                <Square key1="1" key2="1" />
                <Square />
                <Square />
            </div>
            <div className="board-row">
                <Square />
                <Square />
                <Square />
            </div>
            <div className="board-row">
                <Square />
                <Square />
                <Square />
            </div>
        </>
    );
}

function App() {
    return <div className="App">{Board()}</div>;
}

export default App;
