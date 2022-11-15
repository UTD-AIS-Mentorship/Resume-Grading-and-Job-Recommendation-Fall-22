import React from 'react';

import {BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';
import Home from './components/pages/Home';
import ResumeChecker from './components/pages/resumeChecker';
import JobSearch from './components/pages/jobSearch';

function App() {
  return (
    <>
    <Router>
      <Routes>
        <Route path={"/resumeChecker"}  exact element = {<ResumeChecker />} ></Route>
        <Route path={'/'} exact element = {<Home />}> </Route>
        <Route path={"/jobSearch"} exact element = {<JobSearch />} ></Route>
        
      </Routes>
    </Router>
    </>  
  );
}

export default App;
