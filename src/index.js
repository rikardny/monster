import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';

function Mode(props) {
  let change;
  let mode;
  let text;
  let run;

  switch(props.mode) {
    case "setup":
      change = <button type="button" className="btn change btn-primary" onClick={props.onClick}>Next</button>
      mode = <button type="button" className="btn btn-primary" disabled>Setup</button>
      text = <span>1. Select initial plate positions</span>
      run = <button type="button" className="btn run btn-outline-primary" disabled>Run</button>
      break;
    case "source":
      change = <button type="button" className="btn change btn-secondary" onClick={props.onClick}>Change</button>
      mode = <button type="button" className="btn btn-success" disabled>Source</button>
      text = <span>2. Select plate for pick up</span>
      run = <button type="button" className="btn run btn-outline-dark" disabled>Run</button>
      break;
    case "target":
      change = <button type="button" className="btn change btn-secondary" onClick={props.onClick}>Cancel</button>
      mode = <button type="button" className="btn btn-danger" disabled>Target</button>
      text = <span>3. Select target position for plate</span>
      run = <button type="button" className="btn run btn-outline-secondary" disabled>Run</button>
      break;
    case "ready":
      change = <button type="button" className="btn change btn-secondary" onClick={props.onClick}>Cancel</button>
      mode = <button type="button" className="btn btn-warning" disabled>Ready</button>
      text = <span>4. Press run to perform move</span>
      run = <button type="button" className="btn run btn-warning">Run</button>
      break;
    case "moving":
      change = <button type="button" className="btn change btn-secondary" disabled>Cancel</button>
      mode = <button type="button" className="btn btn-danger" disabled>Ready</button>
      text = <span>5. Press abort to stop move</span>
      run = <button type="button" className="btn run btn-danger">Abort</button>
      break;
    default: break;
  }

  return (
    <div className="section">
      {mode}
      {text}
      <div className="btn-group right" role="group">
        {change}
        {run}
      </div>
    </div>
  )
}

function Position(props) {
  switch(props.plate) {
    case "empty":   return <button className="position empty" onClick={props.onClick}>{props.id}</button>
    case "full":    return <button className="position full" onClick={props.onClick}>{props.id}</button>
    case "source":  return <button className="position source" onClick={props.onClick}>{props.id}</button>
    case "target":  return <button className="position target" onClick={props.onClick}>{props.id}</button>
    default:    return
  }
}


class Positions extends React.Component {
  renderSquare(i) {
    return (
      <Position
        id={i}
        plate={this.props.plates[i]}
        onClick={() => this.props.handlePlateClick(i)}
      />
    );
  }

  render() {
    return (
      <div className="section map">
        {this.renderSquare(1)}
        {this.renderSquare(2)}
        {this.renderSquare(3)}
        {this.renderSquare(4)}
      </div>
    );
  }
}

// SYSTEM STATE MACHINE:

class System extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      mode: "setup", // setup, source, target, ready, moving
      plates: Array(5).fill("empty"), // empty, full, source, target
      initial: Array(5).fill("empty"), // copy
    }
  }

  resetPlates() {
    const initial = this.state.initial.slice()
    this.setState({plates: initial})
  }

  handleChangeClick() {
    switch(this.state.mode) {
      case "setup":
        const plates = this.state.plates.slice();
        this.setState({initial: plates})
        this.setState({mode: "source"});
        break;
      case "source":
        this.setState({mode: "setup"});
        this.resetPlates();
        break;
      case "target":
        this.setState({mode: "source"});
        this.resetPlates();
        break;
      case "ready":
        this.setState({mode: "source"});
        this.resetPlates();
        break;
      default: break;
    }
  }

  handlePlateClick(i) {
    const plates = this.state.plates.slice();
    switch(this.state.mode) {
      case "setup": plates[i] = plates[i] === "empty" ? "full" : "empty"; break;
      case "source":
        if (plates[i] === "full") {
          plates[i] = "source";
          this.setState({mode: "target"});
        }
        break;
      case "target":
        if (plates[i] === "empty") {
          plates[i] = "target";
          this.setState({mode: "ready"});
        }
        break;
      default: break;
    }
    this.setState({plates: plates})
  }

  render() {
    return (
      <div className="container">
        <Mode
          mode={this.state.mode}
          onClick={() => this.handleChangeClick()}
        />
        <Positions
          plates={this.state.plates}
          handlePlateClick={(i) => this.handlePlateClick(i)}
        />
      </div>
    );
  }
}

// ========================================

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<System />);
