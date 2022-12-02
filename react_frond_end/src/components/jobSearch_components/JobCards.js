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
             <JobCardItem text={value['positionName']} 
              company={value['company']} 
              location={value['location']} 
              path={value['url']} 
              percent= {Math.round(value['similarity score'] * 100)}/>
               ))   
                  
          }
        </Carousel>
    </div>      
           
  )
}
 
export default JobCards;