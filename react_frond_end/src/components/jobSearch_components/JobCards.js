import React from 'react'
import JobCardItem from './JobCardItem'
import './JobCards.css';
import Carousel from '../other_components/Carousel';

function JobCards() {
    
  return (
    <div >
        <Carousel>
            <div className='cards__container'><div className='cards__wrapper'><JobCardItem text="Sample Text" company="Job Company" location="Job Location" path='' percent= { 90 }/></div></div>
            <div className='cards__container'><div className='cards__wrapper'><JobCardItem text="Sample Text" company="Job Company" location="Job Location" path='' percent= { 90 }/></div></div>
            <div className='cards__container'><div className='cards__wrapper'><JobCardItem text="Sample Text" company="Job Company" location="Job Location" path='' percent= { 90 }/></div></div>
            

            
            
            <div className='cards__container'><div className='cards__wrapper'><JobCardItem text="Sample Text" company="Job Company" location="Job Location" path='' percent= { 90 }/></div></div>
            <div className='cards__container'><div className='cards__wrapper'><JobCardItem text="Sample Text" company="Job Company" location="Job Location" path='' percent= { 90 }/></div></div>
            <div className='cards__container'><div className='cards__wrapper'><JobCardItem text="Sample Text" company="Job Company" location="Job Location" path='' percent= { 90 }/></div></div>
            <div className='cards__container'><div className='cards__wrapper'><JobCardItem text="Sample Text" company="Job Company" location="Job Location" path='' percent= { 90 }/></div></div>
            <div className='cards__container'><div className='cards__wrapper'><JobCardItem text="Sample Text" company="Job Company" location="Job Location" path='' percent= { 90 }/></div></div>
            <div className='cards__container'><div className='cards__wrapper'><JobCardItem text="Sample Text" company="Job Company" location="Job Location" path='' percent= { 90 }/></div></div>
            <div className='cards__container'><div className='cards__wrapper'><JobCardItem text="Sample Text" company="Job Company" location="Job Location" path='' percent= { 90 }/></div></div>
  
        </Carousel>
    </div>      
           
  )
}
 
export default JobCards;