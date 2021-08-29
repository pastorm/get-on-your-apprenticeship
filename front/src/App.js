import React, { Component } from 'react';
import logo from './hogwarts.png';
import './App.css';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = { apiResponse: "" };
  }
  
  componentDidMount() {
    this.getStudents();
  }

  getStudents() {
    fetch("http://localhost:3000/real/students")
      .then(res => res.text())
      .then(res => this.setState({ apiResponse: res }))
      .catch(err => err);
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            Here is a list of all students:
        </p>
        <p className="App-intro">{this.state.apiResponse}</p>
        </header>
      </div>
    );
  }
}

export default App;
