import React from 'react'
import JobCardItem from './JobCardItem'
import './JobCards.css';
import Carousel from '../other_components/Carousel';

function JobCards(data) {
    
  return (
    <div >
        <Carousel>
          {
            data['jobInfo'].map( (value) => ( 
              <div className='job_div'>
                <JobCardItem text={value['positionName']} 
                  company={value['company']} 
                  location={value['location']} 
                  path={value['url']} 
                  percent= {Math.round(Math.pow(value['similarity score'], 1/7) * 100)}/>
                  
             </div>
              
                  
            ))

              
                      
          }

            
              
        </Carousel>
        
        
        
    </div>      
           
  )
}
 
export default JobCards;