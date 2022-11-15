import React from 'react';
import '../../App.css';
import Footer from '../frontPage_components/Footer';
import JobCards from '../jobSearch_components/JobCards';
import CategoryCards from '../jobSearch_components/CategoryCards';
//import resumeCards from '../../components/resumeChecker_components/resumeCards';


function jobSearch() {
  return (
    <>
        <CategoryCards/> 
        <JobCards/> 
        <Footer />
    </>
  );
}

export default jobSearch;


