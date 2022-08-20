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
      change = <button type="button" className="btn btn-primary" onClick={props.onClick}>Done</button>
      mode = <button type="button" className="btn btn-primary" disabled>Setup</button>
      text = <span>1. Select initial plate positions</span>
      run = <button type="button" className="btn run btn-danger" disabled>Run</button>
      break;
    case "source":
      change = <button type="button" className="btn btn-secondary" onClick={props.onClick}>Change</button>
      mode = <button type="button" className="btn btn-success" disabled>Source</button>
      text = <span>2. Select plate for pick up</span>
      run = <button type="button" className="btn run btn-danger" disabled>Run</button>
      break;
    case "target":
      change = <button type="button" className="btn btn-secondary" onClick={props.onClick}>Cancel</button>
      mode = <button type="button" className="btn btn-danger" disabled>Target</button>
      text = <span>3. Select target position for plate</span>
      run = <button type="button" className="btn run btn-danger" disabled>Run</button>
      break;
    case "ready":
      change = <button type="button" className="btn btn-secondary" onClick={props.onClick}>Cancel</button>
      mode = <button type="button" className="btn btn-warning" disabled>Ready</button>
      text = <span>4. Press run to perform move</span>
      run = <button type="button" className="btn run btn-danger">Run</button>
      break;
    case "moving":
      change = <button type="button" className="btn btn-secondary" disabled>Cancel</button>
      mode = <button type="button" className="btn btn-danger" disabled>Ready</button>
      text = <span>5. Press abort to stop move</span>
      run = <button type="button" className="btn run btn-danger">Abort</button>
      break;
    default: break;
  }

  return (
    <div className="section">
      <div className="btn-group" role="group">
        {change}
        {mode}
      </div>
      {text}
      {run}
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
    }
  }

  handleChangeClick() {
    switch(this.state.mode) {
      case "setup":     this.setState({mode: "source"});    break;
      case "source":    this.setState({mode: "setup"});     break;
      case "target":    this.setState({mode: "source"});    break;
      default: break;
    }
  }

  handlePlateClick(i) {
    const plates = this.state.plates.slice();
    switch(this.state.mode) {
      case "setup": plates[i] = plates[i] === "empty" ? "full" : "empty"; break;
      case "source":
        plates[i] = plates[i] === "full" ? "source" : "empty";
        this.setState({mode: "target"});
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
