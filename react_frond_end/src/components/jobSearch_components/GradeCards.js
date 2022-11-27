import React from 'react'
import GradeCardItem from './GradeCardItem'
import './GradeCards.css';

function GradeCards() {
  return (
    <div >
        <div className='cards__container'>
            <div className='cards__wrapper'>
                
                    <GradeCardItem 
                        
                        title="Filler"
                        desc="Filler"
                        percent= { 90 }
                    />
                    <GradeCardItem 
                        
                        title="Filler"
                        desc="Filler"
                        percent= { 90 }
                    />
                    <GradeCardItem 
                        
                        title="Filler"
                        desc="Filler"
                        percent= { 90 }
                    />
                    <GradeCardItem 
                        
                        title="Filler"
                        desc="Filler"
                        percent= { 90 }
                    />
                
            </div>
        </div>
      
    </div>
  )
}

export default GradeCards;