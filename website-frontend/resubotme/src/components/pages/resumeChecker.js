import React from 'react';
import '../../App.css';
import PDFViewer from '../pdf_components/PDFViewer';
import "./resumeChecker.css"
import JobCards from "../jobSearch_components/JobCards"
import CategoryCards from '../jobSearch_components/CategoryCards';
import GradeCards from "../jobSearch_components/GradeCards";


/*
function toggleDiv(divid){
            
  varon = divid + 'on';
  varoff = divid + 'off';

  if(document.getElementById(varon).style.display === 'block'){
    document.getElementById(varon).style.display = 'none';
    document.getElementById(varoff).style.display = 'block';
  }else{  
    document.getElementById(varoff).style.display = 'none';
    document.getElementById(varon).style.display = 'block';
  }
} 
 <div id="mydivoff" class="split left">
                <div class="centered">
                 <CategoryCards/>
                </div>
            </div>
*/

function resumeChecker() {
  return (
   
    <>
        <div className="pdf_container">
            
            <div id="mydivon" class="split left">
                <div class="centered">
                  
                  <CategoryCards/>
                  <JobCards/>
                  <GradeCards/>
                  
                 
                </div>
            </div>
           
            <div class="split right">
                <div>
                  <btn onclick="toggleDiv('mydiv')">Toggle Screen</btn>
                  <PDFViewer/>    
                </div>
            </div>
            <script>

            

            </script>
        </div>
    </>
    
  );
}

export default resumeChecker;
