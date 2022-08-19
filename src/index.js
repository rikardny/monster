import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';

function TopMessage(props) {
  return props.phase;
}

function Square(props) {
  switch(props.plate) {
    case true:
      return <button className="slot plate" onClick={props.onClick}>{props.number}</button>
    case false:
      return <button className="slot" onClick={props.onClick}>{props.number}</button>
    case "source":
      return <button className="slot plate" onClick={props.onClick}>{props.number}</button>
    case "destination":
      return <button className="slot plate" onClick={props.onClick}>{props.number}</button>
  }
}

class Positions extends React.Component {
  renderSquare(i) {
    return (
      <Square
        number={i}
        plate={this.props.plates[i]}
        onClick={() => this.props.handleClick(i)}
      />
    );
  }

  render() {
    return (
      <div>
        <div className="board-row">
          {this.renderSquare(1)}
          {this.renderSquare(2)}
          {this.renderSquare(3)}
          {this.renderSquare(4)}
        </div>
      </div>
    );
  }
}

// SYSTEM STATE MACHINE:

class System extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      phase: "setup",
      plates: Array(5).fill(false),
    }
  }

  handleClick(i) {
    const plates = this.state.plates.slice();
    plates[i] = !plates[i];
    this.setState({plates: plates})
  }

  render() {
    return (
      <div className="game">
        <div className="game-board">
          <TopMessage phase={this.state.phase} />
          <Positions
            plates={this.state.plates}
            handleClick={(i) => this.handleClick(i)}
          />

        </div>
        <div className="game-info">
          <div>{/* status */}</div>
          <ol>{/* TODO */}</ol>
        </div>
      </div>
    );
  }
}

// ========================================

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<System />);
