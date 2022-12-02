import React, {useState} from "react";
import '../../App.css';
//import PDFViewer from '../pdf_components/PDFViewer';
import "./resumeChecker.css"
import JobCards from "../jobSearch_components/JobCards"
import CategoryCards from '../jobSearch_components/CategoryCards';
import GradeCards from "../jobSearch_components/GradeCards";
import { CircularProgressbar,buildStyles } from 'react-circular-progressbar';
import "react-circular-progressbar/dist/styles.css"
import VisibilitySensor from "react-visibility-sensor";
import { Link } from "react-router-dom";
import resumeData from "../../data.js"


function ResumeChecker() {
  
 const [option, setOption]=useState(true);
 const [input, setInput]=useState(false)
 const [pdfFile,setPdfFile]=useState(false);
 const [rawFile, setRawFile] = useState(false);
 const [pdfError, setPdfError]=useState('');
 const [submit, setSubmit]=useState(false);
  const [totalScore, setTotalScore] = useState(false)
  const [gradesData, setGradeData] = useState(false)
  const [jobData, setJobData] = useState(false);
  const [catData, setCatData] = useState(false);

 const [setViewPdf]=useState(false);
 const allowedFIles = ['application/pdf'];


  const handleSwitchChange = () => {
      return setOption(!option);
      
    
  }

  const handleInputChange = () => {
    return setInput(!input)
  }

  
  const handleFileChange = (e) =>{
    let selectedFile = e.target.files[0];
    localStorage.setItem("backup", selectedFile);
    if(selectedFile){
        if(selectedFile && allowedFIles.includes(selectedFile.type)){
            let reader = new FileReader();
            console.log(selectedFile);
            setSubmit(true);

            setRawFile(e.target.files[0])

            reader.readAsDataURL(selectedFile);


            reader.onloadend=(e)=>{
                setPdfError('');
                setPdfFile(e.target.result);
            }
            

            
        } else{
            setPdfFile(null);
            setPdfError('Not a vaild pdf: Please select a PDF');
        }
    } else {
        console.log('select a PDF');
    }
}




let handleFileSubmit= async (e)=>{
  e.preventDefault();
  
  //setGradeData(resJson["scores"])
  //setJobData(resumeData['similarjobs'])
   
  //setCatData(resumeData['predicition'])

  //setInput(true)
  //let resJson = resumeData
  //console.log(resumeData)

  
  if(pdfFile!==null){
    try{
      const formData = new FormData();
      formData.append("file", rawFile);

      

      let res = await fetch("http://127.0.0.1:5000/data", {
        method: "POST",
        body: formData
      });


      if (res.status === 200){
        
        let resJson = await res.json();
        console.log(resJson)
        setGradeData(resJson['scores'])
        setTotalScore(resJson['TotalScore'])
        setCatData(resJson['prediction'])
        setJobData(resJson['similarjobs'])
        setInput(true)
        //setViewPdf(pdfFile);
        
      }
    } catch (err) {
      console.log(err);
    }
  } else {
      setViewPdf(null);
  } 
}
// document.getElementById("input_button").disabled = true;
//   var myInput = document.getElementById("input_button");
//   if (myInput.value.length > 0){
//     document.getElementById("input_button").disabled = false;
//   }

  
  return (
    
    <div id="master_container">
      {!input ?
        <div className="pdf_container">
          <div id="input_wrapper">
            <div class="input_card">
              <h5 className="input_title">Upload your resume to continue.</h5>
              <form className='form-group' onSubmit={handleFileSubmit} form="nameform">

                <div className='input_div'>
                <input type='file' className='input_submit' onChange={handleFileChange}></input>
                
                </div>
                <Link to='/' >
                  <button type="button" form="nameform" id="back_input_button" onClick="Home()">Back</button>     
                </Link>      
                {!submit ?  <input disabled id="input_button" type="submit" value="Submit"  /> :  <input enabled id="input_button" type="submit" value="Submit"  /> }
               
                
                {pdfError && <span className='text-danger'>{pdfError}</span>}
              </form>
            </div>
            

            
          </div>
        </div>
      :
        <div className="pdf_container">
          {option ?
            <div id="mydivon" class="split_left">
              <h2 class="headingText">Overall Score:</h2>
              <div id="topper_wrapper">
                <div id="overallScore" style={{ width: 250, height: 250 }}>
                  <VisibilitySensor>
                    {({ isVisible }) => {
                    const percentage = isVisible ? Math.round(totalScore * 100) : 0;
                      return (
                        <CircularProgressbar value={percentage} 
                          text={`${percentage}%`} 
                          styles={buildStyles({
                            textColor: "#e0e2db",
                            pathColor: "#e6af2e",
                            trailColor: "#e0e2db"
                          })}/>
                      );
                    }}
                  </VisibilitySensor>
                </div>
                <div id="side_blurb">
                  <h4>Our Total Score Distribution is calculated by:</h4>
                  <ul>
                    <li>Grammar - 50%</li>
                    <li>Resume Requirements - 20%</li>
                    <li>Word Score - 15%</li>
                    <li>Numeric Score- 15%</li>
                  </ul>
                  <h4>There is always room to improve!</h4>
                </div>
              </div>
              <h2 class="headingText">Sub Scores:</h2>
              <GradeCards gradesInfo={gradesData}/>
            </div>
            : 
            <div id="mydivoff" class="split_left">
              <h2 class="headingText">Top 3 Job Categories:</h2>
              <CategoryCards catInfo = {catData}/>
              <h2 class="headingText">Reccomended Jobs:</h2>
               <JobCards jobInfo = {jobData} /> 
            </div>
          }
            
            
              
            <div class="split_right ">
                <div>
                    <button type="button" form="nameform" id="switchButton" onClick={()=> handleSwitchChange() } >Switch Mode</button>
                    
                    <button type="button" form="nameform" id="newResuButton" onClick={()=> handleInputChange()}>New Resume</button>

                    <Link to='/' >
                      <button type="button" form="nameform" id="backButton"  onClick={()=> handleInputChange()}>Back</button>
                    </Link>
                    
                    
                    
            
                    
                    <div className = "pdf_viewer">
                        {pdfFile && ( <iframe title="frameDisplay" src= {pdfFile}   width="100%" height="100%" > </iframe>)}
                        {!pdfFile && <>No file is selected yet</>}
                           
                    </div> 
                     

                </div>
            </div>
        </div>
      }
    </div>
    
  );
}



export default ResumeChecker;
 //<PDFViewerReact document={{ url: pdfFile}} hideNavbar={true} scale={1.5}/>