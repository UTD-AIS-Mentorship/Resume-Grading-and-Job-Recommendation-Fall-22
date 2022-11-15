import React, { useState } from "react";
import './PDFViewer.css';
import PDFViewerReact from 'pdf-viewer-reactjs';

//import {fromPath} from "pdf2pic";

function PDFViewer(){
    
    //var fileText = [];
    //var pdfImage;
    //const images = [];
   
    const [pdfFile,setPdfFile]=useState(null);
    const [pdfError, setPdfError]=useState('');

    const [setViewPdf]=useState(null);

    //const pdfjs = require("pdfjs-dist/build/pdf");

    //const pdf2html = require('pdf2html')

    /*
    const options = {
        density: 100,
        saveFilename: "untitled",
        savePath: "./images",
        format: "png",
        width: 600,
        height: 600
    }
    */

    /*
    async function getContent (src){
        const doc = await pdfjs.getDocument({data: atob(src)}).promise;
        const page = await doc.getPage(1);
        return await page.getTextContent();
    }
    

    async function getItems(src){
        var text = "";
        const content = await getContent(src);
         content.items.forEach((item) => { 
            text = text + "" + item.str; 
            console.log(item.str);
        })
        return text
    }
    */

    const allowedFIles = ['application/pdf'];
    const handleFileChange = (e) =>{
        let selectedFile = e.target.files[0];
        if(selectedFile){
            if(selectedFile && allowedFIles.includes(selectedFile.type)){
                let reader = new FileReader();
                console.log(selectedFile);
                reader.readAsDataURL(selectedFile);

                //var dataURL = reader.readAsDataURL(selectedFile);

                reader.onloadend=(e)=>{
                    setPdfError('');
                    setPdfFile(e.target.result);
                }

                //console.log(reader.result);
                //var blob = window.dataURLtoBlob(reader.result);
                //console.log(blob);
                //var byteString = atob(dataURL.split(',')[1]);
                
                
                //var mimeString = dataURL.split(',')[0].split(':')[1].split(';')[0]
                
                //var ab = new ArrayBuffer(byteString.length);
                
                //var ia = new Uint8Array(ab);
                
                /*
                for (var i = 0; i < byteString.length; i++) {
                    ia[i] = byteString.charCodeAt(i);
                }

                var blob = new Blob([ab], {type: mimeString});
                console.log(blob);
                */

                /*
                return new Promise ((resolve) =>{
                    reader.onload = async () => {
                        var base64 = reader.result;
                        var getText = await
                        getItems(base64.replace("data:application/pdf;base64,",""))
                        
                        fileText.push({text: getText});
                        resolve(fileText);     
                        
                        console.log(fileText[0].text)
                    }
                })
                */
            } else{
                setPdfFile(null);
                setPdfError('Not a vaild pdf: Please select a PDF');
            }
        } else {
            console.log('select a PDF');
        }
    }

    const handleFileSubmit=(e)=>{
        e.preventDefault();
        if(pdfFile!==null){
            setViewPdf(pdfFile);
        } else {
            setViewPdf(null);
        }
    }

    return (
        <>
            <form className='form-group' onSubmit={handleFileSubmit}>
                        <label><h5>Upload PDF</h5></label>
                        <br></br>

                        <input type='file' className='form-control' onChange={handleFileChange}></input>
                        {pdfError && <span className='text-danger'>{pdfError}</span>}

                    </form>
                    <div className = "pdf_viewer">
                        {pdfFile && (<PDFViewerReact document={{ url: pdfFile}} />)}
                        {!pdfFile && <>No file is selected yet</>}
                        <img src={pdfFile} alt =""></img>     
                    </div>
        </>
                           
                    


    );
}

export default PDFViewer;